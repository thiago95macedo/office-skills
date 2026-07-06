---
name: carta-corporativa
description: Use para produzir cartas formais externas (agradecimentos, parcerias, representatividade).
category: administrativo
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with: []
version: 0.1.0
status: rascunho
---

# Carta Corporativa

## Objetivo
Redigir cartas formais externas para diferentes finalidades, mantendo timbre institucional.

## Entradas
- `finalidade` (string)
- `destinatario` (dict)
- `conteudo` (string)

## Saída
Carta com timbre, local/data, vocativo, corpo, fechamento e assinatura.

## Boas práticas
- Formal, cordial.
- Sem marcas de informalidade.
- Data completa.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir cartas formais externas (agradecimentos, parcerias, representatividade).

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

