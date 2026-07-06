# Template-base de SKILL.md

Copie este arquivo para `skills/<categoria>/<slug>/SKILL.md` e preencha.

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
Frase única declarando o que esta Skill produz.

## Quando usar
Liste 3 a 5 situações em que a Skill é a ferramenta correta.

## Quando NÃO usar
Liste situações em que outra Skill ou outro processo deve ser usado.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| ... | texto | sim | ... |

## Saídas esperadas
Estrutura do artefato produzido, em Markdown.

## Fluxo interno
1. Ler entradas e contexto da empresa.
2. Aplicar tom e estilo definidos em `config/empresa.yaml`.
3. Produzir rascunho.
4. Validar checklist interno.
5. Entregar artefato.

## Boas práticas
- Use tom alinhado à cultura da empresa.
- Cite dados quando fornecidos.
- Sinalize suposições.

## Limitações
- Não acessa dados em tempo real.
- Não toma decisões estratégicas.

## Dependências
- `core/redator-corporativo`

## Exemplos de uso
Veja `examples/`.

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- CRM
- ERP
- GED
```