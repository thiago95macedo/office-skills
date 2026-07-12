---
name: gestao-riscos
description: Use para identificar, classificar e tratar riscos em projeto ou operação.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/plano-acao
  - gestao/cronograma-projeto
  - gestao/matriz-5w2h
version: 0.2.0
status: estavel
references:
  - ISO 31000:2018 — Gestão de Riscos — Diretrizes.
  - PMI. PMBOK Guide. 8. ed. 2025 (8 Performance Domains, incluindo Uncertainty Performance Domain).
  - COSO. Enterprise Risk Management — Integrated Framework. 2017.
  - Hillson, D.; Simon, P. Practical Project Risk Management. 2012.
---

# Gestão de Riscos

## Objetivo
Identificar, analisar, tratar, monitorar e comunicar riscos de projeto ou operação, segundo frameworks reconhecidos (ISO 31000, PMBOK 8, COSO ERM).

## Quando usar
- Início de projeto com duração > 1 mês ou orçamento significativo.
- Decisão estratégica de alto impacto.
- Avaliação de fornecedor, parceiro ou tecnologia crítica.
- Auditoria ou análise de conformidade.
- Revisão periódica de operação contínua.

## Quando NÃO usar
- Para riscos triviais (usar lista simples ou senso comum).
- Para análise de causa raiz de problema já ocorrido (usar 5 Porquês, Ishikawa).
- Para riscos puramente financeiros com modelagem quantitativa (usar `analise-custos`).

## Framework ISO 31000 — Processo

| Etapa | Atividade | Saída |
|-------|-----------|-------|
| 1. **Contexto** | Definir escopo, critérios, stakeholders | Contexto do risco |
| 2. **Identificação** | Listar eventos de risco | Lista de riscos |
| 3. **Análise** | Probabilidade × Impacto (qualitativo ou quantitativo) | Nível de risco |
| 4. **Avaliação** | Comparar com critérios, priorizar | Ranking de riscos |
| 5. **Tratamento** | Mitigar, transferir, evitar, aceitar | Plano de tratamento |
| 6. **Monitoramento** | Acompanhar, revisar, comunicar | Status atualizado |
| 7. **Comunicação** | Reportar a stakeholders | Relatórios |

## Categorias de resposta ao risco

| Resposta | Quando usar | Exemplo |
|----------|-------------|---------|
| **Evitar** (avoid) | Quando o risco é inaceitável | Eliminar a causa do risco |
| **Mitigar** (mitigate) | Quando probabilidade/impacto pode ser reduzido | Plano de contingência |
| **Transferir** (transfer) | Quando há terceiro apto a absorver | Seguro, outsourcing |
| **Aceitar** (accept) | Quando custo de tratar > impacto | Aceitar com plano de contingência |
| **Explorar** (exploit) | Risco positivo (oportunidade) | Aumentar probabilidade |
| **Compartilhar** (share) | Oportunidade com terceiro | Parceria, joint venture |

## Matriz Probabilidade × Impacto

| P×I | Baixo (1) | Médio (2) | Alto (3) | Crítico (4) | Catastrófico (5) |
|-----|-----------|-----------|----------|--------------|-------------------|
| **Quase certo (5)** | 5 | 10 | 15 | 20 | 25 |
| **Provável (4)** | 4 | 8 | 12 | 16 | 20 |
| **Possível (3)** | 3 | 6 | 9 | 12 | 15 |
| **Improvável (2)** | 2 | 4 | 6 | 8 | 10 |
| **Raro (1)** | 1 | 2 | 3 | 4 | 5 |

- **Verde (1-5):** Aceitar com monitoramento.
- **Amarelo (6-12):** Mitigar quando possível.
- **Vermelho (15-25):** Mitigar ativamente ou evitar.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `contexto` | string | sim | Descrição do projeto/operação |
| `criterios_aceitacao` | dict | sim | Apetite a risco (ex: aceitar até 8) |
| `riscos_iniciais` | lista | não | Lista preliminar de riscos |
| `stakeholders` | lista | sim | Partes interessadas |
| `periodo_analise` | string | sim | Janela temporal |
| `fontes_risco` | lista | não | Categorias (mercado, técnico, regulatório, etc.) |

## Saídas esperadas
- Lista de riscos identificados com categoria.
- Matriz Probabilidade × Impacto.
- Nível de risco calculado por evento.
- Estratégia de tratamento por risco.
- Plano de mitigação com responsável, prazo e gatilho.
- Responsável pelo monitoramento.
- Cronograma de revisão.

## Fluxo interno
1. Carregar `config/empresa.yaml` (apetite a risco, tom).
2. Definir contexto (escopo, critérios, stakeholders).
3. Identificar riscos por categoria (técnico, mercado, financeiro, regulatório, operacional, reputacional).
4. Para cada risco: classificar probabilidade (1-5) e impacto (1-5).
5. Calcular nível (P×I).
6. Avaliar contra critérios de aceitação.
7. Definir estratégia de tratamento (evitar/mitigar/transferir/aceitar).
8. Para mitigação: plano com responsável, prazo, gatilho, contingência.
9. Definir responsável e frequência de monitoramento.
10. Estabelecer gatilhos para escalação.

## Boas práticas
- **Identificação ampla** — envolver múltiplos stakeholders.
- **Linguagem direta** — descrever risco como evento + causa + consequência.
- **Riscos positivos** — oportunidades devem ser listadas separadamente.
- **Probabilidade e impacto calibrados** — evitar "tudo é alto".
- **Plano de contingência** — para riscos altos, definir ação se ocorrer.
- **Gatilhos (triggers)** — sinal observável que indica que o risco se materializou.
- **Responsável nominal** — dono do risco e da mitigação.
- **Revisão periódica** — quinzenal ou mensal, conforme volatilidade.
- **Registrar risco residual** — risco após mitigação.
- **Conectar ao orçamento** — provisionar reservas para contingência.
- **Risk register** — manter histórico em arquivo estruturado.

## Limitações
- Não substitui análise quantitativa detalhada (Monte Carlo, árvore de decisão).
- Não cobre riscos puramente financeiros com modelagem estocástica.
- Não garante que o risco se materialize ou não (probabilidade é estimativa).
- Não elimina risco — apenas gerencia.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Risco de projeto de 3 meses
- `02-intermediario.md` — Risco de adoção de nova tecnologia
- `03-avancado.md` — Risco estratégico de internacionalização

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Ferramentas de GRC (ServiceNow GRC, SAP GRC)
- PM software (Jira, Asana, MS Project) com módulo de risco
- Planilhas Google / Excel com templates ISO 31000
- Dashboards (Power BI, Tableau)