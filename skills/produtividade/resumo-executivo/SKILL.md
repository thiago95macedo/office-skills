---
name: resumo-executivo
description: Use para produzir resumo executivo de documento longo (relatório, ata, proposta, estudo) com foco em decisões e números.
category: produtividade
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - gestao/dashboard-executivo
  - _core/organizador-informacao
version: 0.1.0
status: rascunho
---

# Resumo Executivo

## Objetivo
Sintetizar documentos longos em resumo executivo de 1 página, destacando conclusões, dados-chave e decisões.

## Quando usar
- Leitura de relatório extenso.
- Briefing para diretoria.
- Anexo de e-mail.

## Quando NÃO usar
- Para documento curto (resumo seria redundante).
- Para reorganizar (usar `_core/organizador-informacao`).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `documento` | texto | sim |
| `extensao_resumo` | enum | sim |
| `foco` | enum | sim |
| `publico` | string | sim |

## Saídas esperadas
- Resumo de até 1 página.
- Bullets de conclusões.
- Números-chave destacados.
- Recomendações (quando aplicável).

## Fluxo interno
1. Ler documento.
2. Identificar conclusões e números.
3. Selecionar top-5 bullets.
4. Aplicar tom corporativo.
5. Limitar a 1 página.

## Limitações
- Não realiza fact-checking.
- Não substitui leitura completa em decisões críticas.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- PDF readers
- Notion
## Secoes de referencia (geradas)

Descricao desta Skill: Use para produzir resumo executivo de documento longo (relatório, ata, proposta, estudo) com foco em decisões e números.

## Boas práticas

Listar recomendacoes de uso da Skill.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

