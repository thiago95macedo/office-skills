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
version: 0.1.0
status: rascunho
---

# Cobrança

## Objetivo
Produzir mensagens de cobrança cordiais, firmes e rastreáveis, calibradas pelo tempo de atraso e perfil do cliente.

## Quando usar
- Faturas vencidas (amigável a partir de 7 dias, firme após 30).
- Negociação de parcelamento.
- Confirmação de acordo.

## Quando NÃO usar
- Para clientes em disputa jurídica ativa (usar canal jurídico).
- Para simples lembrete de vencimento futuro (usar `administrativo/email-corporativo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `cliente.nome` | string | sim |
| `cliente.contato` | string | sim |
| `fatura.numero` | string | sim |
| `fatura.valor` | number | sim |
| `fatura.vencimento` | data | sim |
| `dias_atraso` | int | sim |
| `tom` | enum | sim |
| `historico` | dict | não |

## Saídas esperadas
- Mensagem principal
- Histórico do que foi feito até agora
- Próxima ação sugerida
- Canal de contato

## Fluxo interno
1. Identificar tom pelo `dias_atraso`.
2. Listar histórico (e-mails anteriores, promessas).
3. Redigir mensagem respeitosa, citando fatura e vencimento.
4. Sugerir próxima ação (pagamento, renegociação, contato).
5. Indicar canal direto.

## Boas práticas
- Cordial, sem agressividade.
- Citar número e data exatos.
- Oferecer opção de negociação.
- Manter registro no histórico.

## Limitações
- Não toma decisão sobre juros/multa.
- Não interrompe fornecimento (decisão gerencial).

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- ERP financeiro
- Sistema de boletos
- CRM
## Secoes de referencia (geradas)

Descricao desta Skill: Use quando precisar redigir mensagem de cobrança a cliente inadimplente, preservando o relacionamento e acelerando o pagamento.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

