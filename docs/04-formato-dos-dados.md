# 04 · Formato dos dados

> Todas as páginas são geradas a partir dos arquivos em [`data/`](../data). Esta página descreve cada um.

[🏠 Início](../README.md)

## `data/taxonomia.json`
Setores e áreas: `slug`, `nome`, `emoji`, `descricao` e a lista de `areas` de cada setor.

## `data/fontes.json` e `data/fontes-guias.json`
As listas curadas de onde os links são coletados.

| Campo | Exemplo | Uso |
|---|---|---|
| `repo` | `teles/awesome-seo` | Repositório no GitHub. |
| `arquivos` | `["README.md"]` | Arquivos markdown/rst que têm os links. |
| `area` | `seo` | Área de destino. `_mapa` indica fonte que cobre várias áreas. |
| `mapa` | `[["Pentest", "ciberseguranca"]]` | Só em fontes `_mapa`: expressão do cabeçalho → área. |
| `licenca` | `CC0-1.0` | Decide se a descrição pode ser reaproveitada (docs/07). |
| `excluir_topicos` | `"Competitions|Conferences"` | Opcional: regex de tópicos da fonte que não entram (fora do tema da área). |
| `ultimo_commit`, `links`, `nota` | | Informação de curadoria. |

## `data/essenciais.json`
Os links "Comece por aqui" e os essenciais de IA (com `"ia": true`), escritos pela curadoria: `nome`, `url`, `descricao` (pt-BR), `tipo`, `idioma`, `gratuito`, `area`, `ia`.

## `data/brutos.jsonl.gz`
Saída do coletor (compactada e versionada, para o `selecionar.py` funcionar num clone novo), uma linha por item encontrado nas fontes: `nome`, `url`, `descricao`, `topico` (cabeçalho H2), `subtopico` (H3), `area`, `fonte`, `arquivo`, `licenca`.

## `data/links.jsonl`
A base final, uma linha por link publicado.

| Campo | Descrição |
|---|---|
| `nome`, `url`, `descricao` | O link. Descrição vazia quando a licença da fonte não permite copiá-la. |
| `area`, `topico`, `grupo` | Onde aparece. `grupo` é usado em *Linguagens* (a linguagem). |
| `tipo` | `site`, `repositorio`, `awesome`, `curso`, `canal`, `video`, `livro`, `comunidade`, `documentacao`, `app`, `ferramenta`. |
| `idioma` | Nos essenciais: `pt`, `en`, `es` ou `multi`. Nos coletados: `pt` quando detectado (domínio `.br`, arquivo pt_BR ou descrição em português), senão vazio. |
| `essencial` | `true` para os links da curadoria. |
| `ia` | `true` para os links da seção 🤖 IA da área (docs/09). |
| `fonte`, `licenca_fonte` | De onde veio (`curadoria` para os essenciais). |

## `data/links.csv`
A mesma base em CSV, para abrir em planilha.

## `data/status-links.json`
Gerado por `scripts/checar_links.py`: para cada URL, `status` (`ok`, `quebrado`, `erro`), `codigo`, `falhas` seguidas e data.

## `data/trilhas.json`
As trilhas por profissão: `nome`, `emoji`, `resumo` e a lista ordenada de `areas`.
