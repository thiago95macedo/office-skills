---
name: one-pager
description: Use para criar resumo executivo de uma página sobre empresa, produto ou serviço.
category: comercial
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-site
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# One-pager

## Objetivo
Sintetizar uma empresa, serviço ou solução em uma única página de alto impacto.

## Entradas
- `assunto` (string)
- `publico` (string)
- `diferenciais` (lista)

## Saída
Markdown de uma página (≤ 500 palavras) com seções objetivas.

## Boas práticas
- Curto, escaneável.
- Foco em valor, não em adjetivos.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para criar resumo executivo de uma página sobre empresa, produto ou serviço.

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

