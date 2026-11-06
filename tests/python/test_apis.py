"""API tests replace the network with fakes. tools/check_apis.py covers the real endpoints."""

import json
from unittest.mock import patch

import pytest
import requests

from helpers import load


class FakeResponse:
    def __init__(self, payload=None, status_code=200, text="", headers=None):
        self.payload = payload
        self.status_code = status_code
        self.text = text
        self.headers = headers or {}
        self.reason = "OK" if status_code < 400 else "Error"
        self.ok = status_code < 400

    def json(self):
        return self.payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")


SAMPLE_ADDRESS = {
    "cep": "01001-000",
    "logradouro": "Praça da Sé",
    "complemento": "",
    "bairro": "Sé",
    "localidade": "São Paulo",
    "uf": "SP",
    "estado": "São Paulo",
    "regiao": "Sudeste",
    "ddd": "11",
}


def test_41_normalizes_and_validates_cep():
    module = load(41)
    assert module.normalize_cep("01001-000") == "01001000"
    with pytest.raises(ValueError):
        module.normalize_cep("123")


def test_41_success_and_not_found():
    module = load(41)
    with patch.object(module.requests, "get", return_value=FakeResponse(SAMPLE_ADDRESS)) as fake_get:
        assert module.fetch_cep("01001-000")["uf"] == "SP"
    assert "01001000" in fake_get.call_args.args[0]
    assert fake_get.call_args.kwargs["timeout"] > 0
    with patch.object(module.requests, "get", return_value=FakeResponse({"erro": "true"})):
        with pytest.raises(LookupError):
            module.fetch_cep("99999-999")


def test_41_network_failure_gives_friendly_exit(capsys):
    module = load(41)
    with patch.object(module.sys, "argv", ["x", "01001000"]):
        with patch.object(module.requests, "get", side_effect=requests.ConnectionError("sem rede")):
            assert module.main() == 1
    assert "Erro de rede" in capsys.readouterr().out


def test_42_city_lookup_and_weather_text():
    module = load(42)
    city = {"name": "Curitiba", "latitude": -25.4, "longitude": -49.2}
    with patch.object(module.requests, "get", return_value=FakeResponse({"results": [city]})):
        assert module.find_city("Curitiba") == city
    with patch.object(module.requests, "get", return_value=FakeResponse({})):
        with pytest.raises(LookupError):
            module.find_city("Xyzzy")
    with pytest.raises(ValueError):
        module.find_city("  ")
    assert module.describe_weather(0) == "céu limpo"
    assert "desconhecida" in module.describe_weather(1234)


def test_43_results_and_404_means_empty():
    module = load(43)
    character = {"name": "Rick", "species": "Human", "status": "Alive"}
    payload = {"info": {"count": 1}, "results": [character]}
    with patch.object(module.requests, "get", return_value=FakeResponse(payload)):
        assert module.search_characters("rick") == (1, [character])
    with patch.object(module.requests, "get", return_value=FakeResponse(status_code=404)):
        assert module.search_characters("xyz") == (0, [])
    assert module.format_character(character) == "Rick (Human, Alive)"


def test_44_card_skips_empty_fields():
    card = load(44).format_address(SAMPLE_ADDRESS)
    assert "Praça da Sé" in card
    assert "Complemento" not in card


def test_44_continues_after_a_bad_cep(capsys):
    module = load(44)
    with patch.object(module.sys, "argv", ["x", "123", "01001000"]):
        with patch.object(module.requests, "get", return_value=FakeResponse(SAMPLE_ADDRESS)):
            assert module.main() == 1
    output = capsys.readouterr().out
    assert "CEP inválido" in output and "Praça da Sé" in output


def test_45_conversion_and_validation():
    module = load(45)
    payload = {"rates": {"BRL": 5.0}, "date": "2026-01-02"}
    with patch.object(module.requests, "get", return_value=FakeResponse(payload)):
        assert module.convert(10, "usd", "brl") == (50.0, 5.0, "2026-01-02")
    with patch.object(module.requests, "get", return_value=FakeResponse(status_code=404)):
        with pytest.raises(LookupError):
            module.convert(10, "usd", "xxx")
    for arguments in [(-1, "USD", "BRL"), (float("nan"), "USD", "BRL"), (1, "US", "BRL"), (1, "USD", "USD")]:
        with pytest.raises(ValueError):
            module.convert(*arguments)


