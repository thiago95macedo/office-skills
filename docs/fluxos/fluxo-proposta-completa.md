# Fluxo — Proposta Comercial Completa

## Objetivo de negócio
Entregar uma proposta comercial robusta, com escopo técnico, orçamento, condições e tratamento de possíveis objeções, pronta para anexo a processo de compra.

## Sequência de Skills

1. `_core/configurador-empresa` — carregar contexto corporativo.
2. `comercial/escopo-tecnico` — definir escopo detalhado.
3. `financeiro/analise-custos` — decompor custos e sugerir preço.
4. `comercial/orcamento` — produzir tabela de orçamento.
5. `comercial/proposta-comercial` — compor documento final.
6. `comercial/tratamento-objeções` — gerar bloco de FAQ de objeções comuns.
7. `comercial/one-pager` — produzir resumo executivo de 1 página (anexo).

## Entradas

- Dados do cliente (nome, contato, segmento)
- Necessidade descrita
- Restrições (prazo, orçamento)
- Tabela de preços padrão

## Saída final

- Proposta completa em Markdown (PDF opcional)
- Orçamento tabular
- FAQ de objeções
- One-pager resumo

## Quando usar
- Resposta a RFP/RFQ
- Pedido formal de proposta
- Repactuação de contrato

## Pré-requisitos
- Acesso a `config/empresa.yaml`
- Tabela de preços atualizada