# Pipeline com ramificação condicional

```yaml
passos:
  - skill: comercial/escopo-tecnico
  - condicional: orcamento.valor > 100000
    then:
      - skill: comercial/tratamento-objeções
    else:
      - skill: comercial/follow-up
```