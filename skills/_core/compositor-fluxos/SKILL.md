---
name: compositor-fluxos
description: Use para encadear várias Skills em um fluxo ordenado, com transferência explícita de saídas como entradas.
category: _core
priority: essencial
depends_on:
  - _core/configurador-empresa
composes_with:
  - qualquer outra Skill da biblioteca
version: 0.1.0
status: rascunho
---

# Compositor de Fluxos

## Objetivo
Permitir composição ordenada de Skills, transformando a saída de uma Skill na entrada estruturada da próxima.

## Quando usar
- Automatizar rotinas que exigem várias Skills em sequência (ex.: proposta comercial: redator + orcamento + escopo).
- Construir pipelines reutilizáveis.

## Quando NÃO usar
- Quando uma única Skill resolve.
- Quando as Skills não compartilham contrato.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `passos` | lista | sim | Lista ordenada de Skills a executar |
| `contexto_inicial` | dict | sim | Variáveis iniciais (empresa, dados) |
| `politica_erro` | enum | não | "abortar" / "continuar" |

## Saídas esperadas
- Artefatos intermediários de cada Skill.
- Artefato final consolidado.
- Log de execução.

## Fluxo interno
1. Carregar `config/empresa.yaml`.
2. Iterar passos em ordem.
3. Mapear saída → entrada conforme contrato.
4. Aplicar política de erro.
5. Entregar artefato final + log.

## Limitações
- Não gerencia execução paralela (a menos que explicitamente configurado).
- Não retém estado entre execuções.