---
name: resposta-rfp
description: Use para responder Request for Proposal/Quote formal, mapeando requisitos do edital a respostas técnicas e comerciais.
category: comercial
priority: recomendada
depends_on:
  - comercial/proposta-comercial
  - comercial/escopo-tecnico
  - comercial/orcamento
composes_with:
  - comercial/tratamento-objeções
version: 0.1.0
status: rascunho
---

# Resposta a RFP/RFQ

## Objetivo
Estruturar resposta completa a RFP/RFQ atendendo integralmente aos requisitos do edital, em formato matricial (requisito → resposta).

## Quando usar
- Editais formais com requisitos.
- Compras governamentais.
- Multinacionais com processo estruturado.

## Entradas
- `requisitos_edital` (lista)
- `proposta_tecnica` (dict)
- `proposta_comercial` (dict)
- `documentos_exigidos` (lista)

## Saída
Documento com matriz de atendimento + anexos.

## Boas práticas
- Responder item a item.
- Apontar onde cada requisito é atendido.
- Anexar comprovações.