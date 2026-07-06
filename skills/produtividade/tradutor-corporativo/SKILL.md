---
name: tradutor-corporativo
description: Use para traduzir textos preservando tom corporativo, terminologia técnica e estilo.
category: produtividade
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/artigo-blog
  - marketing/conteudo-site
version: 0.1.0
status: rascunho
---

# Tradutor Corporativo

## Objetivo
Traduzir textos mantendo terminologia técnica, tom corporativo e estilo da empresa.

## Quando usar
- Documentação técnica multilíngue.
- Site institucional multilíngue.
- E-mails com clientes internacionais.

## Quando NÃO usar
- Para tradução juramentada (usar serviço especializado).
- Para tradução literária.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `texto_origem` | string | sim |
| `idioma_destino` | string | sim |
| `glossario` | dict | sim |
| `tom` | enum | sim |

## Saídas esperadas
- Texto traduzido.
- Termos do glossário aplicados.
- Notas sobre decisões de tradução.

## Limitações
- Não traduz imagens.
- Não certifica tradução juramentada.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- CAT tools
- TMS