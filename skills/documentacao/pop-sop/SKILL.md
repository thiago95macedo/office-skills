---
name: pop-sop
description: Use para criar POP (Procedimento Operacional Padrão) ou SOP auditável, com objetivo, escopo, responsabilidades, materiais, procedimento, registros.
category: documentacao
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - documentacao/checklist
  - documentacao/manual-tecnico
version: 0.1.0
status: rascunho
---

# POP / SOP

## Objetivo
Gerar procedimento operacional padrão auditável, pronto para aprovação em sistema de qualidade.

## Entradas
- `titulo` (string)
- `objetivo` (string)
- `escopo` (string)
- `responsaveis` (lista)
- `materiais` (lista)
- `etapas` (lista)
- `registros` (lista)
- `referencias` (lista)

## Saída
POP completo com cabeçalho de versionamento e numeração.

## Boas práticas
- Verbos no infinitivo.
- Etapas numeradas.
- Indicadores de conformidade ao final.