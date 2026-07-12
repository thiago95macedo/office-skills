---
name: dashboard-executivo
description: Use para consolidar indicadores em resumo executivo de uma página para a diretoria.
category: gestao
priority: opcional
depends_on:
  - gestao/kpi-okr
  - produtividade/resumo-executivo
composes_with:
  - gestao/kpi-okr
  - gestao/plano-acao
version: 0.2.0
status: estavel
references:
  - Few, S. Information Dashboard Design. 2006 / 2. ed. 2013.
  - Tufte, E. The Visual Display of Quantitative Information. 1983.
  - Kaplan, R.; Norton, D. The Balanced Scorecard. 1996.
  - Knaflic, C. Storytelling with Data. 2015.
---

# Dashboard Executivo

## Objetivo
Resumir indicadores-chave em formato escaneável (one-page) para a diretoria, com destaques, variações e alertas que apoiem decisões em segundos.

## Quando usar
- Reunião mensal de diretoria ou conselho.
- Briefing executivo para sponsor.
- Apresentação para investidores.
- Repactuação estratégica (revisão de KPIs e OKRs).
- Tomada de decisão crítica com dados.

## Quando NÃO usar
- Para relatório técnico detalhado (usar `produtividade/resumo-executivo` ou relatório completo).
- Para acompanhamento operacional (usar dashboard operacional, não executivo).
- Para análise exploratória (usar ferramenta de BI).

## Princípios de design (Stephen Few / Edward Tufte / Cole Nussbaumer Knaflic)

| Princípio | Aplicação |
|-----------|-----------|
| **Menos é mais** | 5-7 indicadores, não 30 |
| **Contexto antes do número** | Mostrar variação vs. meta, não só valor absoluto |
| **Sinal-ruído** | Destacar o que mudou, não repetir status quo |
| **Visual encoding correto** | Posição e comprimento > cor e ângulo |
| **Acessibilidade** | Paleta compatível com daltonismo (não só cor) |
| **Hierarquia clara** | Mais importante no topo ou em destaque |
| **Texto limitado** | Rótulos curtos, sem parágrafos |

## Estrutura recomendada (one-pager)

| Bloco | Conteúdo | Tamanho |
|-------|----------|---------|
| **Cabeçalho** | Título, período, data emissão | 1 linha |
| **Destaques** | 3-5 bullets do que mudou e por quê | 1/4 da página |
| **KPIs principais** | 5-7 indicadores com meta e variação | 1/2 da página |
| **OKRs em andamento** | Status dos objetivos do ciclo | 1/4 da página |
| **Riscos e alertas** | Itens que exigem decisão | 1/4 da página |
| **Próximos passos** | Decisões pedidas à diretoria | 1/4 da página |

## Tipos de visualização por métrica

| Tipo de métrica | Visual recomendado |
|------------------|---------------------|
| **Tendência temporal** | Linha com meta destacada |
| **Comparação vs meta** | Bullet chart ou barra com target |
| **Composição** | Stacked bar (horizontal) |
| **Distribuição** | Box plot ou histograma |
| **Correlação** | Scatter plot |
| **Status** | Semáforo (🟢🟡🔴) com legenda |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `periodo` | string | sim | Período coberto (mês, trimestre) |
| `area` | string | sim | Área ou empresa |
| `indicadores` | lista | sim | KPIs com valor atual, meta, baseline |
| `okrs_ciclo` | lista | não | OKRs em andamento com status |
| `destaques` | lista | sim | 3-5 itens relevantes do período |
| `alertas` | lista | não | Riscos, decisões pendentes |
| `proximos_passos` | lista | não | Itens que precisam de decisão |
| `publico` | enum | sim | Diretoria / Conselho / Investidor / Sponsor |

## Saídas esperadas
- Cabeçalho com metadados.
- 3-5 destaques do período.
- 5-7 KPIs principais com valor, meta, variação.
- Status dos OKRs em andamento (quando aplicável).
- Alertas e riscos sinalizados.
- Decisões pedidas à diretoria.
- Sugestão de layout visual (Markdown estruturado).

## Fluxo interno
1. Receber período, área e público-alvo.
2. Selecionar 5-7 KPIs principais (regra 7±2).
3. Para cada KPI, levantar valor atual, meta, baseline, variação.
4. Identificar 3-5 destaques (positivos e negativos).
5. Selecionar status dos OKRs em ciclo (quando aplicável).
6. Listar alertas críticos e decisões pendentes.
7. Aplicar princípio de hierarquia visual.
8. Validar acessibilidade (paleta, contraste, daltonismo).
9. Sugerir layout (cabeçalho → destaques → KPIs → OKRs → alertas → decisões).

## Boas práticas
- **5-7 KPIs** — não sobrecarregar.
- **Contexto antes do número** (meta, variação, baseline).
- **Destaques executivos** — não só números, fatos.
- **Riscos com ação** — alerta + recomendação.
- **Decisões explícitas** — o que a diretoria precisa decidir.
- **Sinalização visual** consistente (cores semânticas: verde/vermelho).
- **Visualização simples** — sem gráficos 3D, sem pie charts (regra de Few).
- **Acessibilidade** — paleta inclusiva, texto descritivo.
- **Frequência definida** — mensal, quinzenal.
- **Comparação** — atual vs. meta vs. período anterior vs. YoY.

## Armadilhas comuns
- Dashboard com 20+ indicadores (sobrecarga cognitiva).
- Apenas números absolutos sem contexto ou variação.
- Pie charts para dados não-compositivos.
- Cores decorativas (vermelho/verde sem significado).
- Sem alertas ou decisões pedidas (status passivo).
- Mesmo dashboard para públicos diferentes (operacional vs. executivo).
- Visualizações interativas para audiência não-técnica.
- Cores sem acessibilidade para daltonismo.

## Limitações
- Não substitui análise aprofundada (é um resumo).
- Não acessa dados em tempo real (depende de integração).
- Não gera insights automáticos (precisa de analista).
- Não substitui dashboard operacional (granularidade diferente).

## Dependências
- `gestao/kpi-okr`
- `produtividade/resumo-executivo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Dashboard mensal comercial
- `02-intermediario.md` — Dashboard trimestral estratégico
- `03-avancado.md` — Dashboard para conselho de administração

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Power BI, Tableau, Looker, Metabase
- Google Data Studio (Looker Studio)
- Planilhas Google / Excel
- CRM (Pipedrive, HubSpot, Salesforce)
- ERP como fonte de dados