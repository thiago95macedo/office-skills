# Fluxo — Atendimento Omnichannel

## Objetivo de negócio
Operar caixa multi-canal com triagem, classificação e resposta eficiente.

## Sequência de Skills

1. `atendimento/triagem-mensagens` — classificar lote de mensagens.
2. `suporte/classificador-tickets` — abrir ticket quando aplicável.
3. `atendimento/resposta-rapida` — responder casos simples.
4. `atendimento/encaminhamento-interno` — repassar casos complexos.
5. `suporte/faq-tecnico` — responder usando base (quando houver).
6. `comercial/follow-up` — sequência de reativação (quando aplicável).

## Saída final

- Tabela de triagem
- Tickets abertos com SLA
- Respostas enviadas
- Encaminhamentos realizados