---
name: onboarding
description: Use para planejar e acompanhar a integração de novo colaborador nos primeiros 30/60/90 dias.
category: rh
priority: recomendada
depends_on:
  - gestao/plano-acao
composes_with:
  - rh/descricao-vaga
  - rh/treinamento-materiais
version: 0.1.0
status: rascunho
---

# Onboarding

## Objetivo
Estruturar plano de integração com marcos em 30, 60 e 90 dias, garantindo acolhimento, treinamento e produtividade.

## Quando usar
- Admissão de novo colaborador.
- Mudança de área/promoção interna.
- Programa de estágio.

## Quando NÃO usar
- Para colaboradores experientes em mudança lateral simples.

## Entradas esperadas
| Campo | Tipo | Obrigatório |
|-------|------|-------------|
| `colaborador` | dict | sim |
| `cargo` | string | sim |
| `gestor` | string | sim |
| `buddy` | string | não |
| `trilha_conhecimento` | lista | sim |
| `marcos_personalizados` | dict | não |

## Saídas esperadas
- Boas-vindas (mensagem).
- Agenda da primeira semana.
- Marcos 30/60/90 dias com entregas e critérios.
- Trilha de treinamentos.
- Check-ins agendados.

## Fluxo interno
1. Receber dados do colaborador.
2. Estruturar primeira semana (dia 1 a dia 5).
3. Listar marcos de 30, 60 e 90 dias.
4. Definir critérios de avaliação de cada marco.
5. Sugerir agenda de check-ins.

## Boas práticas
- Acolhimento humano explícito.
- Treinamentos priorizados.
- Acompanhamento do gestor em frequência definida.

## Limitações
- Não substitui plano de desenvolvimento individual (PDI) completo.

## Dependências
- `gestao/plano-acao`

## Possíveis integrações
- HRIS
- LMS