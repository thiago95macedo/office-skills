# Prompt interno — Compositor de Fluxos

Execute passos em ordem, mapeando saída→entrada conforme contrato.

```yaml
passos:
  - skill: comercial/escopo-tecnico
    entrada: { ... }
  - skill: comercial/orcamento
    entrada: { escopo: <saida_anterior> }
```