---
name: matriz-5w2h
description: Use para aplicar 5W2H (What, Why, Where, When, Who, How, How much) em iniciativa ou projeto.
category: gestao
priority: essencial
depends_on:
  - gestao/plano-acao
composes_with:
  - gestao/cronograma-projeto
  - gestao/plano-acao
version: 0.2.0
status: estavel
references:
  - Origem: indústria automobilística japonesa (Toyota Production System).
  - Chiavenato, I. Introdução à Teoria Geral da Administração. 9. ed.
  - PMI. PMBOK Guide. 7. ed. 2021.
---

# Matriz 5W2H

## Objetivo
Aplicar framework 5W2H (What, Why, Where, When, Who, How, How much) para garantir clareza de planejamento e execução de uma iniciativa, projeto ou ação.

## Quando usar
- Planejamento de iniciativa nova ou ação corretiva.
- Detalhamento de item do `plano-acao`.
- Padronização de comunicação entre áreas sobre uma entrega.
- Apresentação para sponsor que precisa entender escopo em uma página.

## Quando NÃO usar
- Para projetos complexos (usar `cronograma-projeto` ou PMBOK completo).
- Para análise de causa (usar Ishikawa, 5 Porquês).
- Para priorização de backlog (usar WSJF ou RICE).

## As 7 perguntas do framework

| # | Pergunta (EN) | Pergunta (PT) | Resposta visa |
|---|---------------|---------------|----------------|
| 1 | **What** | **O quê** será feito | Entrega, escopo, resultado esperado |
| 2 | **Why** | **Por quê** será feito | Justificativa, problema que resolve |
| 3 | **Where** | **Onde** será feito | Local físico, sistema, área |
| 4 | **When** | **Quando** será feito | Prazo, data, marco |
| 5 | **Who** | **Quem** fará | Responsável nominal, stakeholders |
| 6 | **How** | **Como** será feito | Método, processo, etapas principais |
| 7 | **How much** | **Quanto custará** | Recursos financeiros, humanos, materiais |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `iniciativa` | string | sim | Nome da ação/projeto |
| `contexto` | string | sim | Contexto organizacional relevante |
| `restricoes` | lista | não | Restrições conhecidas |
| `responsaveis_sugeridos` | lista | não | Nomes candidatos a responsável |

## Saídas esperadas
Tabela Markdown com 7 linhas (uma por pergunta) + seção de observações.

## Fluxo interno
1. Receber iniciativa e contexto.
2. Para cada uma das 7 perguntas, redigir resposta concisa (1-2 frases).
3. Validar que cada resposta tem responsável (quando aplicável).
4. Sinalizar premissas que precisam de validação adicional.
5. Encaminhar para `plano-acao` quando detalhamento exigir.

## Boas práticas
- Respostas concisas (1-2 frases cada, máximo).
- Indicadores de data e valor quando aplicáveis (ISO 8601 para datas).
- Responsáveis sempre nominais (não "a equipe").
- Sinalizar premissas com `(a confirmar)` quando necessário.
- Evitar duplicar com plano de ação detalhado (usar 5W2H como sumarização).

## Limitações
- Não substitui plano de projeto formal para iniciativas complexas.
- Não cobre gestão de riscos (complementar com `gestao-riscos`).
- Não cobre comunicação a stakeholders (usar plano de comunicação).

## Dependências
- `gestao/plano-acao` (pode expandir após 5W2H)

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Lançamento de treinamento interno
- `02-intermediario.md` — Migração de sistema
- `03-avancado.md` — Programa plurianual

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Planilhas Google / Excel
- Notion / Confluence
- Ferramentas de gestão (Trello, Asana, Jira)