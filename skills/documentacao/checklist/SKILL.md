---
name: checklist
description: Use para criar listas de verificação aplicáveis a rotinas críticas (auditoria, manutenção, onboarding, fechamento mensal).
category: documentacao
priority: essencial
depends_on: []
composes_with:
  - documentacao/pop-sop
  - gestao/plano-acao
version: 0.1.0
status: rascunho
---

# Checklist

## Objetivo
Criar listas de verificação operacionais, com itens objetivos, agrupados por categoria, marcando ponto crítico quando aplicável.

## Entradas
- `finalidade` (string)
- `itens` (lista)
- `agrupamento` (dict, opcional)

## Saída
Checklist Markdown com checkboxes, categorias e campo de responsável.

## Boas práticas
- Itens curtos e verificáveis.
- Ordem lógica.
- Itens críticos destacados.