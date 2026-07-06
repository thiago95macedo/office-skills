# Exemplo avançado — Revisão de proposta

## Entrada
```yaml
objetivo: "Revisar proposta comercial para cliente regulado pela ANVISA"
publico: "Gerente de Garantia da Qualidade"
tom: "formal"
rascunho: |
  Nossa empresa é a melhor do mercado e vai revolucionar o controle de qualidade de vocês.
restricoes:
  - maximo_palavras: 400
  - evitar: ["melhor do mercado", "revolucionar", "absoluto"]
```

## Saída esperada
> Remoção de adjetivos vazios, substituição por evidência operacional.

A JTLab apresenta proposta técnica para qualificação de equipamentos analíticos, contemplando IQ/OQ/PQ em conformidade com Boas Práticas de Fabricação e requisitos da ANVISA.

A execução segue protocolo rastreável, com documentação auditável e equipe técnica certificada. A experiência da empresa em laboratórios regulados sustenta a aderência aos critérios do cliente.