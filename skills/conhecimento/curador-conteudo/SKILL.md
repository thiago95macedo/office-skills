---
name: curador-conteudo
description: Use para selecionar, organizar e resumir conteúdos relevantes para um objetivo.
category: conhecimento
priority: opcional
depends_on:
  - produtividade/resumo-executivo
composes_with:
  - marketing/artigo-blog
  - suporte/base-conhecimento
version: 0.1.0
status: rascunho
---

# Curador de Conteúdo

## Objetivo
Selecionar, organizar e resumir conteúdos de fontes variadas para um objetivo definido.

## Quando usar
- Newsletter interna.
- Briefing temático.
- Preparação de treinamento.

## Quando NÃO usar
- Para conteúdo único (usar `produtividade/resumo-executivo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `objetivo` | string | sim |
| `fontes` | lista | sim |
| `formato_saida` | enum | sim |

## Saídas esperadas
- Lista curada.
- Resumo por item.
- Recomendações.

## Limitações
- Não pesquisa em tempo real.

## Dependências
- `produtividade/resumo-executivo`

## Possíveis integrações
- Feedly
- Pocket
## Secoes de referencia (geradas)

Descricao desta Skill: Use para selecionar, organizar e resumir conteúdos relevantes para um objetivo.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

