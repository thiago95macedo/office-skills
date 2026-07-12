---
name: kpi-okr
description: Use para definir KPIs (Key Performance Indicators) operacionais e OKRs (Objectives and Key Results) estratégicos em área ou projeto.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/dashboard-executivo
  - gestao/plano-acao
  - gestao/matriz-5w2h
version: 0.2.0
status: estavel
references:
  - Kaplan, R.; Norton, D. The Balanced Scorecard. 1996.
  - Doerr, J. Measure What Matters. 2018.
  - Grove, A. High Output Management. 1983.
  - Parmenter, D. Key Performance Indicators. 2015.
---

# KPI / OKR

## Objetivo
Definir, distinguir e estruturar indicadores operacionais (KPIs) e objetivos estratégicos com resultados-chave (OKRs) de forma mensurável, auditável e acionável.

## Quando usar
- Início de ciclo (trimestral, semestral, anual) que precisa de metas mensuráveis.
- Repactuação de metas após desvio significativo.
- Construção ou revisão de dashboard executivo.
- Tradução de objetivo estratégico em entregas operacionais.

## Quando NÃO usar
- Para metas individuais sem contexto estratégico (usar PDI ou gestão por competências).
- Para diagnóstico de causa (usar Ishikawa / 5 Porquês).
- Para projetos pontuais (usar `plano-acao` ou `matriz-5w2h`).

## Distinção fundamental: KPI vs OKR

| Aspecto | KPI | OKR |
|---------|-----|-----|
| Finalidade | Medir performance operacional | Direcionar mudança e foco |
| Horizonte | Contínuo (mensal/trimestral) | Ciclo curto (trimestral padrão) |
| Atingimento | Espera-se manter ou melhorar | Espera-se 0.6–0.7 (100% = subdimensionado) |
| Cadência | Reporting contínuo | Check-ins e revisão de ciclo |
| Audiência | Operacional e tática | Estratégica |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo_estrategico` | string | sim | Declaração qualitativa do objetivo |
| `metas_trimestrais` | lista | sim | Metas de ciclo (1-3 por objetivo) |
| `indicadores` | lista | sim | KPIs propostos com métrica e meta |
| `baseline` | dict | não | Valor de partida para cada KPI |
| `fonte_dados` | dict | não | Onde cada KPI é coletado |
| `responsaveis` | lista | sim | Donos nominais |

## Saídas esperadas
1. Tabela de **KPIs** com colunas: indicador, fórmula, meta, frequência, fonte, dono.
2. Tabela de **OKRs** com colunas: objetivo, KRs, baseline, meta, status.
3. Observações sobre premissas e limitações dos indicadores.

## Fluxo interno
1. Receber objetivo estratégico.
2. Para cada objetivo, decompor em 2–5 Key Results mensuráveis (SMART).
3. Para cada KR ou área operacional, definir KPIs contínuos de acompanhamento.
4. Validar que cada indicador tem fórmula, meta, frequência e dono.
5. Sinalizar indicadores com fragilidade de fonte de dados.
6. Encaminhar para `dashboard-executivo` quando aplicável.

## Boas práticas (KPI)
- SMART: específico, mensurável, atingível, relevante, temporal.
- Poucos indicadores por área (regra 5±2 de Miller).
- Fórmula explícita e documentada.
- Frequência clara de apuração.
- Meta agressiva mas factível.
- Linha de base (baseline) registrada.

## Boas práticas (OKR)
- Objectives qualitativos, inspiradores e memoráveis.
- KRs quantitativos, agressivos e verificáveis.
- 0.6–0.7 de atingimento = excelente (escala Google).
- Máximo 3–5 OKRs por equipe por ciclo.
- Separar committed OKRs (100%) de aspirational (60–70% OK).
- Check-in semanal ou quinzenal.

## Limitações
- Não acessa dados em tempo real (depende de integração com fontes).
- Não substitui plano estratégico detalhado.
- Pode gerar comportamento inadequado se mal desenhado (Goodhart's Law).
- Não cobre indicadores não-financeiros de cultura e clima sem ajuste.

## Dependências
- Nenhuma direta (mas `gestao/plano-acao` é o consumidor típico)

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — KPIs de atendimento ao cliente
- `02-intermediario.md` — OKRs trimestrais de equipe comercial
- `03-avancado.md` — Mix KPI + OKR para diretoria

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- BI (Power BI, Tableau, Looker)
- Planilhas Google / Excel
- Ferramentas de OKR (Weekdone, Perdoo, Gtmhub)
- CRM e ERP como fontes de dados