---
name: dashboard-executivo
description: Use para consolidar indicadores em resumo executivo de uma página.
category: gestao
priority: opcional
depends_on:
  - gestao/kpi-okr
  - produtividade/resumo-executivo
composes_with:
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Dashboard Executivo

## Objetivo
Resumir indicadores-chave em formato escaneável para a diretoria.

## Entradas
- `indicadores` (lista)
- `periodo` (string)

## Saída
Tabela resumo + destaques + alertas.

## Boas práticas
- Linguagem executiva.
- Destaques com variação.