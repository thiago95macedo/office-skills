---
name: plano-acao
description: Use para estruturar plano de ação com responsáveis, prazos, entregas e indicadores.
category: gestao
priority: essencial
depends_on: []
composes_with:
  - gestao/matriz-5w2h
  - gestao/cronograma-projeto
  - gestao/kpi-okr
version: 0.1.0
status: rascunho
---

# Plano de Ação

## Objetivo
Estruturar plano com ações, responsáveis, prazos, entregas e indicadores de sucesso.

## Entradas
- `objetivo` (string)
- `acoes` (lista)
- `responsaveis` (lista)
- `prazos` (lista)
- `indicadores` (lista)

## Saída
Tabela com colunas: Ação | Responsável | Prazo | Entrega | Indicador.

## Boas práticas
- Ações verificáveis.
- Prazo específico.
- Responsável nominal.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para estruturar plano de ação com responsáveis, prazos, entregas e indicadores.

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

