---
name: gestao-riscos
description: Use para identificar, classificar e tratar riscos em projeto ou operação.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/plano-acao
  - gestao/cronograma-projeto
version: 0.1.0
status: rascunho
---

# Gestão de Riscos

## Objetivo
Identificar riscos, classificá-los por probabilidade e impacto, propor mitigação.

## Entradas
- `contexto` (string)
- `riscos_iniciais` (lista, opcional)

## Saída
Matriz de riscos com probabilidade, impacto, mitigação, responsável.

## Boas práticas
- Linguagem direta.
- Mitigação prática.