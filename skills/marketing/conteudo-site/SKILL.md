---
name: conteudo-site
description: Use para produzir páginas institucionais (home, sobre, serviços, contato) com SEO básico.
category: marketing
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-linkedin
  - marketing/artigo-blog
version: 0.1.0
status: rascunho
---

# Conteúdo para Site

## Objetivo
Produzir páginas institucionais completas, prontas para implementação em CMS.

## Quando usar
- Site institucional.
- Landing pages.
- Páginas de serviços/produtos.

## Quando NÃO usar
- Para blog (usar `marketing/artigo-blog`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `pagina` | enum | sim |
| `tema` | string | sim |
| `publico` | string | sim |
| `seo_keywords` | lista | sim |
| `cta_principal` | string | sim |

## Saídas esperadas
- Estrutura HTML/Markdown.
- Headlines (H1, H2).
- Meta descrição.
- CTA(s).

## Fluxo interno
1. Definir objetivo da página.
2. Listar palavras-chave SEO.
3. Estruturar H1, H2, H3.
4. Redigir blocos curtos.
5. Inserir CTA.
6. Produzir meta descrição.

## Boas práticas
- H1 único.
- Subtítulos com palavras-chave.
- Parágrafos curtos.
- Linkagem interna quando possível.

## Limitações
- Não implementa HTML final.
- Não mede SEO automaticamente.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- WordPress
- Webflow
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir páginas institucionais (home, sobre, serviços, contato) com SEO básico.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

