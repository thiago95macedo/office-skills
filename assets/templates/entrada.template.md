# Template-base — Entrada esperada

```yaml
empresa:
  nome: <nome>
  tom: <formal|semiformal|informal>
  vocabulario_bloqueado: []
contexto:
  objetivo: <...>
  publico: <...>
  prazo: <YYYY-MM-DD>
restricoes:
  maximo_palavras: <n>
  anexos_obrigatorios: []
```

## Campos obrigatórios

- `empresa.nome`
- `contexto.objetivo`
- `contexto.publico`

## Campos opcionais

- `contexto.prazo`
- `restricoes.maximo_palavras`
- `restricoes.anexos_obrigatorios`