---
name: pop-sop
description: Use para criar POP (Procedimento Operacional Padrão) ou SOP (Standard Operating Procedure) auditável, com objetivo, escopo, responsabilidades, materiais, procedimento, registros.
category: documentacao
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - documentacao/checklist
  - documentacao/manual-tecnico
  - gestao/plano-acao
version: 0.2.0
status: estavel
references:
  - ISO 9001:2015 — Sistema de Gestão da Qualidade.
  - GMP (Good Manufacturing Practice) — EU GMP Annex 15 / FDA 21 CFR Part 11.
  - Gawande, A. The Checklist Manifesto. 2009.
  - ISO/IEC 27001:2022 — Anexo A.5.37 Procedures for documented information.
---

# POP / SOP

## Objetivo
Gerar procedimento operacional padrão (POP) ou instrução de trabalho auditável, pronto para aprovação em sistema de gestão da qualidade (ISO 9001, GMP, ISO 27001).

## Quando usar
- Criação de procedimento para rotina crítica ou repetitiva.
- Padronização de prática que será replicada em múltiplos turnos ou unidades.
- Atendimento a requisito regulatório (ANVISA, BACEN, ANATEL, ISO).
- Prevenção de não-conformidade em auditoria.
- Treinamento de novos colaboradores em processo crítico.

## Quando NÃO usar
- Para instrução técnica de equipamento (usar `manual-tecnico`).
- Para política ou diretriz de alto nível (usar documento normativo separado).
- Para checklist pontual sem narrativa (usar `checklist`).

## Estrutura padrão recomendada (ISO + GMP)

| Seção | Conteúdo | Observação |
|-------|----------|------------|
| **Cabeçalho** | Logo, código (POP-XXX-NN), versão, data, área | Controle de versão |
| **Aprovação** | Nome, cargo, data, assinatura dos aprovadores | Trilha de aprovação |
| **1. Objetivo** | Finalidade do procedimento | Verbo no infinitivo |
| **2. Aplicabilidade / Escopo** | Onde se aplica, onde não se aplica | Limites claros |
| **3. Definições e siglas** | Termos técnicos e siglas | Glossário |
| **4. Responsabilidades** | Quem faz o quê (RACI resumido) | Nominais |
| **5. Materiais / Recursos** | Insumos, ferramentas, sistemas | Lista verificável |
| **6. Pré-requisitos** | Condições anteriores necessárias | Treinamento, autorizações |
| **7. Procedimento** | Etapas numeradas com verbos no infinitivo | Núcleo do POP |
| **8. Pontos críticos e controles** | Etapas que exigem verificação extra | 🔴 no documento |
| **9. Registros** | Onde o que é registrado, retenção | Conformidade |
| **10. Indicadores** | Como o POP é medido | Eficácia |
| **11. Não-conformidades** | O que fazer se algo sair do padrão | Ação corretiva |
| **12. Referências** | Normas, POPs relacionados, versões anteriores | Trilha |
| **13. Histórico de revisões** | Tabela de mudanças | Auditoria |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `titulo` | string | sim | Nome do procedimento |
| `objetivo` | string | sim | Finalidade em 1-2 frases |
| `escopo` | string | sim | Aplicabilidade |
| `responsaveis` | lista | sim | Papéis e nomes |
| `materiais` | lista | sim | Insumos, ferramentas, sistemas |
| `etapas` | lista | sim | Passos numerados |
| `registros` | lista | sim | O que é registrado e onde |
| `referencias` | lista | não | Normas e POPs relacionados |
| `codigo` | string | não | Código interno (ex: POP-COM-007) |
| `area` | string | sim | Área emissora |

## Saídas esperadas
POP completo em Markdown com cabeçalho de versionamento, controle de aprovação, 13 seções padrão e pontos críticos destacados.

## Fluxo interno
1. Carregar `config/empresa.yaml` para tom e formato.
2. Receber título, objetivo, escopo e área.
3. Listar responsabilidades nominais (papel + pessoa).
4. Detalhar materiais e pré-requisitos (verificáveis).
5. Redigir etapas com verbos no infinitivo, numeradas.
6. Destacar pontos críticos (ex: verificações, dupla conferência, alarmes).
7. Definir registros, retenção e responsável pelo arquivo.
8. Adicionar indicadores de eficácia do procedimento.
9. Indicar ação em caso de não-conformidade.
10. Incluir referências normativas e histórico de revisões.

## Boas práticas
- Verbos no infinitivo nas etapas ("Conferir", "Registrar", "Aprovar").
- Etapas numeradas; sub-etapas com letras quando necessário.
- Indicadores de conformidade e eficácia ao final.
- Pontos críticos marcados visualmente (🔴 ou ⚠️).
- Cabeçalho com código, versão e data.
- Aprovação nominal e datada.
- Revisão periódica (anual ou bianual) registrada.
- Referência cruzada a POPs relacionados.

## Limitações
- Não substitui análise de risco detalhada (usar `gestao-riscos`).
- Não realiza validação de processo por si só (necessário teste em ambiente real).
- Não cobre desenho do processo (BPMN/fluxograma é entrada complementar).
- Não treina executor (encaminhar para `rh/treinamento-materiais`).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Fechamento mensal contábil
- `02-intermediario.md` — Onboarding de fornecedor crítico
- `03-avancado.md` — Liberação de lote farmacêutico (conceito GMP)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Sistema de Gestão da Qualidade (SGQ)
- GED / ECM (SharePoint, Docuware, TOTVS)
- Ferramentas de BPM (Bizagi, Bonita)
- Controle de treinamento (LMS, Moodle)