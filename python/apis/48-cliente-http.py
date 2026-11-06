"""48. Cliente HTTP: realiza requisições GET e POST pelo terminal.

Uso:
  python 48-cliente-http.py GET https://httpbin.org/get
  python 48-cliente-http.py POST https://httpbin.org/post --json '{"nome": "Lab"}'
"""

import argparse
import json
import sys

import requests

TIMEOUT_SECONDS = 15
MAX_BODY_LENGTH = 600


def send_request(method: str, url: str, raw_json: str | None = None) -> requests.Response:
    if method == "GET" and raw_json is not None:
        raise ValueError("--json só pode ser usado com POST.")
    try:
        payload = None if raw_json is None else json.loads(raw_json)
    except json.JSONDecodeError as error:
        raise ValueError(f"Corpo JSON inválido: {error.msg}") from error
    return requests.request(method, url, json=payload, timeout=TIMEOUT_SECONDS)


def format_response(response: requests.Response) -> str:
    content_type = response.headers.get("Content-Type", "desconhecido")
    body = response.text
    if len(body) > MAX_BODY_LENGTH:
        body = f"{body[:MAX_BODY_LENGTH]}... ({len(response.text)} caracteres no total)"
    return f"Status: {response.status_code} {response.reason}\nTipo: {content_type}\n\n{body}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Cliente HTTP simples.")
    parser.add_argument("method", type=str.upper, choices=["GET", "POST"])
    parser.add_argument("url")
    parser.add_argument("--json", dest="raw_json", help="corpo JSON de um POST")
    options = parser.parse_args()
    try:
        response = send_request(options.method, options.url, options.raw_json)
    except ValueError as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede: {error}")
        return 1
    print(format_response(response))
    return 0 if response.ok else 1


if __name__ == "__main__":
    sys.exit(main())
