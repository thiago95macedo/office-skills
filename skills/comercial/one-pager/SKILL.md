---
name: one-pager
description: Use para criar resumo executivo de uma página sobre empresa, produto ou serviço.
category: comercial
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-site
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# One-pager

## Objetivo
Sintetizar uma empresa, serviço ou solução em uma única página de alto impacto.

## Entradas
- `assunto` (string)
- `publico` (string)
- `diferenciais` (lista)

## Saída
Markdown de uma página (≤ 500 palavras) com seções objetivas.

## Boas práticas
- Curto, escaneável.
- Foco em valor, não em adjetivos.