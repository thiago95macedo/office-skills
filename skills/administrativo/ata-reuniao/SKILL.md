---
name: ata-reuniao
description: Use para documentar reunião em ata estruturada (participantes, pauta, decisões, ações, próxima reunião).
category: administrativo
priority: essencial
depends_on:
  - _core/organizador-informacao
composes_with:
  - gestao/plano-acao
  - produtividade/transcricao-tarefas
version: 0.1.0
status: rascunho
---

# Ata de Reunião

## Objetivo
Documentar formalmente os assuntos tratados em reunião, garantindo rastreabilidade das decisões.

## Entradas
- `notas_reuniao` (string)
- `participantes` (lista)
- `data_hora_local` (dict)

## Saída
Ata com: cabeçalho, participantes, pauta, discussões, decisões, ações, próxima reunião, assinaturas.

## Boas práticas
- Decisões em frases declarativas.
- Ações com responsável e prazo.
- Próxima reunião com data confirmada.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para documentar reunião em ata estruturada (participantes, pauta, decisões, ações, próxima reunião).

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