def test_46_validates_url_and_reads_service_errors():
    module = load(46)
    with pytest.raises(ValueError):
        module.shorten_url("ftp://example.com")
    with pytest.raises(ValueError):
        module.shorten_url("sem-protocolo")
    with patch.object(module.requests, "get", return_value=FakeResponse({"shorturl": "https://is.gd/x"})):
        assert module.shorten_url("https://example.com") == "https://is.gd/x"
    with patch.object(module.requests, "get", return_value=FakeResponse({"errormessage": "bloqueada"})):
        with pytest.raises(LookupError, match="bloqueada"):
            module.shorten_url("https://example.com")


def test_47_client_uses_the_right_verbs():
    module = load(47)
    client = module.TaskApiClient("https://api.test/todos")
    with patch.object(client.session, "request", return_value=FakeResponse({"id": 201})) as fake_request:
        client.create_task(" Estudar ")
        assert fake_request.call_args.args == ("POST", "https://api.test/todos")
        assert fake_request.call_args.kwargs["json"]["title"] == "Estudar"
        client.complete_task(5)
        assert fake_request.call_args.args == ("PATCH", "https://api.test/todos/5")
        client.delete_task(5)
        assert fake_request.call_args.args == ("DELETE", "https://api.test/todos/5")
    with pytest.raises(ValueError):
        client.create_task("  ")


def test_48_validates_body_before_sending():
    module = load(48)
    with pytest.raises(ValueError):
        module.send_request("POST", "https://api.test", "{quebrado")
    with pytest.raises(ValueError):
        module.send_request("GET", "https://api.test", "{}")
    with patch.object(module.requests, "request", return_value=FakeResponse()) as fake_request:
        module.send_request("POST", "https://api.test", '{"a": 1}')
    assert fake_request.call_args.kwargs["json"] == {"a": 1}


def test_48_truncates_long_bodies():
    module = load(48)
    response = FakeResponse(text="x" * 5000, headers={"Content-Type": "text/plain"})
    formatted = module.format_response(response)
    assert "5000 caracteres" in formatted and len(formatted) < 800


def test_49_export_shape_and_file(tmp_path):
    module = load(49)
    record = {
        "id": 1,
        "name": "Ana",
        "email": "a@e.co",
        "address": {"city": "Recife"},
        "company": {"name": "Lab"},
    }
    export = module.build_export([record])
    assert export["total"] == 1
    assert export["records"][0] == {
        "id": 1, "name": "Ana", "email": "a@e.co", "city": "Recife", "company": "Lab",
    }
    path = tmp_path / "saida" / "export.json"
    module.save_export(path, export)
    assert json.loads(path.read_text(encoding="utf-8"))["total"] == 1


def test_50_password_is_hashed_with_individual_salt(tmp_path):
    module = load(50)
    path = tmp_path / "sistema.json"
    store = module.AppStore(path)
    store.register("Ana", "senha-teste-1")
    store.register("bia", "senha-teste-1")
    content = path.read_text(encoding="utf-8")
    assert "senha-teste-1" not in content
    assert store.users["ana"]["password_hash"] != store.users["bia"]["password_hash"]


def test_50_authentication_and_notes_survive_reload(tmp_path):
    module = load(50)
    path = tmp_path / "sistema.json"
    store = module.AppStore(path)
    store.register("ana", "senha-teste-1")
    assert store.authenticate("ANA", "senha-teste-1") == "ana"
    assert store.authenticate("ana", "errada") is None
    assert store.authenticate("ninguem", "senha-teste-1") is None
    store.add_note("ana", "lembrar")
    reloaded = module.AppStore(path)
    assert reloaded.notes_of("ana") == ["lembrar"]
    reloaded.delete_note("ana", 1)
    with pytest.raises(ValueError):
        reloaded.delete_note("ana", 1)


@pytest.mark.parametrize(
    ("username", "password"),
    [("ana silva", "senha-longa"), ("", "senha-longa"), ("ana", "curta")],
)
def test_50_rejects_bad_registrations(tmp_path, username, password):
    store = load(50).AppStore(tmp_path / "sistema.json")
    with pytest.raises(ValueError):
        store.register(username, password)
