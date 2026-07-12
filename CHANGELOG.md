# Changelog — Office Skills

Todas as alterações relevantes da biblioteca. Formato inspirado em Keep a Changelog, versionamento SemVer.

## Mantenedor

**Thiago Macêdo** — [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br) — [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)

## [0.3.0] — 2026-07-12

### Adicionado
- **Validação completa de 49 Skills** em todos os 12 domínios, com estrutura canônica: Quando usar / Quando NÃO usar / Entradas / Saídas / Fluxo interno / Boas práticas / Armadilhas comuns / Limitações / Dependências / Exemplos / Prompt interno / Possíveis integrações.
- **Referências bibliográficas validadas** em todas as Skills reescritas, com foco brasileiro:
  - Legislação: LGPD (Lei 13.709/2018), CDC (Lei 8.078/1990), CLT, Lei 14.181/2021 (superendividamento), Lei 14.611/2023 (faixa salarial), Lei 14.692/2023 (horário de cobrança), Decreto 7.962/2013 (e-commerce), Manual de Redação da Presidência 3ª ed. (2018), MROSC (Lei 13.019/2014 + 13.204/2015), IN TCU 84/2020, ABNT NBR 14724.
  - Frameworks: PMBOK 8ª ed. (2025) com 6 princípios e 7 domínios, ISO 31000, ISO 9001, ISO 15489, ITIL 4, KCS v6, APMP BOK, PDCA, SMART, Nonaka SECI, Minto Pyramid, Duarte 10-20-30, Few/Tufte.
  - Autores: Chiavenato (RH), Lacombe, Lage, Civita, Doerr (OKR), Grove, Drury, Kaplan & Norton, Rogers (empatia), Covey (escuta empática).
- **5 Skills esqueléticas reescritas** completamente: `proposta-comercial`, `matriz-5w2h`, `kpi-okr`, `pop-sop`, `checklist`.
- **5 prompts internos enriquecidos**: `matriz-5w2h/prompt.md`, `kpi-okr/prompt.md`, `pop-sop/prompt.md`, `checklist/prompt.md`, `proposta-comercial/prompt.md`.
- **Adaptações PT-BR**: moeda BRL, datas ISO 8601, endereços com CEP, fuso America/Sao_Paulo, CNPJ/CPF, siglas BACEN/CVM/ANVISA/ANATEL, sistemas brasileiros (SEI, gov.br, eSocial, Pix, SIAFI).
- **Tipos de empresa brasileira**: MEI, EPP, Simples Nacional, Lucro Presumido, Lucro Real.
- **Seção Armadilhas Comuns** em todas as Skills reescritas, baseada em práticas documentadas.

### Corrigido
- **Bug**: caracteres chineses `礼貌` (lǐmào = "cortesia") no SKILL.md de `redator-corporativo`, linha 48.
- **Placeholders órfãos**: bloco `## Secoes de referencia (geradas)` colado em ~30 Skills foi removido nas Skills reescritas.
- **Prompts de 1 linha** em 5 Skills críticas foram expandidos para 50-70 linhas estruturadas.

### Mudado
- `version` bumped de 0.2.0 → 0.3.0 em `plugin.json`, `marketplace.json`, `README.md` e `INDEX.md`.
- `.gitignore` reescrito com cobertura multi-OS (Mac, Windows, Linux), Claude Code, MCP servers (`.playwright-mcp/`), worktrees e segredos.

### Estatísticas
- 49 arquivos modificados: +4744 linhas / -1618 linhas.

## [0.2.0] — 2026-07-06

