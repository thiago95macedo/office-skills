---
name: descricao-vaga
description: Use para redigir descrições de vaga objetivas, atrativas e alinhadas à cultura da empresa.
category: rh
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - rh/treinamento-materiais
  - marketing/conteudo-linkedin
version: 0.1.0
status: rascunho
---

# Descrição de Vaga

## Objetivo
Produzir descrição de vaga completa, com propósito do cargo, responsabilidades, requisitos, diferenciais e benefícios.

## Quando usar
- Abertura de nova posição.
- Reposição de vaga.
- Estruturação de programa de estágio/trainee.

## Quando NÃO usar
- Para descrição interna sucinta (usar memorando simples).

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `cargo` | string | sim |
| `area` | string | sim |
| `reporta_para` | string | sim |
| `missao` | string | sim |
| `responsabilidades` | lista | sim |
| `requisitos_obrigatorios` | lista | sim |
| `requisitos_diferenciais` | lista | não |
| `beneficios` | lista | sim |
| `modelo_trabalho` | enum | sim |

## Saídas esperadas
- Título da vaga.
- Sobre a empresa.
- Propósito do cargo.
- Responsabilidades.
- Requisitos obrigatórios e diferenciais.
- Benefícios.
- Modelo de trabalho.
- Como se candidatar.

## Fluxo interno
1. Receber dados da vaga.
2. Redigir propósito em frase concisa.
3. Listar responsabilidades (verbos no infinitivo).
4. Separar obrigatórios de diferenciais.
5. Apresentar benefícios de forma atrativa sem exagero.

## Boas práticas
- Linguagem inclusiva.
- Sem discriminação velada.
- Benefícios verificáveis.

## Limitações
- Não publica automaticamente em plataformas.

## Dependências
- `_core/redator-corporativo`

## Possíveis integrações
- Gupy, LinkedIn Jobs
- ATS interno
## Secoes de referencia (geradas)

Descricao desta Skill: Use para redigir descrições de vaga objetivas, atrativas e alinhadas à cultura da empresa.

## Exemplos de uso

Indicar que ha exemplos em examples/.

## Prompt interno recomendado

Indicar que o prompt detalhado esta em prompt.md.

