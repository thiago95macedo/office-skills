---
name: orcamento-empresarial
description: Use para planejar e acompanhar receitas, despesas e investimentos por período (mensal, trimestral ou anual).
category: financeiro
priority: recomendada
depends_on: []
composes_with:
  - gestao/kpi-okr
  - gestao/dashboard-executivo
  - financeiro/analise-custos
  - financeiro/prestacao-contas
version: 0.2.0
status: estavel
references:
  - Horngren, C.; Datar, S.; Rajan, M. Cost Accounting: A Managerial Emphasis. 2018.
  - Drury, C. Management and Cost Accounting. 2021.
  - Hope, J.; Fraser, R. Beyond Budgeting. 2003.
  - CFO Brasil. Manual de Orçamento Empresarial. 2019.
---

# Orçamento Empresarial

## Objetivo
Planejar receitas, despesas e investimentos por período, comparar previsto vs realizado, identificar desvios e apoiar decisões gerenciais orientadas a dados.

## Quando usar
- Planejamento anual ou trimestral.
- Revisões orçamentárias (rolling forecast).
- Acompanhamento mensal com análise de variações.
- Apresentação para diretoria, conselho ou investidores.
- Cenário "what-if" para tomada de decisão.

## Quando NÃO usar
- Para orçamento de um único projeto ou serviço (usar `comercial/orcamento`).
- Para análise de custos de um item específico (usar `financeiro/analise-custos`).
- Para fluxo de caixa operacional (usar sistema de tesouraria/ERP).
- Para balanço patrimonial ou DRE (usar sistema contábil).

## Tipos de orçamento

| Tipo | Característica | Quando usar |
|------|----------------|-------------|
| **Estático** | Fixado no início do período, sem revisões | Empresas estáveis, ambientes previsíveis |
| **Flexível** | Ajusta-se ao volume real | Empresas com sazonalidade, manufatura |
| **Base zero (ZBB)** | Justifica-se do zero a cada ciclo | Áreas com custos discricionários |
| **Rolling forecast** | Atualização contínua (ex: 12 meses à frente) | Ambientes voláteis, startups |
| **Por atividades (ABB)** | Baseado em atividades e drivers | Visão de eficiência operacional |
| **Beyond Budgeting** | Indicadores relativos e adaptabilidade | Empresas maduras em gestão |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Período, área, responsável, data de emissão |
| 2 | **Premissas** | Inflação, câmbio, volume, premissas macroeconômicas |
| 3 | **Receitas** | Previsto por categoria, fonte, mês, valor |
| 4 | **Despesas operacionais** | Pessoal, marketing, administrativo, tecnologia, vendas |
| 5 | **Investimentos (CAPEX)** | Aquisições, infraestrutura, P&D |
| 6 | **Resumo** | Total previsto, realizado, variação absoluta e % |
| 7 | **Cenários** | Conservador, base, otimista |
| 8 | **Análise de desvios** | Justificativa para variações > 10% |
| 9 | **Riscos e oportunidades** | Itens que podem afetar o orçamento |
| 10 | **Aprovação** | Responsável, controlador, CFO, CEO |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `periodo` | string | sim | Período coberto (AAAA-QX, AAAA-MM, AAAA) |
| `tipo_orcamento` | enum | sim | estatico / flexivel / base-zero / rolling / atividades / beyond |
| `receitas_previstas` | dict | sim | Receitas por categoria e mês |
| `despesas_previstas` | dict | sim | Despesas por categoria e mês |
| `investimentos` | dict | sim | CAPEX por item, valor, data |
| `realizado` | dict | não | Valores efetivamente realizados (para acompanhamento) |
| `cenarios` | lista | não | Premissas por cenário (conservador/base/agressivo) |
| `premissas_macroeconomicas` | dict | não | Inflação, câmbio, volume, IPCA |
| `aprovador` | string | sim | Quem aprova o orçamento |

## Saídas esperadas
- Cabeçalho com metadados do orçamento.
- Tabela por categoria (receitas, despesas, investimentos) com previsto/realizado.
- Subtotais por área, por mês, por categoria.
- Variações percentuais e absolutas.
- Alertas de desvios significativos.
- Premissas macroeconômicas e do negócio.
- Análise de desvios (> 10% com justificativa).
- Cenários quando o ambiente for incerto.

## Fluxo interno
1. Receber período, tipo e estrutura do orçamento.
2. Validar categorização consistente com histórico (evitar recategorizações).
3. Listar premissas macroeconômicas (inflação, câmbio, volume).
4. Estruturar receitas por categoria e mês (granularidade por driver).
5. Estruturar despesas por categoria e mês.
6. Listar investimentos (CAPEX) com data prevista.
7. Calcular totais e subtotais.
8. Quando houver `realizado`, calcular variações.
9. Sinalizar desvios > 10% (ou conforme política) para análise.
10. Construir cenários (conservador, base, otimista) quando ambiente incerto.
11. Listar riscos e oportunidades.
12. Submeter para aprovação (controladoria, CFO, CEO).

## Boas práticas
- **Categorização estável** entre períodos (evitar renomear categorias).
- **Granularidade suficiente** para análise de variação (por driver).
- **Comentário em variações relevantes** (> 10% ou fora do esperado).
- **Cenários** quando o ambiente for incerto (mín. 3 cenários).
- **Premissas explícitas** (inflação, câmbio, volume) — não deixar subentendido.
- **Separação CAPEX vs OPEX** (investimento vs operação).
- **Revisões periódicas** (mensal ou trimestral) com forecast atualizado.
- **Análise por exceção** (foco em desvios relevantes, não em tudo).
- **Aprovação antes de execução** (controladoria + CFO).
- **Comparação ano a ano** (YoY) quando houver histórico.
- **Não confundir receita com recebimento** (regime de competência).

## Armadilhas comuns
- Confundir regime de caixa com competência (orçamento em competência).
- Não separar CAPEX de OPEX.
- Categorização instável entre períodos (impossibilita comparação).
- Premissas subentendidas (não documentadas).
- Cenário único (sem análise de sensibilidade).
- Orçamento descolado da estratégia (sem alinhamento com plano).
- Falta de ownership (quem responde por cada categoria).
- Aprovação tardia (depois do início do período).
- Não revisitar o orçamento (estático sem flexibilidade).
- Tratar orçamento como "previsão" e não como "compromisso".

## Limitações
- Não acessa dados de ERP em tempo real (depende de integração).
- Não calcula impostos específicos sem declaração (responsabilidade fiscal).
- Não modela cenários estocásticos complexos (Monte Carlo, etc.).
- Não substitui análise de viabilidade econômico-financeira (VPL, TIR).
- Não realiza projeções de longo prazo (> 5 anos sem revisão estrutural).

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Orçamento mensal de área
- `02-intermediario.md` — Orçamento anual com cenários
- `03-avancado.md` — Rolling forecast trimestral

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- ERP (SAP, TOTVS, Oracle, Microsoft Dynamics)
- BI (Power BI, Tableau, Looker)
- Planilhas (Google Sheets, Microsoft Excel)
- Sistemas FP&A (Adaptive Insights, Anaplan, CCH Tagetik)
- CRM para previsão de receita (Pipedrive, HubSpot, Salesforce)