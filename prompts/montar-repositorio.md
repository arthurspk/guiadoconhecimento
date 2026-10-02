# Prompt para o Claude Code: montar, verificar e ampliar o Guia do Conhecimento

> Cole o bloco abaixo no Claude Code, aberto na pasta onde você descompactou o zip (a pasta que tem `README.md`, `data/`, `scripts/`). Ele trabalha em blocos, valida a cada passo e só publica no GitHub quando você confirmar.

---

```text
Você vai montar e finalizar o repositório "Guia do Conhecimento" nesta pasta. É um guia aberto, em pt-BR, com 10.000 a 20.000 links
organizados em setor > área > tópico, com uma seção de inteligência artificial em cada área, para qualquer profissão (dev, editor de vídeo, filmmaker, QA, dados, segurança, tráfego pago,
design, finanças, saúde, educação...). O layout segue o repositório github.com/arthurspk/guiadomaestri (README com proposta,
índice com âncoras, documentação numerada em docs/, catálogo por área, scripts e validação), e o espírito do
github.com/arthurspk/guiadevbrasil (conhecimento gratuito para todos).

Tudo é gerado a partir de data/ por scripts Python. NUNCA edite à mão as páginas em areas/, trilhas/, README.md ou
docs/07: mude data/ ou os scripts e rode o gerador. Leia primeiro: README.md, docs/02, docs/04, docs/05, docs/06 e scripts/README.md.

## Regras
- Trabalhe em BLOCOS (um setor por vez) para não estourar o contexto. Ao fim de cada bloco: rode o pipeline, rode
  `python3 tests/validar.py`, faça um commit com mensagem clara, e resuma em até 5 linhas o que mudou.
- Não invente URL, repositório, nome de skill ou licença. Todo link novo precisa ter sido aberto (WebFetch, Scrapling ou curl).
- Descrições novas em pt-BR, uma frase objetiva, sem emoji e sem exagero.
- Respeite licenças (docs/07): de fonte sem licença, GPL ou NC, só nome e link.
- Total final entre 10.000 e 20.000 links (o validador reprova fora disso). Ajuste os tetos em scripts/selecionar.py se precisar.
- Respeite robots.txt e termos dos sites; poucas threads na verificação.
- Não publique nada (push, criação de repositório) sem a minha confirmação explícita.

## Etapa 1 · Ambiente (uma vez)
python3 -m venv .venv && source .venv/bin/activate
pip install "scrapling[fetchers]"
git init (se ainda não for um repositório) e um primeiro commit com o estado atual.

## Etapa 2 · Reconstruir e validar
python3 scripts/coletar.py      # usa Scrapling; git como reserva. Deve listar ~384 fontes sem FALHA.
python3 scripts/selecionar.py
python3 scripts/gerar.py
python3 tests/validar.py        # deve dizer OK
Se alguma fonte falhar, investigue (repo renomeado, arquivo movido) e corrija data/fontes.json.

## Etapa 3 · Verificar os links com Scrapling (na sua rede, que alcança qualquer site)
python3 scripts/checar_links.py --limite 300   # amostra: confira se a taxa de "ok" é alta e se não há falso positivo
python3 scripts/checar_links.py                # todos (~15 mil URLs; pode levar um tempo)
Rode a checagem completa duas vezes em dias/horários diferentes, depois:
python3 scripts/selecionar.py && python3 scripts/gerar.py && python3 tests/validar.py
(O selecionar.py já lê data/status-links.json e tira os links que falharam 2 vezes seguidas. Essenciais nunca saem sozinhos:
liste os essenciais com falha e revise à mão, trocando a URL ou removendo de data/essenciais.json.)

## Etapa 4 · Ampliar as áreas fracas, um setor por bloco
As áreas abaixo têm poucas listas curadas no GitHub; para cada uma: (a) procure 2 a 5 fontes novas mantidas (awesome lists,
listas em português) e adicione em data/fontes.json com licença e arquivos certos; (b) adicione essenciais verificados em
data/essenciais.json até ter ~20, priorizando conteúdo gratuito, oficial e brasileiro.
- Tecnologia: redes, embarcados-iot, blockchain-web3.
- Design e Criação: edicao-de-video, filmmaking, fotografia, audio-musica.
- Marketing e Vendas: trafego-pago (documentação oficial Google Ads, Meta, TikTok Ads, LinkedIn), vendas.
- Negócios: contabilidade, juridico, atendimento-suporte, rh-pessoas.
- Ciência e Educação: educacao, saude, psicologia, humanidades.
- Carreira e Ferramentas: acessibilidade, extensoes-navegador, trabalho-remoto-freela.
Reverifique e, se estiverem no ar, inclua estes essenciais que ficaram de fora por limite de verificação: Portal do Simples
Nacional, Receita Federal, LC 182/2021 (Marco Legal das Startups), RD Station Academy, Rock Content, Meio & Mensagem,
Ipea/Ipeadata, Plataforma Lattes, FGV IBRE, Campus Virtual Fiocruz, Coursera Photography Basics, Auphonic, Manual de Redação
da Presidência da República, BBC Learning English, DW Learn German, TV5Monde, r/brdev, LinkedIn Vagas, NotebookLM.
Para sites que não são listas markdown (diretórios em HTML), você pode usar o Scrapling para extrair links com seletores CSS,
desde que os termos do site permitam; registre a fonte e a licença.

## Etapa 4b · Ampliar a IA de cada área
Cada página tem a seção "🤖 IA para <área>" (docs/09). Reforce primeiro as seções menores (social-media, open-source,
biologia, arquitetura-software, produto, gestao-de-projetos, idiomas, osint): essenciais de IA verificados em
data/essenciais.json com "ia": true (ferramentas da profissão, skills/plugins/MCPs para agentes, cursos gratuitos, guias de
prompt, regulação e orientações do conselho profissional) e listas de IA do domínio em data/fontes.json com "ia": true.
Reverifique e inclua se estiverem no ar: documento do MEC "Inteligência Artificial na Educação Básica", orientações do CFC
sobre IA na contabilidade, páginas oficiais da Meta sobre Advantage+, documento técnico da ANPD sobre IA generativa,
orientações da APA sobre IA. Nunca repita ChatGPT/Claude genéricos como essencial de área.

## Etapa 5 · Qualidade das páginas
Abra 10 páginas de área ao acaso e confira: nomes estranhos (restos de HTML, URLs como nome), descrições cortadas, tópicos
sem sentido para a área (use `excluir_topicos` em data/fontes.json), seções gigantes. Corrija na origem (regras em
scripts/selecionar.py, fonte trocada em data/fontes.json), nunca na página gerada.

## Etapa 6 · Opcional: traduzir descrições para pt-BR
Em blocos por área, traduza as descrições em inglês para pt-BR num arquivo data/traducoes.json ({url: descricao_pt}) e faça
o gerador preferir a tradução. Só traduza descrições de fontes com licença que permite adaptação (CC0, CC-BY, CC-BY-SA, MIT).

## Etapa 7 · Publicar (só depois da minha confirmação)
Revise o README, defina o nome final em data/config.json (nome e "dono/repo"), regenere, valide e me mostre o resumo:
total de links, URLs únicas, links quebrados removidos, fontes novas, essenciais novos. Depois de eu dizer "pode publicar":
crie o repositório (gh repo create) e faça o push.

## Opcional · Rodar em paralelo no Maestri
Se estiver no Maestri: um Maestro (Fable) coordena; recrute um executor (Sonnet) por setor da Etapa 4, cada um mexendo só
nas áreas do seu setor em data/essenciais.json e data/fontes.json por meio de arquivos parciais data/parcial-<setor>.json;
o Maestro junta os parciais, roda o pipeline e o validador, e faz um commit por setor.
```
