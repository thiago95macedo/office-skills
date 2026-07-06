---
name: proposta-comercial
description: Use quando precisar gerar proposta comercial completa para cliente (resumo executivo, escopo, condições comerciais, cronograma, contatos).
category: comercial
priority: essencial
depends_on:
  - _core/redator-corporativo
  - comercial/escopo-tecnico
  - comercial/orcamento
composes_with:
  - comercial/follow-up
  - comercial/resposta-rfp
  - comercial/tratamento-objeções
version: 0.1.0
status: rascunho
---

# Proposta Comercial

## Objetivo
Produzir proposta comercial completa, padronizada e auditável, pronta para anexar a processos de compra corporativos.

## Quando usar
- Responder a RFP ou solicitação direta de proposta.
- Formalizar negociação verbal com cliente.

## Quando NÃO usar
- Para orçamento avulso (usar `comercial/orcamento`).
- Para escopo técnico isolado (usar `comercial/escopo-tecnico`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `cliente.nome` | string | sim |
| `cliente.contato` | string | sim |
| `escopo` | dict | sim |
| `orcamento` | dict | sim |
| `condicoes_comerciais` | dict | sim |
| `validade` | data | sim |
| `cronograma` | dict | não |

## Saídas esperadas
Documento Markdown estruturado com seções:
1. Resumo executivo
2. Objetivo
3. Escopo
4. Atividades
5. Exclusões
6. Premissas
7. Cronograma
8. Responsabilidades
9. Condições comerciais
10. Validade
11. Contato

## Boas práticas
- Linguagem objetiva.
- Sem adjetivos vazios.
- Sempre declarar exclusões.
- Sempre indicar validade.

## Limitações
- Não calcula impostos em tempo real.
- Não emite contrato juridicamente vinculante.