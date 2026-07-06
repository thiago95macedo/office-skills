---
name: checklist
description: Use para criar listas de verificação aplicáveis a rotinas críticas (auditoria, manutenção, onboarding, fechamento mensal).
category: documentacao
priority: essencial
depends_on: []
composes_with:
  - documentacao/pop-sop
  - gestao/plano-acao
version: 0.1.0
status: rascunho
---

# Checklist

## Objetivo
Criar listas de verificação operacionais, com itens objetivos, agrupados por categoria, marcando ponto crítico quando aplicável.

## Entradas
- `finalidade` (string)
- `itens` (lista)
- `agrupamento` (dict, opcional)

## Saída
Checklist Markdown com checkboxes, categorias e campo de responsável.

## Boas práticas
- Itens curtos e verificáveis.
- Ordem lógica.
- Itens críticos destacados.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para criar listas de verificação aplicáveis a rotinas críticas (auditoria, manutenção, onboarding, fechamento mensal).

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

