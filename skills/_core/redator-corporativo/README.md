# Redator Corporativo

Skill transversal responsável por garantir que todo texto da empresa soe coerente, técnico e respeite a voz configurada para a organização.

Use esta Skill sempre que o texto for representar a empresa externamente ou internamente em canais formais.

## Arquivos desta Skill

- `SKILL.md` — definição canônica
- `prompt.md` — prompt otimizado para o agente
- `examples/` — exemplos básico, intermediário e avançado
- `templates/` — templates de entrada e saída
- `tests/` — casos de teste

## Uso rápido

```yaml
objetivo: "Comunicar novo procedimento de auditoria interna"
publico: "Colaboradores dos times de Qualidade e Operações"
tom: "formal"
rascunho: |
  Informamos que a partir de 01/08 o procedimento XP-12 passa a vigorar.
restricoes:
  - maximo_palavras: 200
```

A Skill devolverá o texto revisado, mantendo a mensagem, ajustando tom e removendo ambiguidades.