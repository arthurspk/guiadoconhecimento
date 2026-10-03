# 08 · Como contribuir

> O guia cresce com a comunidade. Veja como sugerir cada tipo de mudança.

[🏠 Início](../README.md)

## Sugerir um link essencial
Adicione um objeto em [`data/essenciais.json`](../data/essenciais.json):

```json
{"nome": "Nome do recurso", "url": "https://...", "descricao": "Uma frase objetiva em pt-BR.", "tipo": "site", "idioma": "pt", "gratuito": true, "area": "edicao-de-video"}
```

Regras: abra o link antes de sugerir; descrição sem exagero e sem emoji; prefira gratuito e oficial.

## Sugerir uma lista curada (fonte)
Adicione em [`data/fontes.json`](../data/fontes.json) com `repo`, `arquivos`, `area` e `licenca`. A lista deve ser mantida, focada na área e ter licença que permita o uso (veja docs/07).

## Sugerir uma área ou trilha nova
Edite [`data/taxonomia.json`](../data/taxonomia.json) ou [`data/trilhas.json`](../data/trilhas.json) e explique no pull request por que a área não cabe nas existentes.

## Traduzir
O guia sai em 12 idiomas. Há dois tipos de texto:

- **Textos da interface** (títulos, descrições de seção, nomes de áreas e profissões): ficam em `data/i18n/textos.<idioma>.json`. Corrija ali e rode `python3 scripts/conferir_textos.py <idioma>`.
- **Descrições dos links e nomes de tópico**: são traduzidas automaticamente por `scripts/traduzir.py` e ficam em `data/i18n/desc.<idioma>.json.gz`. Se uma tradução ficou ruim, abra uma issue com a página e o link.

Nunca edite as páginas em `i18n/`: elas são geradas.

## Antes de enviar

```bash
python3 scripts/selecionar.py && python3 scripts/gerar.py && python3 tests/validar.py
```

O PR deve mudar só `data/` e as páginas geradas. Não edite as páginas `.md` de área à mão: elas são sobrescritas pelo gerador.
