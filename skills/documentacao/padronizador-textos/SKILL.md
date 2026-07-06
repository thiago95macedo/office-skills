---
name: padronizador-textos
description: Use para aplicar padrão da casa (tom, vocabulário, formatação) a textos existentes sem alterar o conteúdo técnico.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
  - _core/configurador-empresa
composes_with:
  - todas as Skills que produzem texto
version: 0.1.0
status: rascunho
---

# Padronizador de Textos

## Objetivo
Revisar textos existentes para alinhar tom, vocabulário e formatação ao padrão da empresa.

## Entradas
- `texto_original` (string)
- `alvos_padronizacao` (lista: tom | vocabulario | formatacao | ortografia)

## Saída
Texto padronizado + lista de alterações aplicadas.

## Boas práticas
- Manter sentido original.
- Sinalizar mudanças estilísticas sem alterar técnica.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para aplicar padrão da casa (tom, vocabulário, formatação) a textos existentes sem alterar o conteúdo técnico.

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

