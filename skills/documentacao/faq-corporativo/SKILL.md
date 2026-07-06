---
name: faq-corporativo
description: Use para construir FAQ interno ou externo, com perguntas claras, respostas precisas e referência a responsável.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - suporte/faq-tecnico
  - atendimento/triagem-mensagens
version: 0.1.0
status: rascunho
---

# FAQ Corporativo

## Objetivo
Organizar perguntas frequentes com respostas consistentes e responsáveis.

## Entradas
- `perguntas_respostas` (lista)
- `audiencia` (enum)
- `tema` (string)

## Saída
FAQ agrupado por tema, com referência a responsável quando aplicável.

## Boas práticas
- Linguagem clara.
- Evidência técnica quando relevante.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para construir FAQ interno ou externo, com perguntas claras, respostas precisas e referência a responsável.

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

