---
name: ata-reuniao
description: Use para documentar reunião em ata estruturada (participantes, pauta, decisões, ações, próxima reunião).
category: administrativo
priority: essencial
depends_on:
  - _core/organizador-informacao
composes_with:
  - gestao/plano-acao
  - produtividade/transcricao-tarefas
version: 0.1.0
status: rascunho
---

# Ata de Reunião

## Objetivo
Documentar formalmente os assuntos tratados em reunião, garantindo rastreabilidade das decisões.

## Entradas
- `notas_reuniao` (string)
- `participantes` (lista)
- `data_hora_local` (dict)

## Saída
Ata com: cabeçalho, participantes, pauta, discussões, decisões, ações, próxima reunião, assinaturas.

## Boas práticas
- Decisões em frases declarativas.
- Ações com responsável e prazo.
- Próxima reunião com data confirmada.