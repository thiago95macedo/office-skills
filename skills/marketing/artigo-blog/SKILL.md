---
name: artigo-blog
description: Use para produzir artigos de blog com SEO on-page, estrutura escaneável, E-E-A-T e CTA.
category: marketing
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-site
  - marketing/conteudo-linkedin
  - marketing/case-de-sucesso
version: 0.2.0
status: estavel
references:
  - Halvorson, K.; Rach, M. Content Strategy for the Web. 2. ed. 2012 (Content Strategy).
  - Google Search Central — Helpful, reliable, people-first content (E-E-A-T).
  - Google — SEO Starter Guide (atualizado 2025).
  - Krug, S. Don't Make Me Think, Revisited. 3. ed. 2013.
---

# Artigo de Blog

## Objetivo
Produzir artigos de blog completos com pesquisa estruturada, narrativa clara, SEO on-page, alinhados aos padrões E-E-A-T do Google e adaptados ao tom corporativo da empresa.

## Quando usar
- Educação de mercado (topo de funil).
- SEO orgânico (long-tail keywords).
- Construção de autoridade técnica (E-E-A-T).
- Conteúdo para nutrir leads (meio de funil).
- Suporte a SEO de página institucional (linkagem interna).

## Quando NÃO usar
- Para post curto em rede social (usar `marketing/conteudo-linkedin`).
- Para comunicado ou anúncio (usar `administrativo/comunicado-interno`).
- Para artigo científico (usar formato acadêmico).

## Estrutura recomendada (SEO + UX)

| # | Bloco | Função |
|---|-------|--------|
| 1 | **Meta title** | Até 60 caracteres, com keyword principal |
| 2 | **Meta description** | Até 155 caracteres, persuasiva |
| 3 | **URL slug** | Curto, com keyword, separado por hífens |
| 4 | **H1 único** | Título do artigo (1 por página) |
| 5 | **Introdução** | 2-3 parágrafos com gancho e keyword |
| 6 | **Corpo** | 5-8 seções com H2/H3 |
| 7 | **Imagens** | Com alt text descritivo e legenda |
| 8 | **Links internos** | Para outros artigos e páginas do site |
| 9 | **Links externos** | Para fontes confiáveis (autoridade) |
| 10 | **CTA** | Lead magnet, contato, avaliação |
| 11 | **Sobre o autor** | Bio + credenciais (E-E-A-T) |

## Boas práticas de SEO on-page (Google, 2025)

| Elemento | Boas práticas |
|----------|---------------|
| **Title tag** | Único por página, ≤ 60 caracteres, keyword principal no início |
| **Meta description** | ≤ 155 caracteres, persuasiva, com CTA |
| **H1** | Um único, contém keyword principal |
| **H2/H3** | Hierárquicos (sem pular níveis), com keywords secundárias |
| **URL slug** | Curto, com keyword, sem stop words |
| **Alt text em imagens** | Descritivo, com keyword quando relevante |
| **Conteúdo** | Responder à intenção de busca, palavras-chave naturais |
| **Links** | Internos (topologia) e externos (autoridade) para fontes confiáveis |
| **E-E-A-T** | Experiência, especialização, autoridade, confiabilidade demonstráveis |

## Boas práticas de redação (Nielsen, Krug)

- **Escaneabilidade** — bullets, subtítulos, negrito em palavras-chave.
- **Parágrafos curtos** — 3-4 linhas (mobile-friendly).
- **Linha 50-75 caracteres** — fácil leitura.
- **Conclusão primeiro** — "pirâmide invertida" (jornalismo).
- **Hierarquia visual** — H2/H3 bem marcados.
- **Sem jargão desnecessário** — adaptar para o público.
- **CTA explícito** — no final + ao longo do texto.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tema` | string | sim | Assunto do artigo |
| `keywords` | lista | sim | Palavras-chave (1 principal + 2-3 secundárias) |
| `publico` | string | sim | Persona do leitor |
| `extensao` | enum | sim | curto (800-1200) / medio (1500-2500) / longo (3000+) |
| `cta` | string | sim | Próxima ação desejada |
| `autor` | dict | sim | Nome, cargo, bio |
| `meta_title` | string | não | Sugestão de title tag |
| `meta_description` | string | não | Sugestão de meta description |
| `link_interno` | lista | não | URLs de páginas relacionadas |

## Saídas esperadas
- Outline aprovado com estrutura H1/H2/H3.
- Artigo completo com SEO on-page.
- Meta title (≤ 60 caracteres).
- Meta description (≤ 155 caracteres).
- Sugestão de URL slug.
- Alt text para imagens.
- Links internos e externos.
- CTA no início, meio e fim.
- Bio do autor (E-E-A-T).

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom e dados do autor).
2. Pesquisar palavra-chave principal (volume, intenção de busca).
3. Definir outline com base na SERP (top 10 resultados) e intenção.
4. Redigir meta title e meta description com keyword.
5. Produzir artigo com parágrafos curtos e escaneáveis.
6. Inserir links internos e externos (autoritativos).
7. Adicionar CTA em momentos estratégicos.
8. Incluir bio do autor (E-E-A-T).
9. Validar alt text em imagens.
10. Checklist de SEO on-page (title, meta, H1, headings, etc.).

## Boas práticas
- **Outline antes da redação** — validar estrutura antes de gastar tempo.
- **1 keyword principal + 2-3 secundárias** (densidade 1-2%).
- **Pesquisa SERP antes** — entender o que já ranqueia.
- **Intenção de busca** — informativo / comercial / transacional.
- **Parágrafos curtos** — 3-4 linhas (mobile-first).
- **Imagens com alt text** — descrever de verdade.
- **Links internos** — topologia de conteúdo (clusters).
- **E-E-A-T demonstrável** — bio do autor, fontes, evidências.
- **Atualização periódica** — conteúdo envelhece (Z-score de declínio).
- **CTA contextual** — não só no fim (a cada 500-800 palavras).
- **Acessibilidade** — contraste, legendas, estrutura semântica.
- **Core Web Vitals** — imagens otimizadas, semântica.

## Armadilhas comuns
- Keyword stuffing — Google penaliza.
- Conteúdo thin (curto e raso) — não ranqueia.
- Sem E-E-A-T — perde autoridade.
- Texto sem escaneabilidade — alto bounce rate.
- Sem CTA — não converte.
- Linkagem interna quebrada — prejudica topologia.
- Imagens sem alt text — prejudica SEO e acessibilidade.
- Conteúdo desatualizado — declina no ranking.
- Plágio ou "spin" — penalização manual.
- Misturar intenção de busca (informacional + comercial em um artigo).

## Limitações
- Não faz pesquisa de palavras-chave em tempo real (depende de input).
- Não verifica ranking da SERP.
- Não substitui otimização técnica de Core Web Vitals.
- Não mede tempo de leitura, scroll, conversão.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Artigo curto para SEO (800-1200 palavras)
- `02-intermediario.md` — Artigo médio educativo (2000 palavras)
- `03-avancado.md` — Pilar de cluster de conteúdo (3000+ palavras)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- CMS (WordPress, Ghost, Webflow, Drupal)
- SEO (Semrush, Ahrefs, Ubersuggest)
- Plugin de schema.org (FAQPage, Article)
- Imagens (banco de imagens próprio ou licença comercial)