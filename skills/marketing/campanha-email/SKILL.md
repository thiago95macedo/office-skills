---
name: campanha-email
description: Use para estruturar sequência de e-mails marketing (lançamento, nutrição, reativação) conforme LGPD e boas práticas de entregabilidade.
category: marketing
priority: opcional
depends_on:
  - administrativo/email-corporativo
composes_with:
  - marketing/conteudo-linkedin
  - marketing/conteudo-site
  - marketing/artigo-blog
version: 0.2.0
status: estavel
references:
  - BRASIL. Lei 13.709/2018 — LGPD (consentimento, opt-in, opt-out).
  - BRASIL. Decreto 7.962/2013 — Comércio eletrônico (informações obrigatórias).
  - BRASIL. Decreto 10.271/2020 — Identificação do contratante eletrônico.
  - Chaudhry, S. The Long Tail. Wired, 2004 (foco em nichos).
---

# Campanha de E-mail

## Objetivo
Construir sequência de e-mails marketing com objetivo claro, segmentação, conteúdo progressivo e CTA consistente, conforme LGPD e práticas de entregabilidade.

## Quando usar
- Lançamento de produto/serviço/curso.
- Nutrição de leads (meio de funil).
- Reativação de base fria.
- Promoção comercial com prazo definido.
- Newsletter de autoridade.

## Quando NÃO usar
- Para 1 e-mail avulso (usar `administrativo/email-corporativo`).
- Para comunicado interno (usar `administrativo/comunicado-interno`).
- Para fluxo transacional de produto (usar template do sistema).

## Conformidade legal obrigatória (Brasil)

| Marco | Aplicação |
|-------|-----------|
| **LGPD art. 7º, I** | Consentimento livre, informado e inequívoco para tratamento de dados |
| **LGPD art. 9º** | Informar finalidade do tratamento |
| **LGPD art. 18, IX** | Direito de revogação do consentimento (opt-out facilitado) |
| **Decreto 7.962/2013** | Comércio eletrônico: informações obrigatórias (nome, CNPJ, endereço) |
| **Decreto 10.271/2020** | Identificação do contratante (nome + CPF/CNPJ) |
| **NBR 6028 / Boas práticas** | Identificação clara do remetente |

## Estrutura recomendada por e-mail

| Bloco | Orientação | Limite sugerido |
|-------|------------|-----------------|
| **Pré-cabeçalho** | Complementa assunto | ≤ 90 caracteres |
| **Assunto** | Resumo objetivo | ≤ 60 caracteres |
| **Saudação** | Cordial e personalizada | 1 linha |
| **Corpo** | Conteúdo principal | Escaneável, com 1 CTA |
| **CTA (botão)** | Ação clara | 1 botão + 1 link |
| **Rodapé** | Identificação do remetente, CNPJ, endereço, descadastro | Completo |

## Fluxo de campanhas comuns

| Objetivo | Estrutura típica |
|----------|-------------------|
| **Lançamento** | Aquecimento (3 e-mails) → Lançamento → Carrinho aberto (3-5 e-mails) → Carrinho fechado (1-2) |
| **Nutrição** | Conteúdo educativo progressivo (4-6 e-mails em 2-3 semanas) |
| **Reativação** | Pesquisa de motivo → Oferta personalizada → Última chance → Exclusão |
| **Newsletter** | Cadência fixa (semanal/quinzenal) com curadoria |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo` | string | sim | Objetivo da campanha |
| `publico` | string | sim | Segmento (base fria, leads novos, clientes, etc.) |
| `quantidade` | int | sim | Nº de e-mails na sequência |
| `gatilhos` | lista | não | Eventos que disparam e-mail (carrinho abandonado, aniversário, etc.) |
| `cta_principal` | string | sim | Ação desejada |
| `oferta` | dict | não | Desconto, bônus, brinde (quando aplicável) |
| `origem_dados` | enum | sim | base-propria / parceira / comprada (LGPD: só base própria é clara) |
| `prazo_campanha` | string | sim | Data início e fim |
| `remetente` | dict | sim | Nome, e-mail (ex: contato@empresa.com.br) |

## Saídas esperadas
- Sequência numerada de e-mails.
- Para cada e-mail: assunto, pré-cabeçalho, corpo, CTA.
- Cronograma de envio.
- Segmentação recomendada.
- Rodapé com informações obrigatórias (LGPD + Decreto 7.962/2013).
- Versão de descadastro (opt-out) funcional.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom, dados do remetente, CNPJ, endereço).
2. Validar base (LGPD: opt-in documentado, consentimento verificável).
3. Definir objetivo, segmentação, prazo.
4. Planejar sequência com progressão lógica.
5. Redigir cada e-mail (assunto → pré-cabeçalho → corpo → CTA → rodapé).
6. Definir cronograma de envio.
7. Revisar entregabilidade (assunto curto, sem spam words, sem ALL CAPS).
8. Configurar opt-out funcional (LGPD art. 18, IX).
9. Testar renderização em clientes (Gmail, Outlook, Apple Mail).

## Boas práticas
- **Opt-in documentado** (LGPD) — não comprar base.
- **Opt-out facilitado** — link visível, processo automático, sem custo.
- **Identificação do remetente** — nome + CNPJ + endereço (Decreto 7.962/2013).
- **Assunto objetivo** — ≤ 60 caracteres, sem clickbait.
- **Pré-cabeçalho relevante** — completa o assunto.
- **CTA único por e-mail** — confusão reduz conversão.
- **Escaneabilidade** — bullets, parágrafos curtos.
- **Sem spam words** — "grátis", "você ganhou", "clique aqui".
- **Sem ALL CAPS** — filtros antispam marcam como suspeito.
- **Texto alternativo em imagens** — exibido quando cliente bloqueia imagens.
- **Texto e imagem balanceados** — texto/imagem > 60/40.
- **Pessoa jurídica** clara — remetente identificável.
- **Densidade de imagem** — moderar (1-2 por e-mail).

## Armadilhas comuns
- Base comprada (viola LGPD + gera spam complaints).
- Opt-out difícil ou escondido (viola LGPD art. 18).
- Assunto clickbait ("Você ganhou!!!" — filtros antispam).
- Imagem pesada (carregamento lento, vai para spam).
- Sem versão texto alternativa (clientes de imagem bloqueada mostram nada).
- Remetente genérico ("noreply@") — baixa entregabilidade.
- CTA múltiplos ("clique aqui" + "clique ali" + "saiba mais") — confusão.
- Sem segmentação (envia tudo para todos).
- Calendário apertado (satura a base).
- Não limpar base (acumula inativos, prejudica reputação).

## Limitações
- Não envia automaticamente (depende de plataforma).
- Não testa A/B automaticamente (precisa de configuração).
- Não mede resultados (abertura, clique, conversão).
- Não gerencia descadastros automaticamente.
- Não valida DNS (SPF, DKIM, DMARC) — necessário para entregabilidade.

## Dependências
- `administrativo/email-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Newsletter semanal (4 e-mails)
- `02-intermediario.md` — Lançamento de produto (sequência de 6)
- `03-avancado.md` — Reativação de base fria (campanha de 4 etapas)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Plataformas de e-mail marketing (RD Station, Mailchimp, ActiveCampaign, Leadlovers)
- CRM (Pipedrive, HubSpot, Salesforce, RD CRM)
- Automação de marketing (HubSpot, RD Station, Dinamize)
- Sites e landing pages com formulários (WordPress, Leadpages)