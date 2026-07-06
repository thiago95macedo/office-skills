---
name: campanha-email
description: Use para estruturar sequência de e-mails marketing (lançamento, nutrição, reativação).
category: marketing
priority: opcional
depends_on:
  - administrativo/email-corporativo
composes_with:
  - marketing/conteudo-linkedin
version: 0.1.0
status: rascunho
---

# Campanha de E-mail

## Objetivo
Construir sequência de e-mails com objetivo claro, segmentação, conteúdo progressivo e CTA consistente.

## Quando usar
- Lançamento.
- Nutrição de leads.
- Reativação de base.

## Quando NÃO usar
- Para 1 e-mail avulso (usar `administrativo/email-corporativo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `objetivo` | string | sim |
| `publico` | string | sim |
| `quantidade` | int | sim |
| `gatilhos` | lista | não |
| `cta_principal` | string | sim |

## Saídas esperadas
- Sequência numerada de e-mails.
- Assunto, pré-cabeçalho, corpo, CTA.
- Cronograma de envio.

## Fluxo interno
1. Definir objetivo e segmentação.
2. Planejar sequência com progressão lógica.
3. Redigir cada e-mail.
4. Definir cronograma.
5. Revisar entregabilidade (assunto curto, sem spam words).

## Limitações
- Não envia automaticamente.
- Não mede resultados.

## Dependências
- `administrativo/email-corporativo`

## Possíveis integrações
- Mailchimp
- RD Station