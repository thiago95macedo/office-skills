---
name: justificativa-financeira
description: Use para justificar aquisição ou investimento com base em ROI, payback, riscos e impacto no negócio.
category: financeiro
priority: opcional
depends_on:
  - financeiro/analise-custos
composes_with:
  - financeiro/orcamento-empresarial
  - comercial/proposta-comercial
  - gestao/gestao-riscos
version: 0.2.0
status: estavel
references:
  - Brigham, E.; Houston, J. Fundamentals of Financial Management. 2016.
  - Damodaran, A. Investment Valuation. 2012.
  - PMI. PMBOK Guide. 8. ed. 2025.
  - Ross, S.; Westerfield, R.; Jordan, B. Fundamentals of Corporate Finance. 2020.
---

# Justificativa Financeira

## Objetivo
Sustentar tecnicamente decisão de compra, contratação ou investimento com dados financeiros verificáveis, cenários comparativos e análise de risco.

## Quando usar
- Compra de equipamento, sistema ou serviço de alto valor.
- Contratação de fornecedor estratégico (consultoria, software, infraestrutura).
- Investimento em expansão (nova unidade, novo mercado).
- Substituição de sistema legado.
- Apresentação para diretoria, conselho ou comitê de investimentos.

## Quando NÃO usar
- Para compras de baixo valor com aprovação automática (processo simplificado).
- Para investimentos com ROI já aprovado em plano estratégico (apenas referenciar).
- Para análise de viabilidade econômico-financeira detalhada (usar `analise-custos`).

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Resumo executivo** | Recomendação em 1 parágrafo |
| 2 | **Contexto e problema** | Situação atual, dor, oportunidade |
| 3 | **Objeto da proposta** | O que se propõe adquirir/contratar |
| 4 | **Cenário atual vs proposto** | Comparação objetiva |
| 5 | **Benefícios quantificados** | Receitas adicionais, economias, produtividade |
| 6 | **Benefícios qualitativos** | Marca, risco mitigado, experiência do cliente |
| 7 | **Análise financeira** | Investimento, ROI, payback, VPL, TIR (quando aplicável) |
| 8 | **Riscos e mitigação** | Riscos técnicos, financeiros, operacionais |
| 9 | **Alternativas consideradas** | Outras opções rejeitadas com motivo |
| 10 | **Premissas** | Inflação, volume, câmbio, premissas de negócio |
| 11 | **Próximos passos** | Aprovação, cronograma, governança |
| 12 | **Anexos** | Propostas, especificações, contratos, pareceres |

## Indicadores financeiros

