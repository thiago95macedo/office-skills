---
name: escopo-tecnico
description: Use para descrever serviços com clareza técnica — atividades, entregas, premissas, exclusões, responsabilidades.
category: comercial
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - comercial/orcamento
  - comercial/proposta-comercial
version: 0.1.0
status: rascunho
---

# Escopo Técnico

## Objetivo
Documentar o escopo de um serviço com linguagem técnica clara, evitando ambiguidades contratuais.

## Quando usar
- Antes de elaborar orçamento.
- Em propostas técnicas.
- Em contratação de fornecedores.

## Entradas
- `servico` (descrição resumida)
- `atividades` (lista)
- `entregas` (lista)
- `premissas` (lista)
- `exclusoes` (lista)
- `responsabilidades_cliente` (lista)

## Saída
Documento Markdown estruturado com seções nomeadas.

## Boas práticas
- Use verbos no infinitivo nas atividades.
- Liste exclusões explicitamente.
- Declare premissas que afetam o serviço.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para descrever serviços com clareza técnica — atividades, entregas, premissas, exclusões, responsabilidades.

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

