---
name: analise-planilha
description: Use para analisar planilhas (CSV, Excel, Google Sheets) e produzir descrição com estatísticas, tendências, outliers e insights acionáveis.
category: produtividade
priority: essencial
depends_on:
  - produtividade/extrator-dados
composes_with:
  - gestao/dashboard-executivo
  - gestao/kpi-okr
version: 0.2.0
status: estavel
references:
  - Tufte, E. The Visual Display of Quantitative Information. 1983.
  - Few, S. Information Dashboard Design. 2. ed. 2013.
  - Knaflic, C. Storytelling with Data. 2015.
  - BRASIL. Lei 13.709/2018 — LGPD (cuidado com dados pessoais em planilhas).
---

# Análise de Planilha

## Objetivo
Analisar dados tabulares e produzir descrição compreensiva com estatísticas descritivas, tendências, outliers e insights acionáveis para o público-alvo.

## Quando usar
- Análise exploratória inicial de dados.
- Briefing de indicadores para reunião.
- Apoio à decisão gerencial.
- Validação de hipótese de negócio.
- Preparação de dashboard.

## Quando NÃO usar
- Para modelagem estatística avançada (regressão, ML — usar Python/R).
- Para ETL de dados (usar pipeline dedicado).
- Para dados não estruturados (usar `extrator-dados` antes).

## Estrutura recomendada de análise

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Resumo executivo** | 1 parágrafo com achados principais |
| 2 | **Contexto dos dados** | Origem, período, volumetria, qualidade |
| 3 | **Estatísticas descritivas** | Média, mediana, desvio, mín/máx |
| 4 | **Distribuição** | Como os dados se distribuem |
| 5 | **Tendências** | Evolução no tempo (sazonalidade, direção) |
| 6 | **Outliers** | Pontos fora do padrão e contexto |
| 7 | **Correlações** | Relações entre variáveis (quando aplicável) |
| 8 | **Insights acionáveis** | O que isso significa para o negócio |
| 9 | **Limitações** | Avisos sobre qualidade e cobertura |
| 10 | **Próximos passos** | Análises adicionais sugeridas |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `dados` | path/string | sim | Arquivo CSV/Excel ou conteúdo inline |
| `foco` | string | sim | Pergunta de negócio a responder |
| `publico` | string | sim | Quem vai consumir (diretoria, operacional) |
| `profundidade` | enum | sim | basica / detalhada / tecnica |
| `periodo_referencia` | string | não | Período dos dados |
| `filtros` | dict | não | Segmentações aplicadas |

## Saídas esperadas
- Resumo executivo (5-7 linhas).
- Estatísticas descritivas por coluna.
- Tendências e outliers identificados.
- Insights acionáveis (3-5 bullets).
- Limitações e cuidados (LGPD, qualidade dos dados).
- Próximos passos.

## Fluxo interno
1. Carregar dados do arquivo ou string.
2. Validar qualidade (tipos, nulos, duplicatas).
3. Detectar tipo de cada coluna (numérica, categórica, data).
4. Calcular estatísticas descritivas para numéricas.
5. Identificar outliers (IQR, z-score).
6. Calcular tendências temporais quando houver data.
7. Cruzar com pergunta de negócio.
8. Produzir insights acionáveis.
9. Sinalizar limitações (LGPD quando houver dados pessoais).

## Boas práticas
- **Validação de qualidade primeiro** — não analisar dado sujo.
- **Pergunta de negócio clara** — análise sem objetivo é só estatística.
- **Público-alvo definido** — ajusta nível técnico.
- **Visualização simples** — Tufte: máximo de dados, mínimo de tinta.
- **Outliers com contexto** — explicar por que existem.
- **Comparação com baseline** — atual vs. anterior, atual vs. meta.
- **Sinalizar limitações** — honestidade sobre o dado.
- **LGPD** — anonimizar dados pessoais em relatórios compartilháveis.
- **Conclusão + recomendação** — análise sem ação é inútil.
- **Repetibilidade** — análise deve ser reproduzível (script ou query).

## Armadilhas comuns
- Confundir correlação com causalidade.
- Sem outliers (todo mundo é "normal").
- Análise descritiva sem pergunta de negócio.
- Visualização enganosa (escala truncada).
- Ignorar dados faltantes (missingness pode ser informativa).
- Misturar moedas sem conversão (BRL vs. USD).
- Comparar períodos diferentes sem ajuste (sazonalidade).
- Compartilhar dados pessoais sem tratamento (viola LGPD).

## Limitações
- Não realiza modelagem preditiva ou causal.
- Não conecta em fontes em tempo real.
- Não acessa sistemas externos.
- Não detecta fraude ou anomalias estatísticas avançadas.

## Dependências
- `produtividade/extrator-dados`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Análise exploratória de CSV de vendas
- `02-intermediario.md` — Análise com tendências e outliers
- `03-avancado.md` — Análise para diretoria com insights acionáveis

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Excel, Google Sheets, LibreOffice Calc
- Power BI, Tableau, Looker, Metabase
- Pandas (Python), R, SQL
- Google Data Studio