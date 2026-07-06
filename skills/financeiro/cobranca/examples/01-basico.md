# Exemplo básico — Cobrança amigável 7 dias

## Entrada
```yaml
cliente: { nome: "Laboratório X", contato: "financeiro@labx.com.br" }
fatura: { numero: "NF-12345", valor: 5800, vencimento: "2026-06-25" }
dias_atraso: 7
tom: amigavel
```

## Saída

**Assunto:** Lançamento NF-12345 — pendência em aberto

Prezados,

Identificamos que a fatura NF-12345, no valor de R$ 5.800,00, com vencimento em 25/06/2026, encontra-se em aberto.

Caso o pagamento já tenha sido realizado, gentileza desconsiderar este aviso. Em caso de dúvida, estamos à disposição para conciliar.

Atenciosamente,
Equipe Financeira — {{empresa}}