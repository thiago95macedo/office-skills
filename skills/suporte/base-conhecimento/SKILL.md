---
name: base-conhecimento
description: Use para organizar e manter base de conhecimento interna com taxonomia, donos, ciclo de revisão e governança KCS.
category: suporte
priority: opcional
depends_on: []
composes_with:
  - suporte/faq-tecnico
  - conhecimento/mapa-conhecimento
  - conhecimento/curador-conteudo
version: 0.2.0
status: estavel
references:
  - KCS® v6 Practices Guide — Consortium for Service Innovation (operada por HDI/Informa TechTarget no Brasil).
  - Dalkir, K. Knowledge Management in Theory and Practice. 4. ed. 2023.
  - Nonaka, I.; Takeuchi, H. The Knowledge-Creating Company. 1995 (modelo SECI).
  - APQC — American Productivity & Quality Center (Knowledge Management frameworks).
---

# Base de Conhecimento

## Objetivo
Estruturar base de conhecimento interna com taxonomia, donos por categoria, ciclo de revisão periódico e governança, segundo práticas KCS (Knowledge-Centered Service).

## Quando usar
- Organização inicial de KB dispersa.
- Revisão periódica da base existente.
- Auditoria de qualidade e atualização.
- Onboarding de equipe na estrutura.
- Migração entre plataformas.

## Quando NÃO usar
- Para FAQ específico de produto (usar `suporte/faq-tecnico`).
- Para mapeamento amplo de conhecimento organizacional (usar `conhecimento/mapa-conhecimento`).

## Princípios KCS (Knowledge-Centered Service)

| Princípio | Aplicação |
|-----------|-----------|
| **Abundance** | Mais conteúdo é melhor — qualidade vem com uso |
| **Create Value from Demand** | Artigos nascem da demanda real (não da especulação) |
| **Collect, Don't Store** | Conhecimento emerge do fluxo de trabalho |
| **Improve as We Use** | Cada uso é oportunidade de melhoria |
| **Solve Loop** | Capturar no momento da resolução |
| **Evolve Loop** | Melhorar continuamente |

## Estrutura recomendada

| Componente | Conteúdo |
|------------|----------|
| **Taxonomia** | Áreas funcionais, tipos de artigo, níveis |
| **Categorias** | Agrupamento por tema/produto |
| **Donos** | Responsáveis por categoria |
| **Ciclo de revisão** | Frequência e critério |
| **Qualidade** | Padrão mínimo (formato, completude, links) |
| **Métricas** | Uso, satisfação, contribuição |
| **Workflow** | Criação, aprovação, publicação, retirada |

## Tipos de artigo em KB

| Tipo | Finalidade | Tamanho típico |
|------|-----------|----------------|
| **Solução** | Resposta a problema recorrente | 300-800 palavras |
| **Procedimento** | Passo a passo para tarefa | 500-1500 palavras |
| **Referência** | Informação técnica ou de processo | Variável |
| **FAQ** | Perguntas e respostas agrupadas | Variável |
| **Política** | Regra de negócio ou compliance | Variável |
| **Runbook** | Operação técnica crítica | Variável |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `conteudo_atual` | lista | sim | Artigos existentes |
| `categoria` | dict | sim | Estrutura atual ou proposta |
| `dono` | dict | sim | Responsáveis por área |
| `ciclo_revisao` | string | sim | Frequência de revisão (mensal, trimestral) |
| `criterio_atualizacao` | enum | sim | por-uso / por-tempo / por-evento |
| `ferramenta` | enum | sim | Confluence / Notion / SharePoint / Document360 |
| `objetivo` | string | sim | Finalidade (auditoria, migração, organização) |

## Saídas esperadas
- Taxonomia proposta (ou ajustes na existente).
- Lista de donos por categoria.
- Calendário de revisões (próximos 6 meses).
- Lista de artigos vencidos e a vencer.
- Relatório de qualidade por categoria.
- Recomendações de melhoria.

## Fluxo interno
1. Carregar `config/empresa.yaml` (ferramenta, áreas, donos).
2. Receber conteúdo atual e objetivo.
3. Mapear taxonomia atual vs. proposta.
4. Identificar artigos por tipo, categoria, dono.
5. Identificar artigos vencidos (última revisão > ciclo definido).
6. Listar artigos a vencer (próximos 30/60/90 dias).
7. Avaliar qualidade (formato, completude, links, métricas de uso).
8. Recomendar melhorias.
9. Propor calendário de revisão.

## Boas práticas (KCS + Dalkir)
- **Solve Loop no momento** — capturar durante resolução (não após).
- **Evolve Loop contínuo** — cada uso é oportunidade de melhoria.
- **Donos por categoria** — não centralizar.
- **Ciclo de revisão por uso** — artigos mais usados = revisões mais frequentes.
- **Ciclo por tempo** — categorias inteiras a cada X meses.
- **Qualidade mínima** — template padrão + checklist.
- **Links entre artigos** — topologia de conhecimento.
- **Métricas de uso** — identificar artigos obsoletos (sem uso = obsoleto).
- **Contribuição coletiva** — todos podem sugerir, donos aprovam.
- **Versionamento** — histórico de mudanças.
- **LGPD** — não registrar dados pessoais em KB.

## Armadilhas comuns
- Sem donos — ninguém mantém.
- Sem ciclo de revisão — base defasa.
- Sem padrão de qualidade — formato inconsistente.
- Captura tardia (depois da resolução, perde contexto).
- KB como "depósito de PDFs" — sem escaneabilidade.
- Sem métricas de uso — impossível priorizar.
- Sem links entre artigos — conteúdo isolado.
- Dados sensíveis na KB (viola LGPD).

## Limitações
- Não mede uso real sem integração com a ferramenta.
- Não acessa conteúdo de outras ferramentas automaticamente.
- Não realiza busca semântica.
- Não sugere conteúdo relacionado automaticamente.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Auditoria inicial de KB dispersa
- `02-intermediario.md` — Reorganização com taxonomia
- `03-avancado.md` — Migração entre plataformas

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Ferramentas de KB (Confluence, Notion, Document360, Guru)
- ITSM (Zendesk, Jira Service Management, Movidesk)
- Sistemas de busca (Algolia, Elasticsearch)
- Analytics de uso (Mixpanel, Amplitude)