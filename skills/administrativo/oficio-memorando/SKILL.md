---
name: oficio-memorando
description: Use para produzir ofícios e memorandos internos formais, com numeração, destinatário, assunto, conteúdo e assinatura.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
version: 0.1.0
status: rascunho
---

# Ofício / Memorando

## Objetivo
Padronizar comunicações formais internas com estrutura rígida e auditável.

## Entradas
- `tipo` (enum: oficio | memorando)
- `destinatario` (dict)
- `assunto` (string)
- `conteudo` (string)

## Saída
Documento com numeração, cabeçalho, corpo, local/data, assinatura.

## Boas práticas
- Linguagem impessoal.
- Sem ambiguidade.
- Numeração sequencial quando em série.