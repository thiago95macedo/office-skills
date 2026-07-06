---
name: orcamento
description: Use para gerar orçamento detalhado (itens, quantidades, valores unitários, totais, condições de pagamento) a partir de um escopo.
category: comercial
priority: essencial
depends_on:
  - comercial/escopo-tecnico
composes_with:
  - comercial/proposta-comercial
  - financeiro/analise-custos
version: 0.1.0
status: rascunho
---

# Orçamento

## Objetivo
Gerar orçamento estruturado, com itens, quantidades, valores unitários, totais, impostos destacados e condições de pagamento.

## Quando usar
- Após definição de escopo.
- Para anexar a propostas ou processos de compra.

## Quando NÃO usar
- Quando ainda não há escopo definido.

## Entradas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `escopo` | dict | sim |
| `tabela_precos` | dict | sim |
| `impostos` | dict | não |
| `condicoes_pagamento` | dict | sim |

## Saída
Tabela de itens, subtotal, impostos, total geral, condições.

## Boas práticas
- Sempre discriminar impostos.
- Sempre indicar moeda e condições.
- Sinalizar itens opcionais.

## Limitações
- Não consulta tabelas tributárias em tempo real.