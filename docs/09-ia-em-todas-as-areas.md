# 09 · IA em todas as áreas

> Como a camada de inteligência artificial do guia é montada, o que você encontra em cada seção 🤖 e como usar IA no trabalho com responsabilidade.

[🏠 Início](../README.md) · [🤖 IA para todas as áreas](../ia/README.md)

## O que tem em cada seção 🤖

Toda página de área tem uma seção **🤖 IA para <área>**, logo depois de "⭐ Comece por aqui":

- **Essenciais de IA:** de 8 a 15 links escolhidos a dedo, com descrição em português: ferramentas de IA daquela profissão, skills, plugins e servidores MCP para agentes (Claude, ChatGPT, Codex, Gemini), cursos gratuitos, guias de prompt, regulação e páginas de uso responsável do conselho ou órgão da área quando existem.
- **Mais ferramentas e recursos de IA:** até 30 links coletados de três origens:
  1. listas curadas de IA específicas do domínio (ex.: IA para finanças, IA jurídica, geração de vídeo, IA para pesquisa), marcadas com `"ia": true` em `data/fontes.json`;
  2. listas gerais de ferramentas de IA, cujas categorias são distribuídas pelas áreas (vídeo → Edição de Vídeo, música e voz → Áudio, SEO → SEO, marketing → Marketing Digital...), configuradas em `data/fontes-guias.json`;
  3. itens das próprias listas da área que falam de IA (detectados por termos como *AI*, *LLM*, *GPT*, *machine learning*, *inteligência artificial*).

As áreas *IA Generativa e LLMs* e *Ferramentas de IA* já são inteiras sobre IA; nelas a seção 🤖 traz só o "por onde começar".

## Como usar IA com responsabilidade

- **Dados sensíveis:** não cole dados pessoais, de clientes, de pacientes ou segredos da empresa em ferramentas que usam o conteúdo para treinar modelos. Veja os termos de cada ferramenta e prefira planos corporativos ou modelos locais (Ollama, Open WebUI) quando o dado é sensível. No Brasil, a LGPD vale também para o que você envia a uma IA.
- **Confira sempre:** modelos de linguagem erram com confiança. Fonte, número, citação jurídica, dose de medicamento e código precisam ser verificados por você.
- **Regras da profissão:** vários conselhos e órgãos já publicaram orientações sobre IA (saúde, direito, psicologia, contabilidade, educação). Quando existem e foram verificadas, estão na seção 🤖 da área.
- **Direitos autorais e transparência:** em criação (imagem, vídeo, música, texto), siga as regras das plataformas sobre conteúdo gerado por IA e respeite os direitos de quem criou o material de referência.
- **Agentes e automações:** dê ao agente só as permissões necessárias e mantenha aprovação humana antes de ações irreversíveis (enviar, publicar, pagar, apagar).

## Como contribuir com a camada de IA

- Essencial de IA novo: em `data/essenciais.json`, com `"ia": true` e a área.
- Lista de IA de um domínio: em `data/fontes.json`, com `"ia": true`.
- Categoria nova de uma lista geral de IA: ajuste o `mapa` da fonte em `data/fontes-guias.json`.
- Depois: `python3 scripts/coletar.py && python3 scripts/selecionar.py && python3 scripts/gerar.py && python3 tests/validar.py`.
