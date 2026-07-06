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