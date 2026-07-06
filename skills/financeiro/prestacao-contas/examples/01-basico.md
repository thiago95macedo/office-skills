# Exemplo básico — Viagem corporativa

## Entrada
```yaml
periodo: "01–03/07/2026"
responsavel: "Ana Souza"
centro_custo: "COM-2026-014"
valor_total_recebido: 2500
itens:
  - { data: "01/07", descricao: "Passagem aérea SP–RJ", nf: "12345", valor: 850 }
  - { data: "01/07", descricao: "Hospedagem 2 diárias", nf: "REC-009", valor: 720 }
  - { data: "02/07", descricao: "Refeições", nf: "s/n", valor: 180 }
  - { data: "03/07", descricao: "Táxi aeroporto", nf: "REC-010", valor: 95 }
```

## Saída
- Total recebido: R$ 2.500,00
- Total gasto: R$ 1.845,00
- Saldo a devolver: R$ 655,00

Parecer: Pendente — 1 item sem NF ("Refeições"). Solicitar comprovante.