---
name: gestao-riscos
description: Use para identificar, classificar e tratar riscos em projeto ou operação.
category: gestao
priority: recomendada
depends_on: []
composes_with:
  - gestao/plano-acao
  - gestao/cronograma-projeto
version: 0.1.0
status: rascunho
---

# Gestão de Riscos

## Objetivo
Identificar riscos, classificá-los por probabilidade e impacto, propor mitigação.

## Entradas
- `contexto` (string)
- `riscos_iniciais` (lista, opcional)

## Saída
Matriz de riscos com probabilidade, impacto, mitigação, responsável.

## Boas práticas
- Linguagem direta.
- Mitigação prática.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para identificar, classificar e tratar riscos em projeto ou operação.

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

