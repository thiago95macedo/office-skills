---
name: prestacao-contas
description: Use para documentar uso de recursos em projeto, viagem, evento ou verba corporativa, com rastreabilidade de cada item.
category: financeiro
priority: recomendada
depends_on: []
composes_with:
  - financeiro/cobranca
  - gestao/plano-acao
version: 0.1.0
status: rascunho
---

# Prestação de Contas

## Objetivo
Documentar com transparência e rastreabilidade cada item de despesa de um projeto, viagem, evento ou verba corporativa.

## Quando usar
- Após viagem corporativa.
- Após evento patrocinado pela empresa.
- Em prestação de contas de projeto com verba designada.
- Em auditoria interna.

## Quando NÃO usar
- Para simples relatório de despesas pontuais (usar `produtividade/resumo-executivo`).
- Para contabilização fiscal (usar ferramenta contábil).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `periodo` | string | sim |
| `responsavel` | string | sim |
| `centro_custo` | string | sim |
| `itens` | lista | sim |
| `valor_total_recebido` | number | sim |
| `valor_total_gasto` | number | sim |
| `saldo` | number | sim |

## Saídas esperadas
- Cabeçalho com período, responsável, centro de custo.
- Tabela numerada de itens (descrição, valor, NF/recibo, data).
- Total recebido, gasto, saldo.
- Anexo de comprovantes referenciado.
- Parecer final (aprovado / pendente / reprovado).

## Fluxo interno
1. Receber dados do período e responsável.
2. Listar itens numerados sequencialmente.
3. Referenciar NF/recibo para cada item.
4. Calcular totais e saldo.
5. Sinalizar itens sem comprovante.
6. Emitir parecer.

## Boas práticas
- Numerar itens sequencialmente.
- Citar NF/recibo.
- Sinalizar divergências.
- Documentar saldo (a devolver ou a receber).

## Limitações
- Não verifica autenticidade de comprovantes.
- Não calcula impostos sobre reembolsos.

## Dependências
- Nenhuma

## Possíveis integrações
- ERP
- Sistema de reembolso
- GED