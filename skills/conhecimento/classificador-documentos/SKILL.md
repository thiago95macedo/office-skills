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
## Secoes de referencia (geradas)

Descricao desta Skill: Use para classificar documentos por tipo (contrato, relatório, proposta, NF) e tema.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

