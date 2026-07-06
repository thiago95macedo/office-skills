---
name: faq-corporativo
description: Use para construir FAQ interno ou externo, com perguntas claras, respostas precisas e referência a responsável.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - suporte/faq-tecnico
  - atendimento/triagem-mensagens
version: 0.1.0
status: rascunho
---

# FAQ Corporativo

## Objetivo
Organizar perguntas frequentes com respostas consistentes e responsáveis.

## Entradas
- `perguntas_respostas` (lista)
- `audiencia` (enum)
- `tema` (string)

## Saída
FAQ agrupado por tema, com referência a responsável quando aplicável.

## Boas práticas
- Linguagem clara.
- Evidência técnica quando relevante.