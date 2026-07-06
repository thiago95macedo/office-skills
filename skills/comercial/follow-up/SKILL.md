---
name: follow-up
description: Use para redigir mensagens de retorno após reunião, envio de proposta, contato frio ou negociação parada.
category: comercial
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - comercial/atendimento-lead
version: 0.1.0
status: rascunho
---

# Follow-up

## Objetivo
Manter o relacionamento comercial ativo, retomar conversas e acelerar ciclos de decisão.

## Quando usar
- Após reunião com cliente.
- Após envio de proposta sem retorno.
- Após contato sem avanço.

## Entradas
- `contexto_interacao` (string)
- `tipo_followup` (enum: reuniao|proposta|negociacao|introducao)
- `proximo_passo_desejado` (string)

## Saída
Mensagem curta, cordial, com CTA claro.

## Boas práticas
- Seja breve.
- Relembre o último ponto tratado.
- Sugira próximo passo objetivo.