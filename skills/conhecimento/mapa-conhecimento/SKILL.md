---
name: mapa-conhecimento
description: Use para mapear ativos de conhecimento da empresa (documentos, especialistas, bases, ferramentas).
category: conhecimento
priority: recomendada
depends_on:
  - conhecimento/classificador-documentos
composes_with:
  - suporte/base-conhecimento
version: 0.1.0
status: rascunho
---

# Mapa de Conhecimento

## Objetivo
Inventariar ativos de conhecimento, identificar lacunas e especialistas por domínio.

## Quando usar
- Onboarding de gestão.
- Planejamento de sucessão.
- Auditoria.

## Quando NÃO usar
- Para FAQ específico (usar `suporte/faq-tecnico`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `areas` | lista | sim |
| `documentos` | lista | sim |
| `especialistas` | lista | sim |

## Saídas esperadas
- Mapa visual.
- Lacunas.
- Riscos.

## Limitações
- Não entrevista especialistas.

## Dependências
- `conhecimento/classificador-documentos`

## Possíveis integrações
- Confluence
- Notion