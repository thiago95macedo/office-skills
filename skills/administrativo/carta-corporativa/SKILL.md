---
name: carta-corporativa
description: Use para produzir cartas formais externas (agradecimentos, parcerias, representatividade).
category: administrativo
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with: []
version: 0.1.0
status: rascunho
---

# Carta Corporativa

## Objetivo
Redigir cartas formais externas para diferentes finalidades, mantendo timbre institucional.

## Entradas
- `finalidade` (string)
- `destinatario` (dict)
- `conteudo` (string)

## Saída
Carta com timbre, local/data, vocativo, corpo, fechamento e assinatura.

## Boas práticas
- Formal, cordial.
- Sem marcas de informalidade.
- Data completa.