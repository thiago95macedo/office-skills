---
name: manual-tecnico
description: Use para produzir manuais técnicos completos (instalação, operação, manutenção) de equipamentos ou sistemas.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
  - documentacao/pop-sop
composes_with:
  - documentacao/checklist
  - rh/treinamento-materiais
version: 0.1.0
status: rascunho
---

# Manual Técnico

## Objetivo
Documentar equipamentos/sistemas com seções padronizadas para uso, manutenção e troubleshooting.

## Entradas
- `equipamento` (string)
- `secoes` (lista)
- `nivel_tecnico` (enum)

## Saída
Manual com sumário, introdução, instalação, operação, manutenção, segurança, anexos.

## Boas práticas
- Diagramas quando possível.
- Linguagem técnica calibrada ao público.