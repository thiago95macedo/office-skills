---
name: plano-acao
description: Use para estruturar plano de ação com responsáveis, prazos, entregas e indicadores de sucesso.
category: gestao
priority: essencial
depends_on: []
composes_with:
  - gestao/matriz-5w2h
  - gestao/cronograma-projeto
  - gestao/kpi-okr
  - gestao/gestao-riscos
version: 0.2.0
status: estavel
references:
  - PDCA (Plan-Do-Check-Act) — Shewhart 1939 / Deming 1950.
  - SMART — Doran 1981 (Management Review).
  - PMI. PMBOK Guide. 8. ed. 2025.
  - Drucker, P. The Effective Executive. 1967.
---

# Plano de Ação

## Objetivo
Estruturar plano com ações verificáveis, responsáveis nominais, prazos, entregas e indicadores de sucesso, garantindo rastreabilidade e execução disciplinada.

## Quando usar
- Tradução de objetivo estratégico em tarefas operacionais.
- Plano de projeto com fases e entregas.
- Plano corretivo após desvio ou problema.
- Plano de implementação de iniciativa nova.
- Plano de onboarding de projeto ou área.

## Quando NÃO usar
- Para iniciativa trivial (1-2 ações) (usar lista simples).
- Para framework 5W2H detalhado (usar `matriz-5w2h`).
- Para roadmap plurianual (usar `cronograma-projeto` ou planejamento estratégico).

## Critérios SMART (Doran, 1981)

| Letra | Significado | Pergunta-guia |
|-------|-------------|----------------|
| **S** | Specific (Específico) | O que exatamente será feito? |
| **M** | Measurable (Mensurável) | Como sei que foi feito? |
| **A** | Achievable (Alcançável) | É viável com recursos disponíveis? |
| **R** | Relevant (Relevante) | Contribui para o objetivo? |
| **T** | Time-bound (Temporal) | Quando será feito? |

## Ciclo PDCA (Deming)

| Etapa | Ação | Resultado |
|-------|------|-----------|
| **Plan** (Planejar) | Definir objetivo, ação, indicadores | Plano |
| **Do** (Executar) | Implementar conforme planejado | Execução |
| **Check** (Verificar) | Medir resultados vs. indicadores | Dados |
| **Act** (Agir) | Padronizar, corrigir ou melhorar | Aprendizado |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Objetivo macro, responsável, período |
| 2 | **Contexto** | Por que este plano existe |
| 3 | **Ações** | Lista numerada com verbo no infinitivo |
| 4 | **Responsáveis** | Nome nominal por ação |
| 5 | **Prazos** | Data ISO 8601 ou marco |
| 6 | **Entregas** | Produto verificável de cada ação |
| 7 | **Indicadores** | Como medir sucesso |
| 8 | **Dependências** | Pré-requisitos e bloqueios |
| 9 | **Riscos** | O que pode dar errado |
| 10 | **Acompanhamento** | Frequência e fórum de revisão |
| 11 | **Aprovações** | Sponsor e responsável |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo` | string | sim | Objetivo macro do plano |
| `acoes` | lista | sim | Ações com descrição, responsável, prazo, entrega |
| `responsaveis` | lista | sim | Nomes e papéis |
| `prazos` | dict | sim | Datas ou marcos |
| `indicadores` | lista | sim | Como medir sucesso |
| `contexto` | string | sim | Razão do plano |
| `dependencias` | lista | não | Pré-requisitos |
| `riscos` | lista | não | Riscos identificados |
| `sponsor` | string | sim | Patrocinador do plano |

## Saídas esperadas
- Cabeçalho com objetivo e responsável.
- Contexto do plano.
- Tabela numerada com colunas: ação | responsável | prazo | entrega | indicador.
- Lista de dependências e riscos.
- Cronograma de acompanhamento.
- Aprovações.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom e formato institucional).
2. Receber objetivo e contexto do plano.
3. Decompor objetivo em ações SMART.
4. Para cada ação: verbo no infinitivo, responsável, prazo, entrega, indicador.
5. Identificar dependências entre ações.
6. Identificar riscos e gatilhos.
7. Definir frequência e fórum de acompanhamento.
8. Submeter para aprovação do sponsor.

## Boas práticas
- **Ações verificáveis** (verbo no infinitivo + objeto + critério).
- **Responsável nominal** (nome + papel) — nunca "a equipe".
- **Prazo específico** (data ISO 8601, não "em breve" ou "quando possível").
- **Entrega mensurável** (produto verificável, não "trabalhar em X").
- **Indicador definido** (como saber se foi bem feito).
- **Dependências mapeadas** (bloqueios potenciais).
- **Riscos sinalizados** (com gatilho e contingência).
- **Acompanhamento periódico** (semanal, quinzenal ou mensal).
- **Revisão pós-conclusão** (lições aprendidas).
- **Vinculação ao objetivo macro** (alinhamento estratégico).
- **Escalação clara** (o que fazer se atrasar).

## Limitações
- Não substitui execução disciplinada (plano não é garantia).
- Não cobre mudanças de prioridade durante execução (revisão é necessária).
- Não garante que o objetivo macro seja alcançado (risco existe).
- Não substitui gestão de mudança organizacional.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Plano de ação de iniciativa pontual
- `02-intermediario.md` — Plano corretivo pós-incidente
- `03-avancado.md` — Plano de implantação de programa

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Ferramentas de gestão (Asana, Trello, Jira, Monday)
- Planilhas Google / Excel
- Notion / Confluence
- Dashboards (Power BI, Tableau)