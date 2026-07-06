---
name: kpi-okr
description: Use para definir KPIs e OKRs em área ou projeto.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/dashboard-executivo
  - gestao/plano-acao
version: 0.1.0
status: rascunho
---

# KPI / OKR

## Objetivo
Definir KPIs operacionais e OKRs estratégicos de forma mensurável.

## Entradas
- `objetivo_estrategico` (string)
- `metas_trimestrais` (lista)
- `indicadores` (lista)

## Saída
KPIs (com fórmula, meta, frequência) e OKRs (objetivo + KRs).

## Boas práticas
- KRs mensuráveis.
- Frequência clara.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para definir KPIs e OKRs em área ou projeto.

## Quando usar

Listar situacoes em que a Skill e a ferramenta correta.

## Quando NÃO usar

Listar situacoes em que outra Skill ou processo deve ser usado.

## Entradas esperadas

Documentar campos, tipos e obrigatoriedade.

## Saídas esperadas

Documentar artefatos produzidos pela Skill.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Limitações

Declarar restricoes conhecidas da Skill.

## Dependências

Apontar Skills que esta Skill depende.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

## Possíveis integrações

Listar integracoes com sistemas externos.

