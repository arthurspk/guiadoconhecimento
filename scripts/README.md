# 📜 Scripts

> Tudo em Python 3, só stdlib obrigatória. O Scrapling é opcional e melhora a coleta e a checagem.

[🏠 Início](../README.md)

| Script | Entrada | Saída | Para que serve |
|---|---|---|---|
| `coletar.py` | `data/fontes*.json` | `data/brutos.jsonl.gz` | Baixa as listas curadas (Scrapling → git) e extrai os links. `--area <slug>` recoleta uma área e mescla; `--sem-scrapling`. |
| `selecionar.py` | `brutos.jsonl.gz`, `essenciais.json` | `data/links.jsonl` | Normaliza, deduplica, aplica licenças, tetos e rodízio. `--teto`, `--teto-grande`, `--teto-linguagens`. |
| `gerar.py` | `data/*` | `README.md`, `areas/`, `trilhas/`, `docs/07`, `data/links.csv` | Gera as páginas. Determinístico. |
| `checar_links.py` | `links.jsonl` | `data/status-links.json` | Confere links. `--area`, `--limite`. O `selecionar.py` tira os que falharam 2 vezes. |
| `../tests/validar.py` | tudo | código de saída | Confere dados, páginas, âncoras e links internos. |

## Ordem

```bash
python3 scripts/coletar.py && python3 scripts/selecionar.py && python3 scripts/gerar.py && python3 tests/validar.py
```
