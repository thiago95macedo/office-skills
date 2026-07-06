---
name: organizador-informacao
description: Use quando houver informação dispersa, desorganizada ou redundante que precise virar um documento estruturado (atas, briefings, relatórios, FAQs).
category: _core
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/ata-reuniao
  - produtividade/resumo-executivo
  - suporte/classificador-tickets
  - conhecimento/classificador-documentos
version: 0.1.0
status: rascunho
---

# Organizador de Informação

## Objetivo
Transformar conteúdo bruto (notas soltas, transcrições, e-mails, tópicos) em documentos estruturados, sem perder informação relevante.

## Quando usar
- Compilar informações de várias fontes em um único documento.
- Reorganizar notas de reunião em ata.
- Construir briefing a partir de documentos extensos.

## Quando NÃO usar
- Quando a fonte já está bem estruturada.
- Para resumir (usar `produtividade/resumo-executivo`).

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `fontes` | lista | sim | Textos brutos a organizar |
| `objetivo_documento` | texto | sim | Finalidade do documento final |
| `template_saida` | texto | não | Modelo de saída (default: estruturado padrão) |

## Saídas esperadas
Documento Markdown com seções lógicas, agrupamento por afinidade e eliminação de redundâncias.

## Fluxo interno
1. Receber fontes brutas.
2. Identificar temas recorrentes.
3. Agrupar informações por afinidade.
4. Eliminar duplicidades.
5. Ordenar logicamente (cronologia, prioridade ou hierarquia).
6. Aplicar tom corporativo.

## Boas práticas
- Preservar dados quantitativos sempre que presentes.
- Sinalizar suposições quando a fonte for ambígua.
- Citar a fonte original em parênteses quando relevante.

## Limitações
- Não realiza fact-checking automático.
- Não traduz.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- Notion
- Confluence
- SharePoint