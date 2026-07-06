---
name: treinamento-materiais
description: Use para produzir materiais de treinamento (apostila, roteiro, exercícios, avaliação).
category: rh
priority: opcional
depends_on:
  - _core/redator-corporativo
  - documentacao/manual-tecnico
composes_with:
  - rh/onboarding
version: 0.1.0
status: rascunho
---

# Treinamento — Materiais

## Objetivo
Produzir materiais didáticos completos para treinamentos internos, com teoria, prática e avaliação.

## Quando usar
- Programa de integração.
- Capacitação técnica.
- Atualização regulatória.

## Quando NÃO usar
- Para treinamento externo (usar `marketing/conteudo-site` ou fornecedor).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `tema` | string | sim |
| `publico` | string | sim |
| `duracao` | string | sim |
| `objetivos_aprendizagem` | lista | sim |
| `conteudo` | dict | sim |
| `avaliacao` | dict | não |

## Saídas esperadas
- Roteiro do instrutor.
- Material do aluno (apostila/slides).
- Exercícios práticos.
- Avaliação de aprendizagem.

## Fluxo interno
1. Definir objetivos mensuráveis.
2. Estruturar conteúdo em módulos.
3. Elaborar exercícios.
4. Criar avaliação.

## Boas práticas
- Objetivos mensuráveis.
- Exercícios baseados em cenários reais.
- Avaliação alinhada aos objetivos.

## Limitações
- Não cria vídeos.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- LMS
- PowerPoint
- Google Slides
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir materiais de treinamento (apostila, roteiro, exercícios, avaliação).

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

