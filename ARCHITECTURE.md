# Arquitetura — Office Skills

Este documento registra as decisões arquiteturais (ADRs) da biblioteca Office Skills. Cada decisão tem identificação, contexto, consequência e trade-offs.

## Contato do mantenedor

**Thiago Macêdo** — [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br) — [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)

## ADR-001 — Skills como unidades mínimas

**Decisão:** Cada Skill é a menor unidade funcional. Não existem sub-Skills públicas.

**Consequência:** Uma Skill grande demais deve ser quebrada em duas ou três. Uma Skill trivialmente pequena deve ser fundida com uma vizinha.

**Trade-off:** Resistência à tentação de criar Skills "faz-tudo".

## ADR-002 — Categorização por domínio de negócio

**Decisão:** Organização em 12 domínios (`_core`, `comercial`, `administrativo`, `financeiro`, `gestao`, `documentacao`, `rh`, `marketing`, `atendimento`, `suporte`, `produtividade`, `conhecimento`).

**Consequência:** Uma Skill pertence a um único domínio. Quando cruzar fronteiras, registrar as dependências cruzadas no SKILL.md.

**Trade-off:** Domínios podem crescer de forma desigual; revisões periódicas devem rebalancear.

## ADR-003 — Estrutura fixa de arquivos por Skill

**Decisão:** Toda Skill tem SKILL.md, README.md, prompt.md, examples/, templates/, tests/.

**Consequência:** Padronização total. Ferramentas de validação podem assumir a estrutura.

**Trade-off:** Skills muito simples carregam overhead de pastas vazias; aceitamos o overhead em troca de uniformidade.

## ADR-004 — Frontmatter padronizado

**Decisão:** Toda Skill abre com frontmatter YAML contendo `name`, `description`, `category`, `priority`, `depends_on`, `composes_with`, `version`, `status`.

**Consequência:** O catálogo pode ser gerado automaticamente por scripts.

**Trade-off:** Exige disciplina para manter o frontmatter atualizado.

## ADR-005 — Configuração por contexto, não por código

**Decisão:** Personalização por empresa é feita por arquivo de configuração externo (`config/empresa.yaml`) e variáveis passadas no momento de invocação. Nunca se duplica uma Skill para uma empresa.

**Consequência:** Mesma Skill atende múltiplas empresas; estilo, vocabulário e premissas mudam via configuração.

**Trade-off:** Configuração adicional é necessária; o ganho de escalabilidade compensa.

## ADR-006 — Composição por contratos

**Decisão:** Skills se compõem por contratos explícitos (entradas e saídas documentadas em `templates/`). Não há encadeamento implícito.

**Consequência:** Fluxos compostos são transparentes, reproduzíveis e versionáveis.

**Trade-off:** Exige documentação rigorosa dos contratos.

## ADR-007 — Independência de fornecedor

**Decisão:** Skills não devem depender de um fornecedor específico de IA, framework ou ferramenta. Onde houver dependência, ela deve ser isolada em uma Skill adaptadora específica.

**Consequência:** A biblioteca roda em Claude, GPT, Gemini, modelos locais e ferramentas correlatas.

**Trade-off:** Cuidado para não introduzir acoplamento acidental em exemplos.

## ADR-008 — Testes como cenários de pressão

**Decisão:** Cada Skill deve ter pelo menos três casos de teste em `tests/casos-de-teste.md`, descrevendo cenários realistas que comprovam que o agente cumpre o que promete.

**Consequência:** Skill sem teste é considerada incompleta.

**Trade-off:** Aumento de esforço inicial.

## ADR-009 — Versionamento semântico por Skill

**Decisão:** Cada Skill tem versão própria (SemVer). A biblioteca tem versão agregada em `CHANGELOG.md`.

**Consequência:** Mudanças incompatíveis em uma Skill não quebram outras.

**Trade-off:** Necessidade de disciplina de versionamento.

## ADR-010 — Catálogo navegável + busca textual

**Decisão:** `INDEX.md` é a fonte de verdade navegável; `scripts/build-index.js` regenera o índice a partir dos SKILL.md.

**Consequência:** O índice nunca fica desatualizado se a fonte estiver correta.

**Trade-off:** Toda Skill nova precisa ser commitada para aparecer.

## Mapa de dependências entre Skills

```
core/redator-corporativo ──┬──> comercial/proposta-comercial
                          ├──> comercial/orcamento
                          ├──> administrativo/email-corporativo
                          ├──> documentacao/pop-sop
                          └──> marketing/conteudo-institucional

core/organizador-informacao ──┬──> gestao/ata-reuniao
                              ├──> produtividade/resumo-executivo
                              └──> suporte/classificador-tickets

produtividade/extrator-dados ────> financeiro/analise-custos
                                ─> gestao/dashboard-kpi

comercial/proposta-comercial ────> comercial/orcamento
                                ─> comercial/tratamento-objecoes
```

## Roadmap arquitetural

| Fase | Entrega |
|------|---------|
| 0.1.0 | Catálogo base + Skills core + amostras nos 12 domínios |
| 0.2.0 | Scripts de validação, indexação e lint |
| 0.3.0 | Configuração por empresa (`config/empresa.example.yaml`) |
| 0.4.0 | Adaptadores para Claude Code, Codex, Gemini CLI |
| 1.0.0 | Cobertura completa dos 12 domínios; testes verdes |