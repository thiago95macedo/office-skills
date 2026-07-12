---
name: treinamento-materiais
description: Use para produzir materiais didáticos completos para treinamentos internos, com teoria, prática e avaliação.
category: rh
priority: opcional
depends_on:
  - _core/redator-corporativo
  - documentacao/manual-tecnico
composes_with:
  - rh/onboarding
  - rh/feedback-constructivo
  - rh/avaliacao-desempenho
version: 0.2.0
status: estavel
references:
  - Bloom, B. Taxonomy of Educational Objectives. 1956 (Bloom revisada por Anderson 2001).
  - Mager, R. Preparing Instructional Objectives. 1962.
  - ADDIE (Analysis, Design, Development, Implementation, Evaluation) — origem militar 1970s.
  - Chiavenato, I. Treinamento e Desenvolvimento de Pessoas. 2016.
---

# Treinamento — Materiais

## Objetivo
Produzir materiais didáticos completos para treinamentos internos: apostila, roteiro do instrutor, slides, exercícios e avaliação, alinhados a objetivos de aprendizagem mensuráveis.

## Quando usar
- Programa de integração de novos colaboradores.
- Capacitação técnica (nova ferramenta, processo ou tecnologia).
- Atualização regulatória (LGPD, normas técnicas, SOX).
- Desenvolvimento de liderança ou soft skills.
- Reciclagem periódica de procedimentos críticos.

## Quando NÃO usar
- Para treinamento contratado de fornecedor externo.
- Para curso acadêmico formal (usar estrutura de curso).
- Para microlearning (pílulas rápidas) — usar formato próprio.

## Taxonomia de Bloom (revisada por Anderson, 2001)

| Nível | Verbo-exemplo | Aplicação |
|-------|---------------|-----------|
| **Lembrar** | Listar, identificar, nomear | Fatos, conceitos básicos |
| **Entender** | Descrever, explicar, resumir | Compreensão conceitual |
| **Aplicar** | Executar, implementar, usar | Uso prático |
| **Analisar** | Comparar, diferenciar, examinar | Decomposição |
| **Avaliar** | Criticar, justificar, decidir | Julgamento fundamentado |
| **Criar** | Projetar, planejar, produzir | Síntese criativa |

## Modelo ADDIE

| Fase | Atividade | Saída |
|------|-----------|-------|
| **A**nálise | Identificar gap de competência | Diagnóstico de necessidade |
| **D**esign | Estruturar objetivos, conteúdo, avaliação | Plano de treinamento |
| **D**esenvolvimento | Criar materiais, apostilas, exercícios | Conteúdo didático |
| **I**mplementação | Aplicar o treinamento em sala/virtual | Turma realizada |
| **A**valiação | Medir reação, aprendizado, comportamento, resultado | ROI do treinamento (modelo Kirkpatrick) |

## Estrutura recomendada de materiais

| # | Componente | Conteúdo |
|---|------------|----------|
| 1 | **Roteiro do instrutor** | Plano de aula, tempos, dinâmicas, transições |
| 2 | **Apostila / material do aluno** | Conceitos, exemplos, exercícios |
| 3 | **Slides** | Visual de apoio (não substitui apostila) |
| 4 | **Exercícios práticos** | Cenários reais da empresa |
| 5 | **Avaliação de aprendizagem** | Prova, quiz ou exercício final |
| 6 | **Avaliação de reação** | Questionário de satisfação (Kirkpatrick L1) |
| 7 | **Material de apoio** | Links, leituras complementares |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tema` | string | sim | Assunto do treinamento |
| `publico` | string | sim | Perfil do aluno (cargo, senioridade) |
| `duracao` | string | sim | Tempo total (ex: "8h" ou "4 aulas de 2h") |
| `objetivos_aprendizagem` | lista | sim | 3-5 objetivos mensuráveis |
| `conteudo` | dict | sim | Tópicos, conceitos, exemplos |
| `nivel_bloom` | enum | sim | lembrar / entender / aplicar / analisar / avaliar / criar |
| `avaliacao` | dict | não | Tipo de prova ou exercício final |
| `pre_requisitos` | lista | não | Conhecimentos prévios esperados |
| `materiais_complementares` | lista | não | Leituras, vídeos |

## Saídas esperadas
- Roteiro do instrutor (cronograma detalhado).
- Apostila completa (conceitos + exemplos).
- Slides estruturados (títulos, tópicos, imagens).
- Exercícios práticos baseados em cenários.
- Avaliação alinhada aos objetivos.
- Questionário de reação.

## Fluxo interno
1. Definir objetivos mensuráveis (3-5) por nível de Bloom apropriado.
2. Estruturar conteúdo em módulos alinhados aos objetivos.
3. Criar exercícios práticos com cenários reais da empresa.
4. Elaborar avaliação alinhada aos objetivos (mesma cobertura).
5. Produzir slides de apoio visual.
6. Criar roteiro do instrutor com tempos e dinâmicas.
7. Adicionar questionário de reação (L1 Kirkpatrick).
8. Validar com SME (Subject Matter Expert) antes de publicar.

## Boas práticas
- **Objetivos mensuráveis** (verbo de Bloom + objeto + critério).
- **Exercícios baseados em cenários reais** da empresa (não teóricos).
- **Avaliação alinhada aos objetivos** (não avaliar o que não foi ensinado).
- **Engajamento ativo** — não palestra > 20 minutos sem atividade.
- **Microlearning** quando possível — pílulas de 5-10 minutos.
- **Acessibilidade** — legendas, contraste, material para PCD.
- **Prática antes da teoria** — flipped classroom quando aplicável.
- **Espaço seguro** para erros (laboratório simulado).
- **Material de referência** — apostila fica com aluno após o curso.
- **Avaliação posterior** — L2 (aprendizagem), L3 (comportamento), L4 (resultados).
- **Atualização periódica** — revisar conteúdo a cada ciclo.

## Armadilhas comuns
- Objetivos vagos ("entender vendas") — não mensuráveis.
- Conteúdo teórico sem prática — esquecimento rápido.
- Avaliação desconectada dos objetivos — avalia o que não ensinou.
- Material desatualizado (ex: ferramenta nova, não ensinou a antiga).
- Tempo mal dimensionado — apressar conteúdo importante.
- Falta de engajamento (palestra 4h sem pausas ou atividades).
- Sem material de apoio (apto só com slides).
- Sem avaliação de reação — não sabe se foi útil.
- Misturar níveis (iniciante + avançado na mesma turma).
- Esquecer de avaliar pós-treinamento (L2, L3).

## Limitações
- Não cria vídeos nem animações complexas.
- Não substitui instrutor humano.
- Não mede ROI organizacional automaticamente.
- Não acessa LMS automaticamente para publicação.
- Não gera quizzes interativos (apenas conteúdo).

## Dependências
- `_core/redator-corporativo`
- `documentacao/manual-tecnico`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Treinamento de integração (1 dia)
- `02-intermediario.md` — Capacitação técnica (16h)
- `03-avancado.md` — Programa de liderança (40h)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- LMS (Moodle, Docebo, Canvas)
- PowerPoint, Google Slides, Keynote
- Mentimeter, Slido (enquetes interativas)
- Loom, OBS (gravação)
- Google Drive, OneDrive (armazenamento)