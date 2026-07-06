---
name: oficio-memorando
description: Use para produzir ofícios e memorandos internos formais, com numeração, destinatário, assunto, conteúdo e assinatura.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
version: 0.1.0
status: rascunho
---

# Ofício / Memorando

## Objetivo
Padronizar comunicações formais internas com estrutura rígida e auditável.

## Entradas
- `tipo` (enum: oficio | memorando)
- `destinatario` (dict)
- `assunto` (string)
- `conteudo` (string)

## Saída
Documento com numeração, cabeçalho, corpo, local/data, assinatura.

## Boas práticas
- Linguagem impessoal.
- Sem ambiguidade.
- Numeração sequencial quando em série.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir ofícios e memorandos internos formais, com numeração, destinatário, assunto, conteúdo e assinatura.

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

