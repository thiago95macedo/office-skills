---
name: case-de-sucesso
description: Use para estruturar cases de sucesso a partir de resultados reais do cliente.
category: marketing
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-linkedin
  - marketing/conteudo-site
version: 0.1.0
status: rascunho
---

# Case de Sucesso

## Objetivo
Construir narrativa de case com contexto, desafio, solução, resultados mensuráveis e depoimento.

## Quando usar
- Após projeto bem-sucedido.
- Para uso comercial e institucional.
- Para pitch e propostas.

## Quando NÃO usar
- Para case sem aprovação do cliente.
- Para case sem resultados mensuráveis.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `cliente` | dict | sim |
| `desafio` | string | sim |
| `solucao` | string | sim |
| `resultados` | lista | sim |
| `depoimento` | string | não |
| `aprovacao_cliente` | boolean | sim |

## Saídas esperadas
- Resumo do case.
- Contexto.
- Desafio.
- Solução aplicada.
- Resultados mensuráveis.
- Depoimento (se houver).
- Próximos passos.

## Fluxo interno
1. Confirmar aprovação do cliente.
2. Estruturar narrativa.
3. Quantificar resultados.
4. Coletar depoimento (se houver).
5. Revisar com cliente.

## Boas práticas
- Resultados com dados.
- Aprovação formal do cliente.
- Linguagem sóbria, sem exagero.

## Limitações
- Não entrevista o cliente.
- Não coleta métricas automaticamente.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- CRM
- Site
## Secoes de referencia (geradas)

Descricao desta Skill: Use para estruturar cases de sucesso a partir de resultados reais do cliente.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

