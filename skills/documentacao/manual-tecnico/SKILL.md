---
name: manual-tecnico
description: Use para produzir manuais técnicos completos (instalação, operação, manutenção) de equipamentos ou sistemas.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
  - documentacao/pop-sop
composes_with:
  - documentacao/checklist
  - rh/treinamento-materiais
version: 0.1.0
status: rascunho
---

# Manual Técnico

## Objetivo
Documentar equipamentos/sistemas com seções padronizadas para uso, manutenção e troubleshooting.

## Entradas
- `equipamento` (string)
- `secoes` (lista)
- `nivel_tecnico` (enum)

## Saída
Manual com sumário, introdução, instalação, operação, manutenção, segurança, anexos.

## Boas práticas
- Diagramas quando possível.
- Linguagem técnica calibrada ao público.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir manuais técnicos completos (instalação, operação, manutenção) de equipamentos ou sistemas.

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

