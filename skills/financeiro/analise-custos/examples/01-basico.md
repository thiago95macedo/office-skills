# Exemplo básico — Serviço de calibração

## Entrada
```yaml
itens_custo:
  - { item: "Técnico (4h)", quantidade: 1, valor_unitario: 600 }
  - { item: "Padrão de calibração", quantidade: 1, valor_unitario: 250 }
  - { item: "Deslocamento", quantidade: 1, valor_unitario: 180 }
custos_indiretos:
  rateio_por_servico: 150
margem_desejada: 30
impostos:
  iss: 5
  pis_cofins: 3.65
```

## Saída esperada (resumida)

| Item | Valor |
|------|-------|
| Custos diretos | 1.030,00 |
| Custos indiretos | 150,00 |
| Subtotal | 1.180,00 |
| Impostos (8,65%) | 102,07 |
| Margem (30%) | 354,00 |
| **Preço sugerido** | **1.636,07** |

Premissas:
- Rateio de indiretos por serviço.
- ISS municipal 5%, regime cumulativo.

Cenários:
- Conservador (margem 20%): R$ 1.522,00
- Base (margem 30%): R$ 1.636,07
- Agressivo (margem 45%): R$ 1.802,00