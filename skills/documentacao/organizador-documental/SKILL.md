---
name: organizador-documental
description: Use para propor estrutura de pastas e nomenclatura para acervos de documentos (políticas, contratos, projetos).
category: documentacao
priority: opcional
depends_on: []
composes_with:
  - conhecimento/classificador-documentos
  - produtividade/organizador-arquivos
version: 0.1.0
status: rascunho
---

# Organizador Documental

## Objetivo
Sugerir estrutura de pastas, convenção de nomes e taxonomia para acervos corporativos.

## Entradas
- `tipo_acervo` (enum)
- `volumetria_estimada` (int)
- `usuarios` (lista)

## Saída
Mapa de pastas + convenção de nomes + guia de uso.

## Boas práticas
- Estrutura rasa.
- Nomes sem caracteres especiais.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para propor estrutura de pastas e nomenclatura para acervos de documentos (políticas, contratos, projetos).

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

