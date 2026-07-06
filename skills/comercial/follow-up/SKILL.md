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
## Secoes de referencia (geradas)

Descricao desta Skill: Use para redigir mensagens de retorno após reunião, envio de proposta, contato frio ou negociação parada.

## Quando NÃO usar

Listar situacoes em que outra Skill ou processo deve ser usado.

## Entradas esperadas

Documentar campos, tipos e obrigatoriedade.

## Saídas esperadas

Documentar artefatos produzidos pela Skill.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Limitações

Declarar restricoes conhecidas da Skill.

## Dependências

Apontar Skills que esta Skill depende.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

## Possíveis integrações

Listar integracoes com sistemas externos.

