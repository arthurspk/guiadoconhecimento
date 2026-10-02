# 05 · Coleta com Scrapling

> Como os links chegam ao guia, por que usamos o [Scrapling](https://github.com/D4Vinci/Scrapling) e como rodar a coleta e a verificação na sua máquina.

[🏠 Início](../README.md)

## O fluxo

```
data/fontes.json ──► coletar.py ──► data/brutos.jsonl.gz ──► selecionar.py ──► data/links.jsonl ──► gerar.py ──► páginas
                       (Scrapling / git)                     (curadoria)                          checar_links.py (Scrapling)
```

1. **Coletar:** para cada fonte, baixa os arquivos markdown do GitHub e extrai cada item de lista: nome, URL, descrição e o cabeçalho sob o qual aparece. O parser entende listas `- [nome](url) - descrição`, tabelas, links de referência (`[nome][1]` e `[nome]: url`), HTML (`<a href>`), reStructuredText (`` `nome <url>`_ ``) e linhas `Nome: https://...`.
2. **Selecionar:** normaliza URLs (tira `utm_`, `www.`, barra final), remove duplicados dentro da área, descarta nomes vazios ou genéricos ("link", "aqui"), aplica a política de licenças e escolhe os links de cada área com teto e rodízio entre fontes (docs/06).
3. **Gerar:** monta as páginas.
4. **Verificar:** confere se cada link responde.

## Por que o Scrapling

O Scrapling foi validado para este projeto:

- **Coleta de listas:** busca os arquivos crus do GitHub (`raw.githubusercontent.com`) com retentativas. Na construção inicial, 343 das 396 fontes vieram por ele em segundos; o `git` serve de reserva automática.
- **Verificação de links:** o `Fetcher` imita um navegador real (TLS e cabeçalhos), então sites que barram robôs simples respondem normalmente. Isso reduz falsos "quebrados".
- **Páginas que não são listas markdown:** diretórios em HTML podem ser raspados com seletores CSS (`page.css('a::attr(href)')`) e o parser adaptativo continua achando os elementos quando o site muda de layout.
- **Limite:** o Scrapling não substitui a curadoria. Ele acha e confere links; quem decide o que entra são as fontes curadas, os essenciais e as regras de qualidade.

## Rodar na sua máquina

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install "scrapling[fetchers]"
scrapling install            # baixa os navegadores, só se for usar StealthyFetcher/DynamicFetcher
python3 scripts/coletar.py              # ou --area <slug> para recoletar só uma área (mescla com o resto)
python3 scripts/selecionar.py
python3 scripts/gerar.py
python3 scripts/checar_links.py --limite 500   # amostra; sem --limite confere tudo
python3 scripts/gerar.py && python3 tests/validar.py
```

## Boas maneiras

- Respeite o `robots.txt` e os termos dos sites; a verificação faz uma requisição por URL, com poucas threads.
- Não use a coleta para copiar conteúdo protegido: o guia guarda **links**, e descrições só quando a licença permite.
