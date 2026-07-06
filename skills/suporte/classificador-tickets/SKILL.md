---
name: classificador-tickets
description: Use para classificar tickets de suporte por categoria, prioridade e produto.
category: suporte
priority: essencial
depends_on: []
composes_with:
  - suporte/faq-tecnico
  - suporte/base-conhecimento
version: 0.1.0
status: rascunho
---

# Classificador de Tickets

## Objetivo
Classificar tickets por categoria (incidente/solicitação/problema/mudança), prioridade (P1–P4) e produto/área.

## Quando usar
- Integração omnichannel.
- Triagem automatizada.
- Definição de SLA inicial.

## Quando NÃO usar
- Quando o ticket já vem classificado.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `descricao` | string | sim |
| `canal` | enum | sim |
| `cliente_vip` | bool | não |
| `regras_categorizacao` | dict | sim |

## Saídas esperadas
- Categoria ITIL.
- Prioridade.
- Produto/área.
- SLA sugerido.
- Sugestão de artigo da base de conhecimento.

## Fluxo interno
1. Detectar palavras-chave.
2. Mapear para categoria.
3. Calcular prioridade por impacto × urgência.
4. Sugerir artigo relacionado.

## Limitações
- Não acessa telemetria de sistemas.

## Dependências
- Nenhuma

## Possíveis integrações
- Zendesk
- Jira Service Management