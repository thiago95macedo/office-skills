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
  - rh/onboarding
version: 0.2.0
status: estavel
references:
  - Chiavenato, I. Gestão de Pessoas. 4. ed. 2014.
  - Dutra, J. S. Competências: conceitos, instrumentos e aplicações. 2017.
  - BRASIL. CLT art. 469 e seguintes — Poder de direção do empregador.
  - 9-Box Grid — origem em 1970s (McKinsey/EXEC).
---

# Avaliação de Desempenho

## Objetivo
Estruturar ciclo avaliativo com critérios objetivos, evidências datadas, comparação de autoavaliação e avaliação do gestor, e Plano de Desenvolvimento Individual (PDI).

## Quando usar
- Ciclo anual ou semestral de avaliação.
- Avaliação de programa de trainee/estágio.
- Repactuação de PDI em meio de ciclo.
- Avaliação de desligamento (entrada/saída).
- Sucessão e planos de carreira (9-box).

## Quando NÃO usar
- Para feedback pontual imediato (usar `rh/feedback-constructivo`).
- Para demissão por justa causa (processo distinto, jurídico).
- Para reajuste salarial isolado (processo de remuneração à parte).

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Ciclo, colaborador, cargo, gestor, data |
| 2 | **Resumo do ciclo** | Período, contexto, entregas principais |
| 3 | **Critérios** | Competências técnicas e comportamentais |
| 4 | **Autoavaliação** | Percepção do colaborador (com evidências) |
| 5 | **Avaliação do gestor** | Visão gerencial (com evidências) |
| 6 | **Calibração** | Comparação entre pares (mesma função/nível) |
| 7 | **Pontos fortes** | Onde o colaborador brilha |
| 8 | **Oportunidades** | Onde pode crescer |
| 9 | **Notas finais** | Nota geral ou por critério (escala definida) |
| 10 | **PDI** | Plano de Desenvolvimento Individual (curto e médio prazo) |
| 11 | **Próxima conversa** | Data combinada e pauta |
| 12 | **Aprovações** | Gestor, RH, colaborador (ciência) |

## Frameworks reconhecidos

| Framework | Aplicação |
|-----------|-----------|
| **9-Box Grid** | Mapeamento de performance × potencial (sucessão) |
| **Avaliação 360°** | Feedback de múltiplas fontes (pares, subordinados, clientes) |
| **BARS** (Behaviorally Anchored Rating Scales) | Escala ancorada em comportamentos específicos |
| **OKR** | Resultados mensuráveis do ciclo |
| **Avaliação por competências** | Técnicas + comportamentais |
| **Avaliação por objetivos (MBO)** | Resultados vs metas |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `colaborador` | dict | sim | Nome, cargo, área, gestor |
| `ciclo` | string | sim | Identificação do ciclo (AAAA.S1, AAAA) |
| `criterios` | lista | sim | Critérios técnicos e comportamentais |
| `evidencias` | lista | sim | Fatos datados de cada critério |
| `autoavaliacao` | dict | sim | Notas e comentários do colaborador |
| `avaliacao_gestor` | dict | sim | Notas e comentários do gestor |
| `feedback_pares` | lista | não | Avaliação 360° (quando aplicável) |
| `metas_ciclo` | lista | sim | OKRs ou metas do ciclo |
| `notas_anteriores` | dict | não | Histórico do colaborador |

## Saídas esperadas
- Cabeçalho com metadados.
- Resumo do ciclo.
- Tabela de critérios com autoavaliação, avaliação do gestor e calibração.
- Pontos fortes e oportunidades.
- PDI estruturado (curto prazo 90 dias / médio prazo 12 meses).
- Próxima conversa agendada.
- Aprovações.

## Fluxo interno
1. Carregar `config/empresa.yaml` (critérios padrão, escala).
2. Receber dados do colaborador, ciclo, metas e critérios.
3. Listar evidências datadas por critério (eventos, entregas, comportamentos).
4. Compilar autoavaliação do colaborador.
5. Compilar avaliação do gestor com base em evidências.
6. Realizar calibração (quando houver conselho de calibração).
7. Listar pontos fortes e oportunidades.
8. Construir PDI com metas SMART (curto prazo + médio prazo).
9. Definir data da próxima conversa de acompanhamento.
10. Submeter para revisão do RH e ciência do colaborador.

## Boas práticas
- **Critérios objetivos** — mensuráveis e verificáveis.
- **Evidências datadas** — fatos, não impressões.
- **Comparação entre pares** — calibração contra o mesmo nível/função.
- **PDI com metas SMART** — específico, mensurável, atingível, relevante, temporal.
- **Pontos fortes + oportunidades** — equilíbrio (não só defeitos).
- **Conversa presencial** — não apenas papel.
- **Registro no sistema** — auditoria e continuidade.
- **Frequência regular** — semestral mínimo, ideal trimestral.
- **Linguagem respeitosa** — fato, não julgamento.
- **Foco em comportamento** — não em pessoa.
- **Continuidade** — PDI vinculado ao próximo ciclo.
- **Sigilo LGPD** — dados sensíveis tratados com base legal.

## Armadilhas comuns
- Avaliação por "achismo" — sem evidências.
- Viés de recência — só lembrar do último mês.
- Viés de halo — uma característica boa influencia todas as outras.
- Viés de centralidade — todos recebem nota média.
- Comparação entre pessoas — avaliação deve ser contra critérios.
- Feedback só negativo — desmotiva.
- PDI genérico ("aprimorar competências") — sem ação específica.
- Sem acompanhamento — PDI fica no papel.
- Misturar avaliação com reajuste salarial.
- Surpresa na avaliação final — sem feedback contínuo.
- Falta de ciência do colaborador (sem assinatura ou aceite).
- Sigilo violado — compartilhar resultados com colegas.

## Limitações
- Não substitui decisão final do gestor.
- Não automatiza calibração entre gestores.
- Não acessa dados de outros sistemas (CRM, ERP) automaticamente.
- Não substitui plano de cargos e salários.
- Não é instrumento jurídico para dispensa (usar processo adequado).

## Dependências
- `rh/feedback-constructivo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Avaliação anual de analista
- `02-intermediario.md` — Avaliação com 360° + PDI
- `03-avancado.md` — Avaliação para sucessão (9-box)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- HRIS (TOTVS RM, Senior, Pontotel, Sólides)
- Ferramentas de OKR (Weekdone, Perdoo)
- LMS (moodle corporativo)
- Plataforma de pesquisa de clima (Pulse, Satisfação)