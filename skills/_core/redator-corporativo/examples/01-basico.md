# Exemplo básico — Revisão de e-mail curto

## Entrada
```yaml
tom: formal
rascunho: |
  galera, segue em anexo o procedimento novo. quem tiver dúvida me chama.
restricoes:
  - maximo_palavras: 80
```

## Saída esperada
> Substituir "galera" por "equipe". Converter para português formal e remover coloquialismo "me chama".

Prezados(as),

Segue em anexo o novo procedimento. Dúvidas podem ser encaminhadas ao responsável pelo processo.

Atenciosamente,
[Nome]
[Cargo]