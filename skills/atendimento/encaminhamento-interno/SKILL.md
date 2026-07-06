---
name: encaminhamento-interno
description: Use para direcionar uma demanda para a área interna correta, com contexto suficiente.
category: atendimento
priority: recomendada
depends_on: []
composes_with:
  - atendimento/triagem-mensagens
version: 0.1.0
status: rascunho
---

# Encaminhamento Interno

## Objetivo
Redigir mensagem de repasse de demanda para área responsável, com contexto completo e SLA sugerido.

## Quando usar
- Demanda que pertence a outra área.
- Escalonamento de ticket.
- Encaminhamento de lead.

## Quando NÃO usar
- Quando a demanda é da própria área.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `demanda_original` | string | sim |
| `area_destino` | string | sim |
| `contexto_cliente` | dict | sim |
| `sla` | string | sim |
| `responsavel_destino` | string | não |

## Saídas esperadas
- Mensagem para área interna.
- Contexto do cliente.
- SLA.
- Próxima ação esperada.

## Fluxo interno
1. Resumir demanda em 3 linhas.
2. Listar contexto do cliente.
3. Indicar SLA.
4. Sugerir próxima ação.

## Limitações
- Não envia mensagem automaticamente.

## Possíveis integrações
- Sistema de tickets
- Slack