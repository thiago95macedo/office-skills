---
name: atendimento-lead
description: Use para triagem e resposta inicial a leads vindos de canais diversos (site, LinkedIn, indicação).
category: comercial
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - comercial/follow-up
  - comercial/escopo-tecnico
version: 0.1.0
status: rascunho
---

# Atendimento a Lead

## Objetivo
Padronizar primeira resposta a leads, classificando potencial e sugerindo próximo passo.

## Entradas
- `mensagem_lead` (string)
- `canal` (enum)
- `historico` (dict, opcional)

## Saída
Classificação (quente/morno/frio) + resposta inicial + próxima ação.

## Boas práticas
- Responder em até 24h.
- Confirmar interesse e direcionar conversa.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para triagem e resposta inicial a leads vindos de canais diversos (site, LinkedIn, indicação).

## Quando usar

Listar situacoes em que a Skill e a ferramenta correta.

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

