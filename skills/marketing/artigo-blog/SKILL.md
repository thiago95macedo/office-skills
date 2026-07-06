---
name: artigo-blog
description: Use para produzir artigos de blog com SEO básico, estrutura escaneável e CTA.
category: marketing
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-site
  - marketing/conteudo-linkedin
version: 0.1.0
status: rascunho
---

# Artigo de Blog

## Objetivo
Produzir artigos de blog completos, com pesquisa estruturada, narrativa clara e SEO.

## Quando usar
- Educação de mercado.
- SEO orgânico.
- Autoridade técnica.

## Quando NÃO usar
- Para post curto em rede social (usar `marketing/conteudo-linkedin`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `tema` | string | sim |
| `keywords` | lista | sim |
| `publico` | string | sim |
| `extensao` | enum | sim |
| `cta` | string | sim |

## Saídas esperadas
- Outline aprovado.
- Artigo completo com H1/H2/H3.
- Meta descrição.
- Sugestão de imagens.
- CTA final.

## Fluxo interno
1. Definir outline.
2. Pesquisar palavras-chave.
3. Redigir artigo.
4. Inserir links internos/externos.
5. Adicionar CTA.

## Boas práticas
- Outline antes da redação.
- 1 keyword principal + 2-3 secundárias.
- Parágrafos curtos.

## Limitações
- Não faz pesquisa em tempo real.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- WordPress
- Ghost
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir artigos de blog com SEO básico, estrutura escaneável e CTA.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

