---
name: gerador-apresentacao
description: Use para estruturar apresentações (slides) com storyline claro, slides objetivos e CTA.
category: produtividade
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - produtividade/resumo-executivo
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# Gerador de Apresentação

## Objetivo
Estruturar apresentação completa (storyline, slides, mensagens-chave, CTA) pronta para produção visual.

## Quando usar
- Apresentações executivas.
- Pitches.
- Apresentações técnicas.

## Quando NÃO usar
- Para apresentações improvisadas.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `objetivo` | string | sim |
| `publico` | string | sim |
| `duracao_minutos` | int | sim |
| `mensagens_chave` | lista | sim |
| `cta` | string | sim |

## Saídas esperadas
- Storyline.
- Slides com título e mensagens.
- Sugestão de visual por slide.
- Slide de fechamento com CTA.

## Fluxo interno
1. Definir objetivo e público.
2. Construir storyline (problema → solução → prova → ação).
3. Detalhar slides (1 ideia por slide).
4. Sugerir visual.
5. Fechar com CTA.

## Limitações
- Não gera PPTX nativo.
- Não cria imagens.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- PowerPoint
- Google Slides
- Keynote
## Secoes de referencia (geradas)

Descricao desta Skill: Use para estruturar apresentações (slides) com storyline claro, slides objetivos e CTA.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

