# 06 · Curadoria e qualidade

> Um guia com 15 mil links só é útil se cada página for enxuta e confiável. Estas são as regras.

[🏠 Início](../README.md)

## O que entra

- **Essenciais:** de 12 a 20 por área, escolhidos à mão, com descrição objetiva em português, preferindo conteúdo gratuito, oficial e brasileiro quando bom. Na curadoria, cada URL foi aberta ou confirmada em listas curadas; a checagem automática contínua é feita pelo `checar_links.py`.
- **Fontes curadas:** listas do GitHub mantidas (atividade recente), focadas na área e com licença registrada.
- **Links das fontes:** a seleção faz rodízio entre os tópicos de cada lista (até 6 por tópico a cada volta), respeitando a ordem da lista dentro do tópico e respeitando a ordem da lista. Assim a área cobre a lista inteira, não só o começo.
- **Todo link tem descrição.** Se a lista de origem não tem descrição, ou a licença dela não permite copiar o texto, vale a descrição pública do próprio repositório no GitHub (`data/descricoes.json`). Sem nenhuma das duas, o link não entra.
- **Repositórios de IA por profissão:** 1000 por trilha, vindos da busca do GitHub com as consultas de `data/repos-ia-consultas.json`. Só entram repositórios ativos, com pelo menos 3 estrelas, descrição em alfabeto latino, sinal claro de IA no nome, na descrição ou nos tópicos, e fora de uma lista de bloqueio (conteúdo adulto, pirataria, trapaça). A ordem é por estrelas.

## O que não entra

- Links de navegação, selos (badges), imagens, licenças, páginas de issues e PRs, e o próprio repositório da fonte.
- Nomes genéricos ("link", "aqui", "source", "demo").
- Duplicados dentro da mesma área (a URL é normalizada antes de comparar).
- Descrições de fontes sem licença, GPL ou não comerciais (fica só nome e link).
- Descrições que são fragmentos (começam com "or", "and", "by", "see"...), selos de estrelas e marcas de licença coladas.
- Parâmetros de rastreio e de afiliado nas URLs (`utm_*`, `ref`, `aff`, `tag` da Amazon).
- Tópicos fora do tema de uma fonte, configurados em `excluir_topicos` no `data/fontes.json`.

## Tetos por área

Para nenhuma página virar um muro de links, cada área tem um teto de links coletados: **170** na maioria, **260** nas áreas grandes (front-end, back-end, DevOps, IA, segurança, ferramentas) e **1.300** em *Linguagens*, onde cada linguagem tem sua seção. A seção 🤖 de IA tem teto próprio: os essenciais de IA mais **30** links de IA coletados. Os tetos estão em `scripts/selecionar.py` (`--teto`, `--teto-grande`, `--teto-linguagens`, `--teto-ia`).

Dentro do teto, a seleção faz **rodízio entre as fontes**: pega um item de cada fonte por vez, para nenhuma lista dominar a área. As fontes do autor (guias em português) entram primeiro no rodízio.

## Manutenção

- `scripts/checar_links.py` confere os links e o `selecionar.py` remove os quebrados; um link só sai depois de falhar em **duas** rodadas seguidas, e essenciais nunca são removidos automaticamente.
- Fontes paradas há mais de 3 anos devem ser revistas; troque por uma alternativa mantida quando houver.
- Toda mudança passa por `tests/validar.py`.
