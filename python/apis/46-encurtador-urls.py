"""46. Encurtador de URLs: usa a API pública do is.gd.

Uso: python 46-encurtador-urls.py https://www.python.org/
Atenção: cada URL nova cria um link público e permanente no serviço.
"""

import sys
from urllib.parse import urlparse

import requests

SHORTENER_URL = "https://is.gd/create.php"
TIMEOUT_SECONDS = 10


def validate_url(url: str) -> str:
    clean_url = url.strip()
    parsed = urlparse(clean_url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ValueError("Informe uma URL completa, iniciada por http:// ou https://.")
    return clean_url


def shorten_url(url: str) -> str:
    parameters = {"format": "json", "url": validate_url(url)}
    response = requests.get(SHORTENER_URL, params=parameters, timeout=TIMEOUT_SECONDS)
    response.raise_for_status()
    data = response.json()
    if "shorturl" not in data:
        raise LookupError(data.get("errormessage", "O serviço recusou a URL."))
    return data["shorturl"]


def main() -> int:
    url = sys.argv[1] if len(sys.argv) > 1 else input("URL: ")
    try:
        print(f"URL curta: {shorten_url(url)}")
    except (ValueError, LookupError) as error:
        print(f"Erro: {error}")
        return 1
    except requests.RequestException as error:
        print(f"Erro de rede ao consultar o is.gd: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
