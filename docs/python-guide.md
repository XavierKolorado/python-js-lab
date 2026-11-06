# Guia de Python / Python guide

[Voltar ao README / Back to the README](../README.md)

## Preparar o ambiente / Set up

Requer Python 3.10 ou mais recente. Só os exercícios 41 a 49 usam a biblioteca `requests`.
*Requires Python 3.10 or newer. Only exercises 41 to 49 use the `requests` library.*

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

No Windows, ative com `.venv\Scripts\activate`. / *On Windows, activate with `.venv\Scripts\activate`.*

```bash
pip install -r requirements-dev.txt
```

## Executar / Run

Cada arquivo é independente. Execute a partir da raiz do repositório.
*Each file stands alone. Run it from the repository root.*

```bash
python python/fundamentos/04-media-notas.py
```

## Padrão dos exercícios / Exercise pattern

- Funções puras guardam a regra; `main()` cuida de entrada e saída. / *Pure functions hold the rule; `main()` handles input and output.*
- `if __name__ == "__main__":` permite importar o arquivo nos testes. / *It lets tests import the file.*
- Pequenas funções de leitura se repetem de propósito: cada exercício roda sozinho, sem módulo compartilhado. / *Small input helpers repeat on purpose: each exercise runs alone, with no shared module.*
- Identificadores usam inglês; mensagens ao usuário usam português. / *Identifiers are in English; user messages are in Portuguese.*

## Dados locais / Local data

Os exercícios 31, 33 a 36, 39, 49 e 50 gravam em uma pasta `dados/` ao lado do script. Essa pasta é ignorada pelo Git. Quase todos aceitam outro caminho como argumento.
*Exercises 31, 33 to 36, 39, 49 and 50 write to a `dados/` folder beside the script. Git ignores that folder. Nearly all accept another path as an argument.*

## Senhas / Passwords

Os exercícios 18 e 50 usam PBKDF2 com salt. Eles ensinam a nunca guardar senha em texto puro, mas continuam didáticos. Um sistema real precisa de limite de tentativas persistente, sessões seguras, HTTPS e, de preferência, uma biblioteca ou serviço de autenticação consolidado.
*Exercises 18 and 50 use salted PBKDF2. They teach you never to store plain-text passwords, but they remain lessons. A real system needs persistent rate limiting, secure sessions, HTTPS and, ideally, an established authentication library or service.*

A senha `lab-demo` do exercício 18 é pública e serve só para a demonstração.
*The `lab-demo` password in exercise 18 is public and exists only for the demo.*

## Testes / Tests

```bash
python -m pytest
```

Os testes de API trocam a rede por respostas falsas, então funcionam sem internet.
*API tests replace the network with fake responses, so they work offline.*
