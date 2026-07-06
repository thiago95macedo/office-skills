---
name: analise-planilha
description: Use para analisar planilhas (CSV, Excel) e produzir descrição de dados, tendências, outliers e insights.
category: produtividade
priority: essencial
depends_on:
  - produtividade/extrator-dados
composes_with:
  - gestao/dashboard-executivo
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Análise de Planilha

## Objetivo
Analisar dados tabulares e produzir descrição compreensiva com estatísticas, tendências, outliers e insights acionáveis.

## Quando usar
- Análise exploratória inicial.
- Briefing de indicadores.
- Apoio à decisão.

## Quando NÃO usar
- Para modelagem estatística avançada.
- Para ETL de dados.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `dados` | path | sim |
| `foco` | string | sim |
| `publico` | string | sim |
| `profundidade` | enum | sim |

## Saídas esperadas
- Estatísticas descritivas.
- Tendências.
- Outliers.
- Insights.
- Recomendações.

## Fluxo interno
1. Carregar dados.
2. Validar qualidade.
3. Calcular estatísticas.
4. Identificar tendências e outliers.
5. Listar insights.

## Limitações
- Não realiza modelagem preditiva.
- Não conecta em fontes em tempo real.

## Dependências
- `produtividade/extrator-dados`

## Possíveis integrações
- Excel
- Google Sheets
- Power BI
## Secoes de referencia (geradas)

Descricao desta Skill: Use para analisar planilhas (CSV, Excel) e produzir descrição de dados, tendências, outliers e insights.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

