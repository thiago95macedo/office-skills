# Casos de teste — Análise de Custos

## Caso 1 — Serviço simples sem rateio complexo
**Entrada:** 3 itens diretos, 1 indireto, margem 30%.
**Esperado:** decomposição correta, preço base calculado, 3 cenários apresentados.

## Caso 2 — Projeto multi-equipe com rateio por hora
**Entrada:** 3 técnicos com valores/hora distintos, rateio de estrutura.
**Esperado:** custo MO discriminado por técnico, rateio aplicado, total coerente.

## Caso 3 — Análise multi-produto com impostos por estado
**Entrada:** 5 SKUs, ICMS variável.
**Esperado:** matriz SKU × cenário, margem ponderada, recomendação de tabela.

## Critérios verificáveis
- Soma do rateio = total declarado em `valor_total_indireto`.
- Impostos aplicados sobre base de cálculo correta.
- Cenários preservam consistência da margem declarada.