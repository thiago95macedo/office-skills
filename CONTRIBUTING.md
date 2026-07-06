# Contribuindo com Office Skills

Bem-vindo(a)! Este guia mostra como criar, revisar e melhorar Skills.

## Antes de começar

1. Leia o `README.md`, `ARCHITECTURE.md` e `GOVERNANCE.md`.
2. Verifique o `INDEX.md` para evitar Skills duplicadas.
3. Se for criar uma Skill nova, abra uma issue descrevendo a necessidade.

## Criando uma nova Skill

### 1. Escolha a categoria

`skills/<categoria>/<skill-slug>/` — slug em kebab-case, verbos no infinitivo quando possível (ex.: `redator-corporativo`, `analise-custos`).

### 2. Crie a estrutura de pastas

```
skills/<categoria>/<skill-slug>/
├── SKILL.md
├── README.md
├── prompt.md
├── examples/
├── templates/
└── tests/
```

### 3. Preencha o SKILL.md

Use o template abaixo como ponto de partida:

```markdown
---
name: <slug-da-skill>
description: <frase de uma linha dizendo QUANDO usar>
category: <categoria>
priority: <essencial|recomendada|opcional>
depends_on:
  - <outra-skill>
composes_with:
  - <outra-skill>
version: 0.1.0
status: <rascunho|revisao|estavel|deprecada>
---

# <Nome da Skill>

## Objetivo
...

## Quando usar
...

## Quando NÃO usar
...

## Entradas esperadas
...

## Saídas esperadas
...

## Fluxo interno
...

## Boas práticas
...

## Limitações
...

## Dependências
...

## Exemplos de uso
...

## Prompt interno recomendado
...

## Possíveis integrações
...
```

### 4. Preencha o prompt.md

O `prompt.md` é a versão "otimizada para o agente", com instruções mais densas e menos prosa. Pode (e deve) ser mais imperativo que o SKILL.md.

### 5. Crie os templates

`templates/entrada.template.md` mostra o schema de entrada esperado.
`templates/saida.template.md` mostra a estrutura da saída.

### 6. Escreva os testes

`tests/casos-de-teste.md` lista pelo menos três cenários realistas. Cada cenário descreve entrada, comportamento esperado e critérios de aprovação.

### 7. Adicione exemplos

Em `examples/`, coloque exemplos curtos e completos. Um básico, um intermediário, um avançado.

### 8. Atualize o INDEX.md

Adicione a Skill ao `INDEX.md` na seção da categoria correspondente.

### 9. Rode a validação

```bash
bash scripts/validate.sh
```

## Estilo de escrita

- Linguagem neutra e objetiva.
- Frases curtas.
- Sem marketing ou adjetivos vazios.
- Listas e tabelas quando a estrutura ajudar.
- Exemplos sempre concretos.

## Checklist final antes do PR

- [ ] SKILL.md tem frontmatter completo.
- [ ] README.md, prompt.md, examples/, templates/ e tests/ existem.
- [ ] Pelo menos três casos de teste estão escritos.
- [ ] INDEX.md foi atualizado.
- [ ] `scripts/validate.sh` passa sem erros.
- [ ] A Skill não duplica nenhuma existente.
- [ ] Versão semântica foi atribuída.