# Casos de teste — Redator Corporativo

## Caso 1 — Revisão de e-mail coloquial
**Entrada:** rascunho informal.
**Esperado:** tom convertido para formal; coloquialismos removidos; tamanho ≤ 80 palavras.

## Caso 2 — Comunicado interno sem dados
**Entrada:** objetivo + público + tom.
**Esperado:** estrutura com seção "O que muda" e "Como proceder"; tom coerente com configuração.

## Caso 3 — Revisão de proposta regulada
**Entrada:** proposta com adjetivos vazios.
**Esperado:** remoção de vocabulário bloqueado; substituição por evidência operacional; manutenção da mensagem original.