---
name: comunicado-interno
description: Use para comunicar mudanças, decisões ou fatos relevantes para colaboradores internos.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
version: 0.1.0
status: rascunho
---

# Comunicado Interno

## Objetivo
Informar mudanças ou fatos relevantes à empresa de forma clara, uniforme e rastreável.

## Entradas
- `publico` (string)
- `mensagem_central` (string)
- `tom` (enum)
- `canal` (enum: mural | email | intranet)

## Saída
Comunicado em Markdown pronto para distribuição.

## Boas práticas
- Mensagem única por comunicado.
- O que muda e o que não muda.
- Próximos passos.