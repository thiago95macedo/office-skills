---
name: cronograma-projeto
description: Use para montar cronogramas com fases, marcos, atividades, dependências e caminho crítico.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/plano-acao
  - gestao/gestao-riscos
  - gestao/matriz-5w2h
version: 0.2.0
status: estavel
references:
  - PMI. PMBOK Guide. 8. ed. 2025 (Planning + Schedule Performance Domains).
  - PMI. Practice Standard for Scheduling. 2011.
  - Kerzner, H. Project Management: A Systems Approach. 2021.
  - PRINCE2 (AXELOS/PeopleCert) — Practice of Plans.
---

# Cronograma de Projeto

## Objetivo
Construir cronograma detalhado com fases, atividades, marcos, dependências, recursos e caminho crítico, conforme práticas reconhecidas de gestão de projetos.

## Quando usar
- Projeto com duração > 2 semanas ou múltiplas atividades.
- Planejamento de evento, lançamento, campanha.
- Coordenação entre múltiplas equipes.
- Repactuação de prazos durante execução.
- Apresentação de plano para sponsor.

## Quando NÃO usar
- Para iniciativa trivial (usar `plano-acao` ou `matriz-5w2h`).
- Para roadmap plurianual sem atividades definidas (usar OKR + roadmap estratégico).
- Para fluxo operacional recorrente (usar POP ou checklist).

## Conceitos fundamentais

| Conceito | Definição |
|---------|-----------|
| **Atividade** | Unidade de trabalho com início, fim e duração |
| **Marco** (milestone) | Ponto significativo sem duração (entrega, aprovação, evento) |
| **Dependência** | Relação entre atividades (FS, FF, SS, SF) |
| **Caminho crítico** | Sequência mais longa de atividades dependentes — define duração mínima |
| **Folga (float)** | Tempo que uma atividade pode atrasar sem afetar o projeto |
| **Recurso** | Pessoa, equipamento ou material alocado |
| **Restrição** | Data imposta (ex: lançamento externo) |

## Tipos de dependência

| Tipo | Significado | Exemplo |
|------|-------------|---------|
| **FS** (Finish-to-Start) | Sucessora começa quando predecessora termina | Atividade B começa após A terminar |
| **SS** (Start-to-Start) | Sucessora começa quando predecessora começa | Modelagem e implementação em paralelo |
| **FF** (Finish-to-Finish) | Sucessora termina quando predecessora termina | Revisão termina quando escrita termina |
| **SF** (Start-to-Finish) | Sucessora termina quando predecessora começa | (raro) |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Projeto, data emissão, versão, responsável |
| 2 | **Resumo** | Início, fim, duração total, nº de marcos |
| 3 | **Fases** | Grandes blocos do projeto |
| 4 | **Marcos principais** | Entregas e eventos significativos |
| 5 | **Atividades** | Lista detalhada com duração, dependência, responsável |
| 6 | **Caminho crítico** | Sequência que define duração |
| 7 | **Recursos** | Pessoas, sistemas, materiais |
| 8 | **Riscos de prazo** | Atividades com maior risco de atraso |
| 9 | **Aprovações** | Sponsor, gerente, equipe |

## Ferramentas de visualização

| Ferramenta | Quando usar |
|------------|-------------|
| **Gantt** | Visão completa, dependências, recurso (mais comum) |
| **PERT/CPM** | Análise de caminho crítico, três estimativas (otimista, provável, pessimista) |
| **Diagrama de rede** | Lógica de dependências |
| **Roadmap** | Visão plurianual, baixa granularidade |
| **Kanban (sprints)** | Execução iterativa (ágeis) |
| **Burndown/Burnup** | Visualização de progresso vs. escopo |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `nome_projeto` | string | sim | Nome do projeto |
| `data_inicio` | data | sim | ISO 8601 — data de início |
| `data_fim_desejada` | data | não | Data alvo (pode ser vinculante ou indicativa) |
| `fases` | lista | sim | Fases em ordem |
| `atividades` | lista | sim | Atividades com duração e dependência |
| `marcos` | lista | sim | Marcos com data ou condição |
| `responsaveis` | lista | sim | Equipe |
| `recursos` | dict | não | Pessoas e materiais alocados |
| `restricoes` | lista | não | Datas impostas (lançamento, regulatório) |

## Saídas esperadas
- Cabeçalho com metadados.
- Resumo executivo (início, fim, duração, marcos).
- Lista de fases com período.
- Tabela de atividades com duração, dependência, responsável.
- Lista de marcos com data.
- Caminho crítico identificado.
- Riscos de prazo sinalizados.
- Sugestão de representação visual (Gantt textual, tabela).

## Fluxo interno
1. Receber dados do projeto (nome, data início, fim desejada).
2. Decompor em fases e atividades (Work Breakdown Structure — WBS).
3. Estimar duração de cada atividade (em horas, dias ou semanas).
4. Definir dependências (FS, SS, FF, SF).
5. Identificar marcos com data ou condição gatilho.
6. Calcular caminho crítico (sequência mais longa).
7. Validar data fim vs. data desejada.
8. Atribuir responsáveis a cada atividade.
9. Sinalizar restrições (datas impostas).
10. Sugerir representação visual (Gantt textual ou tabela).
11. Identificar atividades com maior risco de prazo.

## Boas práticas
- **Granularidade suficiente** para gerenciar (sem micro-atividades).
- **Duração estimada** com três pontos (otimista, provável, pessimista) quando crítico.
- **Dependências explícitas** — evitar "começa quando possível".
- **Folga calculada** — slack/float em atividades não-críticas.
- **Recurso alocado** — quem faz cada atividade.
- **Buffer de projeto** — reserva de 10-20% no final.
- **Revisão periódica** — semanal em projeto ativo.
- **Marcos visíveis** — datas comemorativas e entregas.
- **Restrições sinalizadas** — datas impostas com motivo.
- **Atualização contínua** — cronograma é vivo, não documento estático.

## Limitações
- Não substitui execução real — cronograma é planejamento.
- Não calcula automaticamente caminho crítico (estimativa).
- Não modela restrições de recurso avançadas (leveling manual).
- Não substitui ferramentas de gestão (MS Project, Primavera, Asana).

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Cronograma de evento pontual
- `02-intermediario.md` — Cronograma de projeto de 3 meses
- `03-avancado.md` — Cronograma com múltiplas equipes e dependências

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- MS Project / Project Online
- Asana, Monday, Trello, Jira
- Smartsheet, Wrike, ClickUp
- Notion / Confluence (para publicação)
- Power BI / Tableau (para dashboards de progresso)