---
name: transcricao-tarefas
description: Use para converter transcrição de áudio/vídeo em lista estruturada de tarefas com responsável e prazo.
category: produtividade
priority: recomendada
depends_on:
  - administrativo/ata-reuniao
composes_with:
  - gestao/plano-acao
  - gestao/matriz-5w2h
version: 0.1.0
status: rascunho
---

# Transcrição → Tarefas

## Objetivo
Converter transcrição em lista de tarefas estruturada com responsável, prazo, prioridade e contexto.

## Quando usar
- Reuniões registradas em áudio.
- Entrevistas com cliente.
- Brainstorms gravados.

## Quando NÃO usar
- Para atas formais (usar `administrativo/ata-reuniao`).
- Para áudios longos (>2h) sem segmentação.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `transcricao` | texto | sim |
| `participantes` | lista | sim |
| `contexto` | string | sim |

## Saídas esperadas
- Lista de tarefas com responsável, prazo, prioridade.
- Decisões registradas.
- Pendências em aberto.

## Limitações
- Não transcreve áudio diretamente.

## Dependências
- `administrativo/ata-reuniao`

## Possíveis integrações
- Whisper
- Otter.ai
- Ferramentas de transcrição
## Secoes de referencia (geradas)

Descricao desta Skill: Use para converter transcrição de áudio/vídeo em lista estruturada de tarefas com responsável e prazo.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

