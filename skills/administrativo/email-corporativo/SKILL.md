---
name: email-corporativo
description: Use para redigir e-mails profissionais (externos ou internos) com tom, estrutura e tamanho adequados.
category: administrativo
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/comunicado-interno
  - comercial/follow-up
version: 0.1.0
status: rascunho
---

# E-mail Corporativo

## Objetivo
Produzir e-mails profissionais com assunto claro, abertura cordial, conteúdo objetivo e CTA.

## Entradas
- `destinatario` (string)
- `assunto` (string)
- `mensagem_central` (string)
- `tom` (enum)
- `anexos` (lista, opcional)

## Saída
E-mail pronto em Markdown, com assunto e assinatura.

## Boas práticas
- Assunto com ≤ 8 palavras.
- Corpo com até 3 parágrafos principais.
- CTA explícito.