---
name: avaliacao-desempenho
description: Use para produzir roteiro completo de avaliação de desempenho (ciclo, critérios, evidências, calibração, PDI).
category: rh
priority: recomendada
depends_on:
  - rh/feedback-constructivo
composes_with:
  - rh/feedback-constructivo
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Avaliação de Desempenho

## Objetivo
Estruturar ciclo avaliativo com critérios objetivos, evidências e plano de desenvolvimento individual.

## Quando usar
- Ciclo anual ou semestral.
- Avaliação de programa de trainee/estágio.
- PDI (Plano de Desenvolvimento Individual).

## Quando NÃO usar
- Para feedback pontual (usar `rh/feedback-constructivo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `colaborador` | dict | sim |
| `ciclo` | string | sim |
| `criterios` | lista | sim |
| `evidencias` | lista | sim |
| `autoavaliacao` | dict | sim |
| `avaliacao_gestor` | dict | sim |

## Saídas esperadas
- Resumo do ciclo.
- Notas por critério (com evidências).
- Pontos fortes e oportunidades.
- PDI (curto prazo e médio prazo).
- Próxima conversa combinada.

## Fluxo interno
1. Listar critérios.
2. Compilar evidências.
3. Cruzar autoavaliação e avaliação do gestor.
4. Listar pontos fortes e oportunidades.
5. Construir PDI com metas SMART.

## Boas práticas
- Critérios objetivos.
- Evidências datadas.
- Comparação apenas contra critérios, não contra pessoas.

## Limitações
- Não substitui decisão final do gestor.

## Dependências
- `rh/feedback-constructivo`

## Possíveis integrações
- HRIS
- 9-box de sucessão
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir roteiro completo de avaliação de desempenho (ciclo, critérios, evidências, calibração, PDI).

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

