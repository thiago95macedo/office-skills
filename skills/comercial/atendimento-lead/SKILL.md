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