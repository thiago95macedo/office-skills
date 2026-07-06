---
name: plano-acao
description: Use para estruturar plano de ação com responsáveis, prazos, entregas e indicadores.
category: gestao
priority: essencial
depends_on: []
composes_with:
  - gestao/matriz-5w2h
  - gestao/cronograma-projeto
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Plano de Ação

## Objetivo
Estruturar plano com ações, responsáveis, prazos, entregas e indicadores de sucesso.

## Entradas
- `objetivo` (string)
- `acoes` (lista)
- `responsaveis` (lista)
- `prazos` (lista)
- `indicadores` (lista)

## Saída
Tabela com colunas: Ação | Responsável | Prazo | Entrega | Indicador.

## Boas práticas
- Ações verificáveis.
- Prazo específico.
- Responsável nominal.