---
name: orcamento-empresarial
description: Use para planejar e acompanhar receitas, despesas e investimentos por período (mensal, trimestral ou anual).
category: financeiro
priority: recomendada
depends_on: []
composes_with:
  - gestao/kpi-okr
  - gestao/dashboard-executivo
  - financeiro/analise-custos
version: 0.1.0
status: rascunho
---

# Orçamento Empresarial

## Objetivo
Planejar receitas, despesas e investimentos, comparando previsto vs realizado e permitindo decisões gerenciais orientadas a dados.

## Quando usar
- Planejamento anual ou trimestral.
- Revisões orçamentárias (orçamento rolling forecast).
- Acompanhamento mensal.
- Apresentação ao conselho.

## Quando NÃO usar
- Para orçamento de um único projeto ou serviço (usar `comercial/orcamento`).
- Para análise de custos de um item específico (usar `financeiro/analise-custos`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `periodo` | string | sim |
| `receitas_previstas` | dict | sim |
| `despesas_previstas` | dict | sim |
| `investimentos` | dict | sim |
| `realizado` | dict | não |
| `cenarios` | lista | não |

## Saídas esperadas
- Tabela por categoria com previsto/realizado.
- Subtotais e totais.
- Variações percentuais.
- Alertas.
- Premissas e riscos.

## Fluxo interno
1. Receber estrutura de receitas, despesas e investimentos.
2. Organizar por categoria.
3. Comparar com `realizado` quando fornecido.
4. Calcular variações.
5. Sinalizar desvios > 10%.
6. Listar premissas.

## Boas práticas
- Categorização estável entre períodos.
- Comentário em variações relevantes.
- Cenários quando o ambiente for incerto.

## Limitações
- Não acessa dados de ERP em tempo real.
- Não calcula impostos específicos sem declaração.

## Dependências
- Nenhuma

## Possíveis integrações
- ERP
- BI
- Planilhas corporativas
## Secoes de referencia (geradas)

Descricao desta Skill: Use para planejar e acompanhar receitas, despesas e investimentos por período (mensal, trimestral ou anual).

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

