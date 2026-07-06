---
name: padronizador-textos
description: Use para aplicar padrão da casa (tom, vocabulário, formatação) a textos existentes sem alterar o conteúdo técnico.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
  - _core/configurador-empresa
composes_with:
  - todas as Skills que produzem texto
version: 0.1.0
status: rascunho
---

# Padronizador de Textos

## Objetivo
Revisar textos existentes para alinhar tom, vocabulário e formatação ao padrão da empresa.

## Entradas
- `texto_original` (string)
- `alvos_padronizacao` (lista: tom | vocabulario | formatacao | ortografia)

## Saída
Texto padronizado + lista de alterações aplicadas.

## Boas práticas
- Manter sentido original.
- Sinalizar mudanças estilísticas sem alterar técnica.