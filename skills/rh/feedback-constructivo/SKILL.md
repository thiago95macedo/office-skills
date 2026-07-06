---
name: feedback-constructivo
description: Use para estruturar feedbacks individuais objetivos, respeitosos e orientados a desenvolvimento.
category: rh
priority: essencial
depends_on: []
composes_with:
  - rh/avaliacao-desempenho
  - rh/onboarding
version: 0.1.0
status: rascunho
---

# Feedback Construtivo

## Objetivo
Estruturar feedback individual com foco em comportamento, impacto e próximo passo, evitando julgamento pessoal.

## Quando usar
- 1:1 periódico.
- Feedback corretivo imediato.
- Reconhecimento.

## Quando NÃO usar
- Para avaliação formal completa (usar `rh/avaliacao-desempenho`).
- Para mediação de conflitos (usar processo mediador).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `colaborador` | string | sim |
| `contexto` | string | sim |
| `comportamento_observado` | string | sim |
| `impacto` | string | sim |
| `tipo` | enum | sim |
| `proximo_passo` | string | sim |

## Saídas esperadas
Mensagem estruturada em:
- Contexto
- Comportamento observado
- Impacto
- Próximo passo combinado
- Apoio do gestor

## Fluxo interno
1. Descrever comportamento (fato, não julgamento).
2. Descrever impacto (no time/cliente/resultado).
3. Sugerir próximo passo.
4. Indicar apoio.

## Boas práticas
- Linguagem direta e respeitosa.
- Foco em comportamento, não em pessoa.
- Sem comparação com outros.

## Limitações
- Não substitui conversa presencial.

## Possíveis integrações
- 1:1 docs
- Sistema de avaliação
## Secoes de referencia (geradas)

Descricao desta Skill: Use para estruturar feedbacks individuais objetivos, respeitosos e orientados a desenvolvimento.

## Dependências

Apontar Skills que esta Skill depende.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

