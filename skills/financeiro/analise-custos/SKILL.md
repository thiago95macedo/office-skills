---
name: analise-custos
description: Use quando precisar decompor a estrutura de custos de um produto ou serviço, calcular preço de venda sugerido e identificar oportunidades de margem.
category: financeiro
priority: essencial
depends_on: []
composes_with:
  - comercial/orcamento
  - comercial/proposta-comercial
  - financeiro/justificativa-financeira
  - financeiro/orcamento-empresarial
version: 0.1.0
status: rascunho
---

# Análise de Custos

## Objetivo
Decompor custos diretos, indiretos e margem de um produto ou serviço, oferecendo preço de venda sugerido e análise de sensibilidade.

## Quando usar
- Definir preço de venda de um novo serviço ou produto.
- Repactuar tabela de preços.
- Avaliar se um contrato é rentável.
- Subsidiar uma proposta comercial.

## Quando NÃO usar
- Para composição rápida de orçamento já previamente tabelado (usar `comercial/orcamento`).
- Para cálculo fiscal/tributário detalhado (usar skill de área jurídica/tributária especializada).

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `itens_custo` | lista | sim | Itens de custo direto (materiais, mão de obra, serviços) |
| `custos_indiretos` | dict | sim | Rateio de custos fixos |
| `margem_desejada` | número | sim | Margem alvo (em %) |
| `impostos` | dict | não | Alíquotas por tributo |
| `concorrencia` | dict | não | Preços médios de mercado |
| `cenario` | enum | não | conservador / base / agressivo |

## Saídas esperadas
- Tabela de decomposição de custos.
- Subtotal, impostos, lucro, preço sugerido.
- Análise de sensibilidade por cenário.
- Premissas documentadas.

## Fluxo interno
1. Receber `itens_custo` e classificar como direto/indireto.
2. Aplicar rateio de `custos_indiretos` por critério (volume, receita, horas).
3. Calcular custo unitário total.
4. Aplicar impostos e margem desejada.
5. Gerar preço de venda sugerido.
6. Construir 3 cenários: conservador, base, agressivo.
7. Comparar com `concorrencia` quando fornecida.
8. Listar premissas e limitações.

## Boas práticas
- Discriminar cada item de custo (não agrupar).
- Documentar critério de rateio.
- Sinalizar premissas frágeis.
- Apresentar três cenários sempre que possível.

## Limitações
- Não acessa bases fiscais em tempo real.
- Não considera custo de oportunidade do capital.
- Não calcula ICMS/diferenciais interestaduais automaticamente.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`.

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- ERP
- Sistema fiscal
- BI