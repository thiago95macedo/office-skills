---
name: escopo-tecnico
description: Use para descrever serviços com clareza técnica — atividades, entregas, premissas, exclusões, responsabilidades.
category: comercial
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - comercial/orcamento
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# Escopo Técnico

## Objetivo
Documentar o escopo de um serviço com linguagem técnica clara, evitando ambiguidades contratuais.

## Quando usar
- Antes de elaborar orçamento.
- Em propostas técnicas.
- Em contratação de fornecedores.

## Entradas
- `servico` (descrição resumida)
- `atividades` (lista)
- `entregas` (lista)
- `premissas` (lista)
- `exclusoes` (lista)
- `responsabilidades_cliente` (lista)

## Saída
Documento Markdown estruturado com seções nomeadas.

## Boas práticas
- Use verbos no infinitivo nas atividades.
- Liste exclusões explicitamente.
- Declare premissas que afetam o serviço.