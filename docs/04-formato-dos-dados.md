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

## `data/descricoes.json`
Gerado por `scripts/descrever.py`: `{url: descrição}` com a descrição pública (campo "About") dos repositórios do GitHub cuja lista de origem não tem descrição ou não permite copiar o texto. O `selecionar.py` usa esse arquivo; link que continua sem descrição não entra no guia.

## `data/repos-ia-consultas.json`
As consultas da busca do GitHub para os repositórios de IA de cada profissão. Em `trilhas`, cada slug de trilha tem uma lista de temas no formato `[emoji, nome, descrição, [consultas]]`. Em `geral` fica o tema de uso geral, que completa a lista quando os temas da profissão não chegam a 1000.

## `data/repos-ia.jsonl`
Gerado por `scripts/coletar_repos_ia.py`: uma linha por repositório e por profissão, com `trilha`, `tema` (índice do tema; `-1` é o tema geral), `nome` (`dono/repo`), `url`, `descricao`, `estrelas`, `linguagem`, `licenca` e `atualizado`. São exatamente 1000 linhas por trilha. O resumo da coleta fica em `data/repos-ia-meta.json`.

## `data/i18n/`
- `textos.pt.json`: os textos da interface (títulos, descrições de seção, rótulos) em português, com marcadores como `{n}` e `{area}`. Os nomes e descrições de setores, áreas, trilhas e temas vêm dos próprios dados.
- `textos.<idioma>.json`: a tradução de todos esses textos. `scripts/conferir_textos.py` confere chaves, marcadores e marcação.
- `desc.<idioma>.json.gz`: gerado por `scripts/traduzir.py`. `{hash: tradução}` das descrições e dos nomes de tópico, onde o hash são os 14 primeiros caracteres do SHA-1 do texto original já limpo.
