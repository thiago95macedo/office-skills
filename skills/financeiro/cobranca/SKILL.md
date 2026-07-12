---
name: cobranca
description: Use quando precisar redigir mensagem de cobrança a cliente inadimplente, preservando o relacionamento e acelerando o pagamento.
category: financeiro
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - financeiro/prestacao-contas
  - administrativo/email-corporativo
  - comercial/follow-up
version: 0.2.0
status: estavel
references:
  - BRASIL. Lei 8.078/1990 — Código de Defesa do Consumidor (CDC).
  - BRASIL. Lei 14.181/2021 — Superendividamento (alterou CDC, incluiu art. 71-A).
  - BRASIL. Lei 14.692/2023 — Horário de centrais de cobrança.
  - BRASIL. Lei 13.709/2018 — LGPD.
  - Serasa Experian. Régua de Cobrança e Cobrança Inteligente. 2024.
  - Súmula 359 do STJ — Notificação prévia à negativação.
---

# Cobrança

## Objetivo
Produzir mensagens de cobrança cordiais, firmes e rastreáveis, calibradas pelo tempo de atraso e perfil do cliente, respeitando o CDC, a LGPD e as boas práticas de régua de cobrança.

## Quando usar
- Faturas vencidas (amigável a partir de 7 dias, firme após 30).
- Negociação de parcelamento ou acordo.
- Confirmação de acordo e agradecimento.
- Lembrete prévio ao vencimento (D-3 ou D-1).
- Notificação prévia à negativação (art. 43, §2º do CDC e Súmula 359 STJ).

## Quando NÃO usar
- Para clientes em disputa jurídica ativa (usar canal jurídico).
- Para negativação (procedimento distinto, exige notificação prévia com 10+ dias úteis).
- Para protesto em cartório (usar fluxo específico).

## Conformidade legal obrigatória

| Marco | Aplicação |
|-------|-----------|
| **CDC art. 42** | Vedado constranger devedor (expor a ridículo, contato com vizinhos) |
| **CDC art. 42-A** | Obrigatória notificação prévia com prazo para pagamento sem acréscimos |
| **CDC art. 43, §2º + Súmula 359 STJ** | Negativação só após notificação prévia com 10+ dias úteis |
| **CDC art. 71-A** (incluído pela Lei 14.181/2021) | Proteção ao superendividado; veda renegociação forçada |
| **Lei 14.692/2023** | Cobrança por central limitada a 8h–20h dias úteis, até 14h aos sábados |
| **LGPD Lei 13.709/2018** | Tratamento de dados pessoais com base legal e finalidade específica |

## Régua de cobrança sugerida

| D+X | Canal | Tom |
|-----|-------|-----|
| D-3 a D-1 | E-mail / push | Lembrete cordial pré-vencimento |
| D+1 a D+7 | E-mail / WhatsApp | Cordial — "identificamos atraso" |
| D+8 a D+15 | SMS / WhatsApp / ligação | Firme — "regularize" |
| D+15 a D+30 | Notificação prévia (CDC art. 42-A) | Formal — "última oportunidade antes de negativação" |
| D+30+ | Negativação (após notificação com 10+ dias úteis) | Institucional — "registrado em birôs" |
| D+60+ | Protesto em cartório | Jurídico-administrativo |
| D+90+ | Cessão para FIDC ou ação judicial | Decisão gerencial |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `cliente.nome` | string | sim | Nome ou razão social |
| `cliente.contato` | string | sim | Nome do contato |
| `cliente.perfil` | enum | sim | pessoa-fisica / pessoa-juridica |
| `cliente.vip` | bool | não | Cliente prioritário (tratamento VIP) |
| `fatura.numero` | string | sim | Número da fatura |
| `fatura.valor_original` | number | sim | Valor original em moeda |
| `fatura.vencimento` | data | sim | Data de vencimento original |
| `fatura.multa_juros` | number | não | Multa e juros aplicáveis |
| `dias_atraso` | int | sim | Dias desde vencimento |
| `tom` | enum | sim | amigavel / firme / formal / juridico |
| `historico` | dict | não | Mensagens anteriores, promessas |
| `canal` | enum | sim | email / whatsapp / sms / carta / ligacao |

## Saídas esperadas
- Mensagem principal (calibrada ao tom e ao canal)
- Tabela resumo com fatura, valor, vencimento, dias atraso
- CTA claro (link de pagamento, opção parcelamento, contato)
- Histórico de interações anteriores (quando aplicável)
- Próxima ação sugerida
- Canal direto para resposta

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom, canais oficiais, dados de cobrança).
2. Calcular tom automaticamente pelo `dias_atraso` (sugestão da régua).
3. Verificar histórico de interações anteriores (LGPD: dados lícitos).
4. Compor mensagem cordial, citando fatura, valor, vencimento, dias atraso.
5. Oferecer canal de negociação (parcelamento, desconto, contato).
6. Indicar próxima ação conforme etapa da régua.
7. Em D+15, incluir notificação prévia (10 dias úteis) para evitar litigância.
8. Em D+30+, mencionar consequência (negativação) de forma impessoal.
9. Respeitar horário permitido pela Lei 14.692/2023.
10. Validar checklist (cordialidade, dados corretos, CTA, sem constrangimento).

## Boas práticas
- **Cordialidade constante** — o tom varia (amigável → firme), mas nunca agressivo.
- **Citar números exatos** (fatura, valor, vencimento) — evitar ambiguidade.
- **Oferecer opções** (pagamento à vista, parcelado, renegociação).
- **Registrar histórico** para evitar cobrança duplicada.
- **Linguagem impessoal** após D+15 (não personalizar contra o devedor).
- **Respeitar LGPD** — não compartilhar dados do devedor com terceiros sem base legal.
- **Atendimento humanizado** — manter canal de diálogo aberto.
- **Cliente VIP** — tratamento prioritário, escalação para gestão.
- **Clientes em superendividamento** (art. 71-A) — encaminhar para repactuação.
- **Documentar tudo** — auditoria de cobrança precisa de histórico.

## Armadilhas comuns (a evitar)
- Cobrança agressiva ou constrangedora (CDC art. 42 — gera indenização).
- Cobrança sem notificação prévia (Súmula 359 STJ — invalida negativação).
- Cobrança fora de horário permitido (Lei 14.692/2023).
- Exposição do devedor a ridículo (lista pública, contato com vizinhos).
- Misturar comunicação de cobrança com ameaça jurídica prematura.
- Cobrança duplicada (sem checar histórico).
- Cobrança sem base legal (uso indevido de dados — LGPD).
- Falta de canal de negociação (cliente quer pagar, não consegue).

## Limitações
- Não toma decisão sobre juros/multa (validar com política comercial e jurídica).
- Não interrompe fornecimento (decisão gerencial).
- Não negativar automaticamente (procedimento separado, exige notificação).
- Não substitui processo jurídico de execução (quando aplicável).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Lembrete amigável pré-vencimento
- `02-intermediario.md` — Cobrança firme após 30 dias
- `03-avancado.md` — Notificação prévia à negativação

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- ERP financeiro (SAP, TOTVS, Omie)
- Plataforma de cobrança (Serasa, Equifax, Cora)
- Gateway de pagamento (Pagar.me, Stripe, Asaas)
- CRM (Pipedrive, HubSpot, Salesforce)
- WhatsApp Business API / Twilio / Zenvia