---
name: email-corporativo
description: Use para redigir e-mails profissionais (externos ou internos) com tom, estrutura e tamanho adequados.
category: administrativo
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/comunicado-interno
  - comercial/follow-up
version: 0.1.0
status: rascunho
---

# E-mail Corporativo

## Objetivo
Produzir e-mails profissionais com assunto claro, abertura cordial, conteúdo objetivo e CTA.

## Entradas
- `destinatario` (string)
- `assunto` (string)
- `mensagem_central` (string)
- `tom` (enum)
- `anexos` (lista, opcional)

## Saída
E-mail pronto em Markdown, com assunto e assinatura.

## Boas práticas
- Assunto com ≤ 8 palavras.
- Corpo com até 3 parágrafos principais.
- CTA explícito.
## Secoes de referencia (geradas)

Descricao desta Skill: Use para redigir e-mails profissionais (externos ou internos) com tom, estrutura e tamanho adequados.

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

