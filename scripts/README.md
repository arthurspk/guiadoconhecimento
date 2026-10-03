# 📜 Scripts

> Tudo em Python 3. Gerar e validar só precisam da stdlib; o Scrapling melhora a coleta e a checagem, o `gh` autenticado é usado nas consultas ao GitHub e o Argos Translate faz a tradução.

[🏠 Início](../README.md)

| Script | Entrada | Saída | Para que serve |
|---|---|---|---|
| `coletar.py` | `data/fontes*.json` | `data/brutos.jsonl.gz` | Baixa as listas curadas (Scrapling → git) e extrai os links. `--area <slug>` recoleta uma área e mescla; `--sem-scrapling`. |
| `descrever.py` | `brutos.jsonl.gz` | `data/descricoes.json` | Busca a descrição pública dos repositórios do GitHub que ficaram sem descrição (`gh api graphql`, 100 por chamada). |
| `selecionar.py` | `brutos.jsonl.gz`, `essenciais.json`, `descricoes.json` | `data/links.jsonl` | Normaliza, deduplica, aplica licenças, exige descrição, aplica tetos e rodízio. `--teto`, `--teto-grande`, `--teto-linguagens`. |
| `coletar_repos_ia.py` | `data/repos-ia-consultas.json` | `data/repos-ia.jsonl` | Busca no GitHub os repositórios de IA de cada profissão, 1000 por trilha. `--trilha <slug>` recoleta uma. |
| `traduzir.py` | `links.jsonl`, `repos-ia.jsonl` | `data/i18n/desc.<idioma>.json.gz` | Traduz descrições e tópicos offline (Argos Translate no CTranslate2). Incremental. `--idiomas es,fr`. |
| `conferir_textos.py` | `data/i18n/textos.*.json` | código de saída | Confere a tradução dos textos da interface contra o português. |
| `gerar.py` | `data/*` | `README*.md`, `areas/`, `trilhas/`, `ia/`, `i18n/`, `docs/07`, `data/links.csv` | Gera as páginas em todos os idiomas. Determinístico. `--idiomas pt,en`. |
| `checar_links.py` | `links.jsonl` | `data/status-links.json` | Confere links. `--area`, `--limite`. O `selecionar.py` tira os que falharam 2 vezes. |
| `../tests/validar.py` | tudo | código de saída | Confere dados, páginas, idiomas, descrições, âncoras e links internos. |

`base.py` (idiomas, textos, emojis, caminhos) e `gerar_ia.py` (páginas de IA) são módulos usados pelo `gerar.py`.

## Ordem

```bash
python3 scripts/coletar.py && python3 scripts/descrever.py && python3 scripts/selecionar.py \
  && python3 scripts/coletar_repos_ia.py && python3 scripts/traduzir.py \
  && python3 scripts/gerar.py && python3 tests/validar.py
```
