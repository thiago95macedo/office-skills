# Entrada esperada — Análise de Custos

```yaml
itens_custo:
  - item: <descrição>
    quantidade: <qtd>
    valor_unitario: <R$>
custos_indiretos:
  rateio_por_servico: <R$>
  # ou
  base_rateio: <receita|hora|volume>
  valor_total_indireto: <R$>
margem_desejada: <%>
impostos:
  iss: <%>
  pis_cofins: <%>
  icms: <%>
concorrencia:
  - { concorrente: <nome>, preco: <R$> }
cenario: base
```

## Campos obrigatórios
- `itens_custo`
- `custos_indiretos`
- `margem_desejada`

## Campos opcionais
- `impostos`
- `concorrencia`
- `cenario`