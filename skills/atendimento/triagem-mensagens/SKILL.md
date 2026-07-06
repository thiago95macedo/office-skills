---
name: triagem-mensagens
description: Use para classificar, priorizar e recomendar próxima ação sobre mensagens recebidas em canais diversos.
category: atendimento
priority: essencial
depends_on: []
composes_with:
  - atendimento/resposta-rapida
  - atendimento/encaminhamento-interno
version: 0.1.0
status: rascunho
---

# Triagem de Mensagens

## Objetivo
Classificar mensagens por urgência, tipo, área responsável e próxima ação, evitando atrasos em canais críticos.

## Quando usar
- Caixa de entrada compartilhada.
- WhatsApp corporativo.
- Chat do site.

## Quando NÃO usar
- Para mensagens individuais já categorizadas.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `mensagens` | lista | sim |
| `canal` | enum | sim |
| `regras_classificacao` | dict | sim |

## Saídas esperadas
- Classificação por urgência (alta/média/baixa).
- Tipo (comercial/suporte/financeiro/RH/etc.).
- Área responsável.
- SLA sugerido.
- Próxima ação recomendada.

## Fluxo interno
1. Receber lote de mensagens.
2. Identificar urgência por palavras-chave e remetente.
3. Classificar tipo conforme regras.
4. Atribuir área responsável.
5. Sugerir SLA.
6. Sugerir próxima ação.

## Boas práticas
- SLA explícito por urgência.
- Sinalização visual (🔴🟡🟢).
- Cliente VIP com tratamento preferencial.

## Limitações
- Não lê anexos automaticamente.
- Não acessa CRM.

## Dependências
- Nenhuma

## Possíveis integrações
- CRM
- Zendesk
- Front