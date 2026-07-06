---
name: classificador-documentos
description: Use para classificar documentos por tipo (contrato, relatório, proposta, NF) e tema.
category: conhecimento
priority: essencial
depends_on: []
composes_with:
  - documentacao/organizador-documental
  - produtividade/extrator-dados
version: 0.1.0
status: rascunho
---

# Classificador de Documentos

## Objetivo
Classificar documentos por tipo, tema, área e urgência automaticamente.

## Quando usar
- Triagem de documentos.
- Organização de GED.
- Indexação para busca.

## Quando NÃO usar
- Para documento já classificado.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `documentos` | lista | sim |
| `taxonomia` | dict | sim |
| `saida_desejada` | enum | sim |

## Saídas esperadas
- Lista classificada.
- Tags.
- Caminho sugerido.

## Limitações
- Não lê PDFs sem OCR.

## Dependências
- Nenhuma

## Possíveis integrações
- GED
- SharePoint