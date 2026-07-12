---
name: conteudo-site
description: Use para produzir páginas institucionais (home, sobre, serviços, contato) com SEO on-page, escaneabilidade e CTA.
category: marketing
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-linkedin
  - marketing/artigo-blog
  - marketing/case-de-sucesso
version: 0.2.0
status: estavel
references:
  - Krug, S. Don't Make Me Think, Revisited. 3. ed. 2013.
  - Google Search Central — Helpful Content (E-E-A-T).
  - Halvorson, K.; Rach, M. Content Strategy for the Web. 2. ed. 2012.
  - WCAG 2.1 AA — Diretrizes de Acessibilidade.
  - BRASIL. LGPD Lei 13.709/2018 (cookies e formulários).
---

# Conteúdo para Site

## Objetivo
Produzir páginas institucionais completas (Home, Sobre, Serviços, Contato, Landing Pages) prontas para implementação em CMS, com SEO on-page, escaneabilidade e CTA.

## Quando usar
- Site institucional (empresa, produto, ONG).
- Landing pages de campanha.
- Páginas de serviços/produtos individuais.
- Páginas de captura (lead magnet, e-book, webinar).
- Páginas de portfólio ou cases.

## Quando NÃO usar
- Para blog (usar `marketing/artigo-blog`).
- Para FAQ (usar `documentacao/faq-corporativo`).
- Para help center / documentação técnica (usar `suporte/faq-tecnico` ou `documentacao/manual-tecnico`).

## Tipos de página e objetivos

| Tipo | Objetivo | Componentes canônicos |
|------|----------|----------------------|
| **Home** | Apresentação + roteamento | Hero + Proposta de valor + Cases + CTA |
| **Sobre** | Identidade e credibilidade | História + Equipe + Missão/Visão + Valores |
| **Serviços** | Compra | Proposta + Benefícios + Cases + Formulário |
| **Contato** | Conversão direta | Endereço + Telefones + Formulário + Mapa |
| **Landing page** | Conversão específica | Headline + Sub + Prova social + Formulário curto |
| **Cases** | Prova social | Cards de case + Logos de clientes |
| **Carreiras** | Atração de talentos (usar `rh/descricao-vaga`) | Cultura + Vagas abertas |

## Estrutura recomendada de SEO on-page

| Elemento | Boas práticas |
|----------|---------------|
| **Title tag** | Único, ≤ 60 caracteres, keyword no início |
| **Meta description** | ≤ 155 caracteres, persuasiva |
| **H1** | Único por página, contém keyword principal |
| **Headings (H2/H3)** | Hierárquicos, sem pular níveis, com keywords secundárias |
| **URL slug** | Curto, com keyword, sem caracteres especiais |
| **Schema.org** | Organization, BreadcrumbList, FAQPage, Service |
| **Alt text** | Descritivo em todas as imagens |
| **Links internos** | Para outras páginas do site (topologia) |
| **CTA** | Acima da dobra + final + âncoras no meio |

## Conformidade legal obrigatória (Brasil)

| Marco | Aplicação |
|-------|-----------|
| **LGPD art. 9º** | Informar finalidade de cookies e formulários |
| **LGPD art. 18** | Direito do titular (acesso, correção, exclusão) |
| **CDC art. 30, 31** | Fornecedor de serviços responde por defeitos |
| **E-commerce (Decreto 7.962/2013)** | Informações obrigatórias (CNPJ, endereço) |
| **Marco Civil (Lei 12.965/2014)** | Privacidade na rede |
| **WCAG 2.1 AA** | Acessibilidade digital |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `pagina` | enum | sim | home / sobre / servicos / contato / landing-page / cases |
| `tema` | string | sim | Assunto principal da página |
| `publico` | string | sim | Persona do visitante |
| `seo_keywords` | lista | sim | Keywords (1 principal + 2-3 secundárias) |
| `cta_principal` | string | sim | Próxima ação desejada |
| `meta_title` | string | sim | Title tag |
| `meta_description` | string | sim | Meta description |
| `link_interno` | lista | não | URLs de páginas relacionadas |
| `prova_social` | dict | não | Logos de clientes, depoimentos, números |
| `campos_formulario` | lista | não | Para páginas de captura |

## Saídas esperadas
- Estrutura HTML/Markdown da página.
- Cabeçalho (head) com meta tags.
- Headlines (H1, H2, H3).
- Meta description.
- Blocos de conteúdo (hero, seções, prova social).
- CTA(s) estratégico(s).
- Schema.org JSON-LD (quando aplicável).
- Versão de cookie banner (LGPD).

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom institucional, dados cadastrais).
2. Validar SEO keyword principal (volume, intenção de busca).
3. Definir objetivo da página (ROI esperado).
4. Estruturar H1, H2, H3 com hierarquia lógica.
5. Redigir blocos curtos e escaneáveis.
6. Inserir CTA principal acima da dobra e no final.
7. Adicionar prova social (logos, depoimentos, números).
8. Produzir meta title e meta description.
9. Definir URL slug.
10. Configurar Schema.org (Organization, BreadcrumbList, Service).
11. Verificar acessibilidade WCAG 2.1 AA.
12. Configurar cookie banner conforme LGPD.

## Boas práticas
- **H1 único** por página — Google penaliza múltiplos.
- **H2 com keywords secundárias** — sem stuffing.
- **Headline poderosa** — Krug: deve ser óbvia em 3 segundos.
- **CTA acima da dobra** — sem rolar para encontrar.
- **Prova social** — logos de clientes reconhecíveis, números reais.
- **Escaneabilidade** — bullets, parágrafos curtos, ênfase visual.
- **Velocidade** — imagens otimizadas, lazy loading.
- **Responsivo** — mobile-first.
- **Acessibilidade WCAG 2.1 AA** — contraste, alt text, navegação por teclado.
- **Schema.org** — rich snippets no Google.
- **Cookie banner LGPD** — opt-in real (não pré-marcado).
- **Formulário mínimo** — apenas campos essenciais (LGPD: minimização).
- **Verificação contínua** — Google Search Console, PageSpeed Insights.

## Armadilhas comuns
- H1 múltiplo (SEO ruim).
- Keyword stuffing (penalização manual).
- Sem CTA ou CTA genérico ("Clique aqui").
- Imagens pesadas (Core Web Vitals ruim).
- Carrossel automático ("kills content", Krug).
- Sem meta description (Google gera, mal).
- Formulário longo (abaixa conversão).
- Cookie banner pré-marcado (viola LGPD).
- Sem Schema.org (perde rich snippets).
- Sem HTTPS (penalização Google).
- Pop-up intrusivo (Mobile Interstitial Penalty).
- Sem página de política de privacidade.

## Limitações
- Não implementa HTML final (entrega conteúdo pronto para CMS).
- Não mede SEO automaticamente (depende de Search Console).
- Não acessa Core Web Vitals reais.
- Não gera imagens (apenas sugestões).
- Não projeta layout visual (apenas estrutura).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Página "Sobre" institucional
- `02-intermediario.md` — Página de serviços com prova social
- `03-avancado.md` — Landing page de geração de leads

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- CMS (WordPress, Drupal, Webflow, Contentful)
- Ferramentas de SEO (Semrush, Ahrefs, Yoast)
- Formulários (RD Station, HubSpot, Typeform)
- Analytics (Google Analytics, GA4, Plausible)
- A/B testing (Google Optimize, VWO)