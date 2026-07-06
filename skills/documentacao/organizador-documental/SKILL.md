---
name: organizador-documental
description: Use para propor estrutura de pastas e nomenclatura para acervos de documentos (políticas, contratos, projetos).
category: documentacao
priority: opcional
depends_on: []
composes_with:
  - conhecimento/classificador-documentos
  - produtividade/organizador-arquivos
version: 0.1.0
status: rascunho
---

# Organizador Documental

## Objetivo
Sugerir estrutura de pastas, convenção de nomes e taxonomia para acervos corporativos.

## Entradas
- `tipo_acervo` (enum)
- `volumetria_estimada` (int)
- `usuarios` (lista)

## Saída
Mapa de pastas + convenção de nomes + guia de uso.

## Boas práticas
- Estrutura rasa.
- Nomes sem caracteres especiais.