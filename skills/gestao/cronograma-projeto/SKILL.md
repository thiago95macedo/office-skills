---
name: cronograma-projeto
description: Use para montar cronogramas com marcos e dependências.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/plano-acao
  - gestao/gestao-riscos
version: 0.1.0
status: rascunho
---

# Cronograma de Projeto

## Objetivo
Construir cronograma com fases, marcos e dependências.

## Entradas
- `fases` (lista)
- `marcos` (lista)
- `dependencias` (lista)

## Saída
Tabela ou diagrama textual com fases, início, fim, marcos.

## Boas práticas
- Marcos datados.
- Dependências explícitas.