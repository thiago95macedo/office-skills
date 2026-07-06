---
name: pop-sop
description: Use para criar POP (Procedimento Operacional Padrão) ou SOP auditável, com objetivo, escopo, responsabilidades, materiais, procedimento, registros.
category: documentacao
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - documentacao/checklist
  - documentacao/manual-tecnico
version: 0.1.0
status: rascunho
---

# POP / SOP

## Objetivo
Gerar procedimento operacional padrão auditável, pronto para aprovação em sistema de qualidade.

## Entradas
- `titulo` (string)
- `objetivo` (string)
- `escopo` (string)
- `responsaveis` (lista)
- `materiais` (lista)
- `etapas` (lista)
- `registros` (lista)
- `referencias` (lista)

## Saída
POP completo com cabeçalho de versionamento e numeração.

## Boas práticas
- Verbos no infinitivo.
- Etapas numeradas.
- Indicadores de conformidade ao final.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para criar POP (Procedimento Operacional Padrão) ou SOP auditável, com objetivo, escopo, responsabilidades, materiais, procedimento, registros.

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

