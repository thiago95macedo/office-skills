---
name: base-conhecimento
description: Use para organizar e manter base de conhecimento interna (categorias, donos, ciclo de revisão).
category: suporte
priority: opcional
depends_on: []
composes_with:
  - suporte/faq-tecnico
  - conhecimento/mapa-conhecimento
version: 0.1.0
status: rascunho
---

# Base de Conhecimento

## Objetivo
Estruturar base de conhecimento com taxonomia, donos e ciclo de revisão.

## Quando usar
- Organização inicial.
- Revisão periódica.
- Auditoria.

## Quando NÃO usar
- Para FAQ específico (usar `suporte/faq-tecnico`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `conteudo_atual` | lista | sim |
| `categoria` | dict | sim |
| `dono` | dict | sim |
| `ciclo_revisao` | string | sim |

## Saídas esperadas
- Taxonomia proposta.
- Donos por categoria.
- Itens vencidos e a vencer.
- Recomendações.

## Limitações
- Não mede uso real.

## Dependências
- Nenhuma

## Possíveis integrações
- Confluence
- Notion
## Secoes de referencia (geradas)

Descricao desta Skill: Use para organizar e manter base de conhecimento interna (categorias, donos, ciclo de revisão).

## Fluxo interno

Detalhar os passos que o agente segue para executar a Skill.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

