---
name: extrator-dados
description: Use para extrair dados estruturados (campos, tabelas, listas) de texto não estruturado.
category: produtividade
priority: essencial
depends_on: []
composes_with:
  - produtividade/analise-planilha
  - conhecimento/classificador-documentos
version: 0.1.0
status: rascunho
---

# Extrator de Dados

## Objetivo
Converter texto não estruturado em dados estruturados (JSON/CSV/YAML) conforme schema definido.

## Quando usar
- Migração de planilhas legadas.
- Extração de dados de PDFs.
- Padronização de cadastros.

## Quando NÃO usar
- Para dados já estruturados.
- Para documentos com regras complexas e baixa confiabilidade.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `fonte` | texto | sim |
| `schema_destino` | dict | sim |
| `politica_ambiguo` | enum | sim |

## Saídas esperadas
- Lista de objetos no schema.
- Lista de exceções/itens não mapeados.
- Confiança média por campo.

## Fluxo interno
1. Receber fonte e schema.
2. Identificar entidades.
3. Mapear para campos.
4. Sinalizar ambiguidades.
5. Produzir saída estruturada.

## Limitações
- Não lê anexos sem OCR.

## Dependências
- Nenhuma

## Possíveis integrações
- OCR
- RPA
## Secoes de referencia (geradas)

Descricao desta Skill: Use para extrair dados estruturados (campos, tabelas, listas) de texto não estruturado.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

