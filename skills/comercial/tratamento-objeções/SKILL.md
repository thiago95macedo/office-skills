---
name: tratamento-objeções
description: Use quando o cliente apresentar objeções (preço, prazo, escopo, fornecedor) e a equipe comercial precisar de argumentos estruturados.
category: comercial
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - comercial/proposta-comercial
  - comercial/follow-up
version: 0.1.0
status: rascunho
---

# Tratamento de Objeções

## Objetivo
Estruturar resposta técnica e comercial a objeções comuns, com argumentos objetivos e respeitosos.

## Quando usar
- Cliente diz "está caro".
- Cliente diz "demora muito".
- Cliente questiona escopo.

## Entradas
- `objecao` (string)
- `contexto_cliente` (dict)
- `evidencias_disponiveis` (lista)

## Saída
Documento com: objeção original, análise, argumentos, evidências, próxima ação recomendada.

## Boas práticas
- Reconhecer a objeção antes de rebater.
- Usar evidências, não adjetivos.
- Oferecer alternativas quando aplicável.