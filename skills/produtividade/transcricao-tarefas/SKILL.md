---
name: transcricao-tarefas
description: Use para converter transcrição de áudio/vídeo em lista estruturada de tarefas com responsável, prazo e prioridade.
category: produtividade
priority: recomendada
depends_on:
  - administrativo/ata-reuniao
composes_with:
  - gestao/plano-acao
  - gestao/matriz-5w2h
version: 0.2.0
status: estavel
references:
  - Modelo SMART — Doran 1981.
  - PMBOK Guide. 8. ed. 2025 (Work Breakdown Structure).
  - Atlassian Confluence — Action Items Template.
  - LGPD Lei 13.709/2018 (cuidado com dados pessoais em transcrição).
---

# Transcrição → Tarefas

## Objetivo
Converter transcrição (reunião, entrevista, brainstorm, podcast) em lista estruturada de tarefas com responsável, prazo, prioridade e contexto, separando decisões e pendências.

## Quando usar
- Reuniões registradas em áudio/vídeo (Teams, Zoom, Meet).
- Entrevistas com cliente, usuário ou especialista.
- Brainstorms gravados (presencial ou remoto).
- Palestras ou treinamentos gravados.
- Episódios de podcast relevantes.

## Quando NÃO usar
- Para atas formais (usar `administrativo/ata-reuniao`).
- Para áudios longos (>2h) sem segmentação.
- Para transcrições jurídicas (usar transcrição oficial).
- Para podcasts com propriedade intelectual (respeitar copyright).

## Estrutura recomendada de saída

| Seção | Conteúdo |
|-------|----------|
| **Cabeçalho** | Fonte, data, duração, participantes |
| **Resumo** | 3-5 bullets do que foi discutido |
| **Decisões** | Frases declarativas |
| **Tarefas** | Tabela numerada: ação, responsável, prazo, prioridade |
| **Pendências** | Itens sem dono definido |
| **Citações relevantes** | Frases literais dignas de nota |
| **Observações** | Premissas, alertas, contexto adicional |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `transcricao` | texto | sim | Texto transcrito (Whisper, Otter, Voxygen, etc.) |
| `participantes` | lista | sim | Quem estava presente (com nome e papel) |
| `contexto` | string | sim | Tipo de reunião/evento e objetivo |
| `idioma` | enum | sim | pt-BR (padrão) |
| `granularidade` | enum | sim | detalhada (toda frase) / sintetica (apenas ações) |

## Saídas esperadas
- Lista de tarefas com responsável, prazo, prioridade.
- Decisões registradas em frases declarativas.
- Pendências em aberto (sem dono definido).
- Citações relevantes (literais).
- Alerta LGPD se houver dados sensíveis.

## Fluxo interno
1. Receber transcrição e contexto.
2. Identificar falas por participante (quando marcado).
3. Extrair decisões explícitas ("decidido que...").
4. Extrair ações implícitas ("vou enviar X", "você pode verificar Y").
5. Atribuir responsável a cada ação (nome ou papel).
6. Inferir prazo quando explícito ("até sexta", "próxima semana").
7. Calcular prioridade (urgência × importância).
8. Listar pendências (sem dono).
9. Sinalizar dados sensíveis (LGPD).

## Boas práticas
- **Granularidade calibrada** — detalhada para tarefas, sintética para overview.
- **Decisões em destaque** — separadamente das tarefas.
- **Tarefas SMART** — verbo no infinitivo + responsável + prazo + critério.
- **Pendências visíveis** — não perder o que ficou em aberto.
- **Citação literal quando relevante** — preserva nuance.
- **Contexto suficiente** — para executar a tarefa sem ouvir o áudio.
- **LGPD** — anonimizar ou omitir dados sensíveis em distribuição.
- **Inferir com cuidado** — quando ambíguo, marcar como "a confirmar".
- **Validar com participantes** — antes de considerar definitiva.
- **Link para fonte** — arquivo de áudio/vídeo original.

## Armadilhas comuns
- Listar tudo como tarefa (sem filtrar o que é tarefa vs. contexto).
- Tarefas sem responsável ("alguém vai ver").
- Tarefas sem prazo ("em breve").
- Decisões misturadas com debate (sem destaque).
- Ignorar pendências (perde rastreabilidade).
- Reproduzir literalmente dados sensíveis (viola LGPD).
- Inferir responsável errado (atribuir a quem não estava).
- Não validar com participantes (interpretação divergente).

## Limitações
- Não transcreve áudio diretamente (depende de ferramenta externa).
- Não detecta sarcasmo ou ironia.
- Não separa falas por participante (depende de diarização).
- Não mede sentimento ou engajamento.

## Dependências
- `administrativo/ata-reuniao`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Reunião semanal de equipe (1h)
- `02-intermediario.md` — Entrevista com cliente (45 min)
- `03-avancado.md` — Brainstorm estratégico (3h) com múltiplos tracks

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Transcrição (Whisper, Voxygen, Otter.ai, Tactiq)
- Reuniões (Microsoft Teams, Zoom, Google Meet)
- Gestão de tarefas (Asana, Trello, Jira)
- Documentação (Notion, Confluence)