| Indicador | Fórmula | Quando usar |
|-----------|---------|-------------|
| **ROI** (Return on Investment) | (Ganho − Investimento) / Investimento × 100% | Comparação rápida de retorno |
| **Payback** | Investimento / Ganho anual | Tempo para recuperar capital |
| **Payback descontado** | Considera valor do dinheiro no tempo | Decisões de longo prazo |
| **VPL** (Valor Presente Líquido) | Σ FC / (1+i)^t − Investimento | Valor criado pelo projeto |
| **TIR** (Taxa Interna de Retorno) | Taxa que torna VPL = 0 | Comparação com custo de capital |
| **TIRM** (TIR modificada) | Ajusta fluxos não convencionais | Projetos com fluxos irregulares |
| **B/C** (Benefício/Custo) | Σ Benefícios / Σ Custos | Análise custo-benefício social |
| **WACC** (custo médio ponderado de capital) | Custo de oportunidade da empresa | Teto mínimo de TIR para projetos |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objeto` | string | sim | Descrição do que será adquirido/contratado |
| `valor_investimento` | number | sim | Valor total do investimento |
| `beneficios_quantificados` | dict | sim | Receitas, economias, produtividade (compremês/ano) |
| `beneficios_qualitativos` | lista | sim | Marca, risco mitigado, experiência do cliente |
| `payback_estimado` | string | sim | Tempo estimado para retorno |
| `riscos` | lista | sim | Riscos técnicos, financeiros, operacionais |
| `mitigacao` | lista | sim | Plano de mitigação por risco |
| `alternativas` | lista | não | Outras opções rejeitadas |
| `premissas` | dict | não | Inflação, volume, câmbio, premissas de negócio |
| `aprovador` | string | sim | Quem aprova (diretoria, conselho) |

## Saídas esperadas
- Resumo executivo com recomendação clara.
- Comparação cenário atual vs proposto.
- Tabela de benefícios quantificados (ganhos mensais/anuais).
- Análise de ROI, payback, VPL, TIR (quando aplicável).
- Lista de riscos com mitigação.
- Alternativas consideradas com motivo de rejeição.
- Premissas macroeconômicas e de negócio.
- Próximos passos e governança.

## Fluxo interno
1. Receber objeto, valor e contexto do investimento.
2. Carregar premissas macroeconômicas (inflação, câmbio, taxa de desconto).
3. Descrever cenário atual (custos, ineficiências, riscos).
4. Descrever cenário proposto (ganhos, melhorias, novas capacidades).
5. Quantificar benefícios (receitas, economia, produtividade) com premissas.
6. Calcular ROI e payback simples.
7. Calcular VPL e TIR (quando aplicável e relevante).
8. Comparar com WACC da empresa (projeto deve superar custo de capital).
9. Listar riscos (técnicos, financeiros, operacionais) com mitigação.
10. Listar alternativas consideradas com motivo de rejeição.
11. Submeter para aprovação (controladoria + CFO + sponsor).

## Boas práticas
- **Benefícios quantificados** sempre que possível (premissas explícitas).
- **Premissas claras** e revisáveis (não "achismo").
- **Comparação com alternativas** (não investir = status quo).
- **Análise de sensibilidade** (cenários otimista/base/pessimista).
- **Riscos com mitigação** (não só listar riscos).
- **VPL e TIR** para projetos de longo prazo (não só payback).
- **Custo de oportunidade** (capital tem custo — comparar com WACC).
- **Aprovação por instância correta** (valor alto → diretoria/conselho).
- **Período de análise coerente** (5 anos para tecnologia, 10+ para infraestrutura).
- **Benefícios intangíveis** explicitamente marcados (não "misturar" com quantificados).
- **Goodhart's Law em mente** (não medir o que se quer melhorar, melhorar o que se mede).

## Armadilhas comuns
- Benefícios superestimados (sem premissa defensável).
- Ignorar custo de oportunidade do capital (projetos abaixo do WACC destróem valor).
- Payback simples em projeto longo (subestima risco).
- Não considerar custos ocultos (treinamento, integração, manutenção).
- Comparação com alternativa inexistente ("fazer nada" raramente é realista).
- Análise única de cenário (sem sensibilidade).
- Benefícios qualitativos contados como quantificados.
- Misturar despesas OPEX com CAPEX sem critério.
- Projeção linear indefinida (sem depreciação ou fim de vida útil).
- Não considerar impostos sobre retorno (quando aplicável).

## Limitações
- Não modela cenários estocásticos complexos (Monte Carlo, árvores de decisão).
- Não calcula VPL/TIR automaticamente em todas as situações (pode citar conceito).
- Não considera custo de oportunidade do capital de forma detalhada.
- Não substitui parecer jurídico sobre contratos.
- Não realiza due diligence de fornecedores.

## Dependências
- `financeiro/analise-custos`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Justificativa de compra de software
- `02-intermediario.md` — Justificativa de equipamento industrial
- `03-avancado.md` — Justificativa de expansão para novo mercado

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- BI (Power BI, Tableau, Looker)
- ERP (SAP, TOTVS, Oracle)
- Planilhas financeiras (Excel, Google Sheets)
- Sistemas FP&A (Adaptive Insights, Anaplan)
- Procurement (Coupa, Ariba)