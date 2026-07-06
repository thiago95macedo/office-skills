---
name: conteudo-linkedin
description: Use para produzir posts profissionais para LinkedIn com ganchos, estrutura narrativa e CTA, respeitando o tom corporativo.
category: marketing
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/artigo-blog
  - marketing/conteudo-site
version: 0.1.0
status: rascunho
---

# Conteúdo LinkedIn

## Objetivo
Criar posts para LinkedIn com gancho inicial atrativo, desenvolvimento curto, exemplo concreto e CTA.

## Quando usar
- Posicionamento da empresa.
- Divulgação de cases.
- Comunicação de marcos.
- Autoridade técnica.

## Quando NÃO usar
- Para conteúdo institucional completo (usar `marketing/conteudo-site`).
- Para artigos longos (usar `marketing/artigo-blog`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `tema` | string | sim |
| `publico` | string | sim |
| `formato` | enum | sim |
| `gancho` | string | não |
| `cta` | string | sim |
| `hashtags` | lista | não |

## Saídas esperadas
- Versão do post (até 1300 caracteres).
- Hashtags sugeridas.
- Variação com pergunta aberta.

## Fluxo interno
1. Definir tema e formato (reflexão, case, dica, lançamento).
2. Construir gancho (1ª linha crítica).
3. Desenvolver em 3-5 blocos curtos.
4. Inserir exemplo concreto.
5. Fechar com CTA.

## Boas práticas
- 1ª linha com ≤ 12 palavras e impacto.
- Frases curtas.
- Espaçamento entre blocos.
- Hashtags 3-5 relevantes.

## Limitações
- Não publica automaticamente.
- Não analisa métricas.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- LinkedIn Scheduler
- Buffer