---
name: faq-tecnico
description: Use para construir FAQ técnico sobre produtos/serviços com respostas verificáveis.
category: suporte
priority: recomendada
depends_on: []
composes_with:
  - documentacao/faq-corporativo
  - suporte/base-conhecimento
version: 0.1.0
status: rascunho
---

# FAQ Técnico

## Objetivo
Construir FAQ técnico com perguntas frequentes, respostas precisas e referência a documentação técnica.

## Quando usar
- Base de conhecimento pública.
- FAQ de produto.
- Autoatendimento.

## Quando NÃO usar
- Para FAQ institucional geral (usar `documentacao/faq-corporativo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `produto` | string | sim |
| `perguntas_respostas` | lista | sim |
| `referencias` | lista | sim |

## Saídas esperadas
- FAQ agrupado por tema.
- Cada resposta com referência técnica.

## Limitações
- Não testa links quebrados.

## Dependências
- Nenhuma

## Possíveis integrações
- Zendesk Guide
- Notion