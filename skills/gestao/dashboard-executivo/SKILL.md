---
name: dashboard-executivo
description: Use para consolidar indicadores em resumo executivo de uma página.
category: gestao
priority: opcional
depends_on:
  - gestao/kpi-okr
  - produtividade/resumo-executivo
composes_with:
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Dashboard Executivo

## Objetivo
Resumir indicadores-chave em formato escaneável para a diretoria.

## Entradas
- `indicadores` (lista)
- `periodo` (string)

## Saída
Tabela resumo + destaques + alertas.

## Boas práticas
- Linguagem executiva.
- Destaques com variação.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para consolidar indicadores em resumo executivo de uma página.

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