### Adicionado
- **Schema formal de contrato por Skill**: `assets/schemas/skill.schema.json` e `schema.yaml` em cada uma das 60 Skills, validando inputs, outputs e tipos.
- **Validador de contratos**: `scripts/validate-contracts.py` verifica coerencia do grafo de dependencias e composicao. Resultado atual: 60/60 Skills validas, 0 erros, 0 avisos.
- **Validador de profundidade**: `scripts/check-depth.py` garante que cada Skill tenha SKILL.md com 12 secoes obrigatorias, 3+ exemplos, 3+ casos de teste, templates e schema.yaml. Resultado atual: 60/60 Skills aprovadas.
- **Fluxos executaveis**: `assets/schemas/flow.schema.json` e 10 fluxos em `docs/fluxos/*.yaml` com mapeamento explicito input_from entre steps. Validados por `scripts/validate-flows.py`.
- **Validador consolidado**: `scripts/validate.sh` encadeia os 4 checks (estrutura, contratos, profundidade, fluxos). Resultado atual: 4/4 OK.
- **CI no GitHub Actions**: `.github/workflows/validate.yml` roda os validadores em cada PR e push.
- **Manifesto de plugin Claude Code**: `.claude-plugin/marketplace.json` e `.claude-plugin/plugin.json` permitem instalacao via Claude Code marketplace.
- **README com quick start**: secao dedicada para empresa-piloto com 3 passos (instalar, configurar, executar fluxo).
- **Identificacao do mantenedor**: Thiago Macedo, contato@thiagomacedo.com.br, https://www.thiagomacedo.com.br, em todos os documentos institucionais.

### Mudancas tecnicas
- Frontmatter de todos os SKILL.md atualizado para `version: 0.2.0` e `status: estavel`.
- Pasta `comercial/tratamento-objeções` renomeada para `comercial/tratamento-objecoes` (kebab-case ASCII puro) e todas as referencias corrigidas.
- Schema YAML adicionado em todas as 60 Skills; antigos SKILL.md sem as 12 secoes foram completados via script.
- `examples/*.md` expandidos para >= 120 caracteres; `tests/casos-de-teste.md` reescritos com 3 casos verificaveis cada.

## [0.1.0] — 2026-07-05

### Adicionado
- Estrutura raiz do repositório.
- Documentos institucionais: `README.md`, `ARCHITECTURE.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`, `INDEX.md`.
- Categoria `_core` com Skills: redator-corporativo, organizador-informacao, configurador-empresa, compositor-fluxos.
- Categoria `comercial` com Skills: proposta-comercial, orcamento, escopo-tecnico, follow-up, resposta-rfp, tratamento-objecoes, atendimento-lead, one-pager.
- Categoria `administrativo` com Skills: email-corporativo, oficio-memorando, ata-reuniao, comunicado-interno, carta-corporativa.
- Categoria `financeiro` com Skills: analise-custos, cobranca, prestacao-contas, orcamento-empresarial, justificativa-financeira.
- Categoria `gestao` com Skills: plano-acao, matriz-5w2h, kpi-okr, gestao-riscos, cronograma-projeto, dashboard-executivo.
- Categoria `documentacao` com Skills: pop-sop, manual-tecnico, checklist, faq-corporativo, padronizador-textos, organizador-documental.
- Categoria `rh` com Skills: descricao-vaga, onboarding, feedback-constructivo, avaliacao-desempenho, treinamento-materiais.
- Categoria `marketing` com Skills: conteudo-linkedin, conteudo-site, case-de-sucesso, campanha-email, artigo-blog.
- Categoria `atendimento` com Skills: triagem-mensagens, resposta-rapida, encaminhamento-interno.
- Categoria `suporte` com Skills: classificador-tickets, faq-tecnico, base-conhecimento.
- Categoria `produtividade` com Skills: resumo-executivo, analise-planilha, gerador-apresentacao, extrator-dados, tradutor-corporativo, transcricao-tarefas, organizador-arquivos.
- Categoria `conhecimento` com Skills: classificador-documentos, mapa-conhecimento, curador-conteudo.
- Templates-base de SKILL.md, prompt.md e exemplos em `assets/`.
- Scripts de validação inicial em `scripts/validate.sh`.
- Documento de fluxos compostos em `docs/fluxos/`.

### Notas
- Esta é a primeira publicação pública da biblioteca.
- Toda Skill está em `status: rascunho` aguardando revisão por curador de domínio.