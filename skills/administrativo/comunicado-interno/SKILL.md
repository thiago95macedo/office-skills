---
name: comunicado-interno
description: Use para comunicar mudanças, decisões ou fatos relevantes para colaboradores internos.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
version: 0.1.0
status: rascunho
---

# Comunicado Interno

## Objetivo
Informar mudanças ou fatos relevantes à empresa de forma clara, uniforme e rastreável.

## Entradas
- `publico` (string)
- `mensagem_central` (string)
- `tom` (enum)
- `canal` (enum: mural | email | intranet)

## Saída
Comunicado em Markdown pronto para distribuição.

## Boas práticas
- Mensagem única por comunicado.
- O que muda e o que não muda.
- Próximos passos.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para comunicar mudanças, decisões ou fatos relevantes para colaboradores internos.

## Quando usar

Listar situacoes em que a Skill e a ferramenta correta.

## Quando NÃO usar

Listar situacoes em que outra Skill ou processo deve ser usado.

## Entradas esperadas

Documentar campos, tipos e obrigatoriedade.

## Saídas esperadas

Documentar artefatos produzidos pela Skill.

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Limitações

Declarar restricoes conhecidas da Skill.

## Dependências

Apontar Skills que esta Skill depende.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

## Possíveis integrações

Listar integracoes com sistemas externos.

