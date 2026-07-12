---
name: resposta-rapida
description: Use para gerar resposta curta, cordial e útil a demandas de atendimento (até 80 palavras).
category: atendimento
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - atendimento/triagem-mensagens
  - atendimento/encaminhamento-interno
version: 0.2.0
status: estavel
references:
  - Rogers, C. R. Empathic: An Unappreciated Way of Being. The Counseling Psychologist. 1975.
  - Covey, S. R. The 7 Habits of Highly Effective People. 1989 (Hábito 5 — Empathic Listening).
  - Zendesk CX Trends 2024 (FCR e SLA de primeira resposta).
---

# Resposta Rápida

## Objetivo
Produzir respostas curtas (até 80 palavras), cordiais e úteis para demandas de atendimento, com CTA claro e tratamento empático (Rogers, 1959; Covey, 1989).

## Quando usar
- Confirmação de recebimento de demanda.
- Solicitação de informação complementar ao cliente.
- Direcionamento a responsável ou área.
- Esclarecimento de dúvida simples e direta.
- Resposta a objeção de baixa complexidade.

## Quando NÃO usar
- Para respostas técnicas detalhadas (usar `suporte/faq-tecnico`).
- Para objeções comerciais complexas (usar `comercial/tratamento-objecoes`).
- Para mensagens em lote (usar template de sistema).

## Estrutura recomendada

| # | Bloco | Limite |
|---|-------|--------|
| 1 | **Saudação personalizada** | 1 linha |
| 2 | **Confirmação de entendimento** | 1-2 frases (mostrar empatia) |
| 3 | **Próximo passo / informação** | 1-2 frases |
| 4 | **CTA claro** | 1 frase |
| 5 | **Fechamento cordial** | 1 linha |

## Tom conforme persona e canal

| Persona | Tom | Exemplo |
|---------|-----|---------|
| Cliente irritado | Empático + resolutivo | "Entendo a frustração. Vou resolver agora." |
| Cliente novo | Cordial + didático | "Obrigado pelo contato. Vou explicar passo a passo." |
| Cliente recorrente | Direto + pessoal | "Olá, [nome]! Já localizei seu pedido." |
| Dúvida técnica | Preciso + referência | "Conforme a documentação do produto X, item 3.2..." |
| Reclamação | Empático + corretivo | "Lamento pelo ocorrido. Vou abrir [protocolo] e retornar." |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `mensagem_original` | string | sim | Mensagem do cliente |
| `contexto` | dict | sim | Contexto do cliente (histórico, produto, ticket) |
| `tom` | enum | sim | cordial / empatico / tecnico / resolutivo |
| `canal` | enum | sim | email / whatsapp / chat / telefone |
| `cta_desejado` | string | sim | Próximo passo esperado |

## Saídas esperadas
- Mensagem curta (≤ 80 palavras).
- Saudação personalizada.
- Confirmação de entendimento.
- Próximo passo claro.
- Fechamento cordial.
- Tom conforme persona.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom padrão, saudações).
2. Identificar persona do cliente pelo contexto.
3. Selecionar tom apropriado.
4. Redigir saudação personalizada (usar nome quando disponível).
5. Confirmar entendimento com empatia (Rogers: "sentir como se fosse o outro").
6. Informar próximo passo ou solicitar informação complementar.
7. Inserir CTA claro.
8. Fechar cordialmente.
9. Validar tamanho (≤ 80 palavras).

## Boas práticas (baseado em Rogers e Covey)

- **Empatia antes de solução** — Rogers: "sentir o mundo do outro como se fosse o seu".
- **Escuta empática** (Covey) — ouvir para entender antes de responder.
- **Saudação personalizada** — usar nome do cliente.
- **Confirmação de entendimento** — mostrar que ouviu.
- **Próximo passo objetivo** — sem ambiguidade.
- **CTA único** — confusão reduz conversão.
- **Cordialidade constante** — mesmo com cliente difícil.
- **Tempo de resposta** — responder em até SLA (e-mail 24h, chat 5min, WhatsApp 1h).
- **Sem jargão** — adaptar para o cliente.
- **Brevidade** — respeito ao tempo do cliente.
- **Saudação não genérica** — não "Prezados" para um único cliente.

## Armadilhas comuns
- Resposta genérica ("Recebemos sua mensagem") — sem empatia.
- Demorar para responder (acima do SLA) — frustra o cliente.
- Misturar "Prezados" para uma pessoa.
- Resposta defensiva ("Não é nossa responsabilidade") — gera churn.
- Resposta longa — cliente desiste antes do final.
- Múltiplos CTAs — confusão.
- Esquecer de cumprimentar pelo nome.
- Sem próximo passo — cliente fica perdido.

## Limitações
- Não trata questões técnicas complexas.
- Não substitui análise de sentimento humana.
- Não envia automaticamente.
- Não acessa bases externas em tempo real.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Confirmação de recebimento
- `02-intermediario.md` — Pedido de informação complementar
- `03-avancado.md` — Resposta empática a reclamação

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Plataformas de atendimento (Zendesk, Freshdesk, Intercom, HubSpot Service)
- Chat corporativo (Slack, Microsoft Teams)
- CRM (RD, HubSpot, Salesforce)
- Macros e templates da plataforma