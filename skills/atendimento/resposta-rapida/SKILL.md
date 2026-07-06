---
name: resposta-rapida
description: Use para gerar resposta curta, cordial e útil a demandas de atendimento.
category: atendimento
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - atendimento/triagem-mensagens
version: 0.1.0
status: rascunho
---

# Resposta Rápida

## Objetivo
Produzir respostas curtas (até 80 palavras), cordiais e úteis, com CTA claro.

## Quando usar
- Confirmação de recebimento.
- Solicitação de informação complementar.
- Direcionamento a responsável.

## Quando NÃO usar
- Para respostas técnicas detalhadas.
- Para respostas comtemplando objeções (usar `comercial/tratamento-objeções`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `mensagem_original` | string | sim |
| `contexto` | dict | sim |
| `tom` | enum | sim |

## Saídas esperadas
Mensagem curta (até 80 palavras), cordial, com CTA.

## Fluxo interno
1. Identificar objetivo da resposta.
2. Selecionar tom.
3. Redigir em até 80 palavras.
4. Inserir CTA.
5. Validar cordialidade.

## Limitações
- Não trata questões técnicas complexas.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- Zendesk Macro
- Freshdesk