---
name: justificativa-financeira
description: Use para justificar aquisição ou investimento com base em ROI, payback, riscos e impacto no negócio.
category: financeiro
priority: opcional
depends_on:
  - financeiro/analise-custos
composes_with:
  - financeiro/orcamento-empresarial
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# Justificativa Financeira

## Objetivo
Sustentar tecnicamente decisão de compra, contratação ou investimento com dados financeiros e operacionais verificáveis.

## Quando usar
- Compra de equipamento de alto valor.
- Contratação de sistema/serviço.
- Investimento em expansão.
- Apresentação para diretoria ou conselho.

## Quando NÃO usar
- Para compras de baixo valor com aprovação automática.
- Para investimentos com ROI já mapeado em plano estratégico (apenas referenciar).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `objeto` | string | sim |
| `valor` | number | sim |
| `beneficios_quantificados` | dict | sim |
| `beneficios_qualitativos` | lista | sim |
| `payback_estimado` | string | sim |
| `riscos` | lista | sim |
| `alternativas` | lista | não |

## Saídas esperadas
- Resumo executivo.
- Cenário atual vs cenário proposto.
- Benefícios quantificados.
- ROI e payback.
- Riscos e mitigação.
- Alternativas consideradas.

## Fluxo interno
1. Descrever objeto e valor.
2. Comparar cenário atual vs proposto.
3. Quantificar benefícios (receitas, economia, produtividade).
4. Calcular ROI e payback.
5. Listar riscos e mitigação.
6. Listar alternativas rejeitadas com motivo.

## Boas práticas
- Benefícios quantificados sempre que possível.
- Premissas claras.
- Comparação com alternativas.

## Limitações
- Não modela cenários estocásticos complexos.
- Não calcula VPL/TIR automaticamente (mas pode citar).

## Dependências
- `financeiro/analise-custos`

## Possíveis integrações
- BI
- ERP