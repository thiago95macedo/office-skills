---
name: organizador-arquivos
description: Use para sugerir estrutura de pastas, nomes de arquivos e regras de versionamento.
category: produtividade
priority: opcional
depends_on: []
composes_with:
  - documentacao/organizador-documental
  - conhecimento/classificador-documentos
version: 0.1.0
status: rascunho
---

# Organizador de Arquivos

## Objetivo
Propor convenção de nomes, estrutura de pastas e regras de versionamento para um acervo.

## Quando usar
- Início de projeto.
- Reorganização de área.
- Padronização entre times.

## Quando NÃO usar
- Para acervo já estruturado.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `tipo_acervo` | enum | sim |
| `volumetria` | int | sim |
| `usuarios` | lista | sim |
| `restricoes` | lista | não |

## Saídas esperadas
- Mapa de pastas.
- Convenção de nomes.
- Regra de versionamento.

## Limitações
- Não move arquivos automaticamente.

## Dependências
- Nenhuma

## Possíveis integrações
- SharePoint
- Google Drive