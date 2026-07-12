---
name: encaminhamento-interno
description: Use para direcionar uma demanda para a área interna correta, com contexto suficiente e SLA sugerido.
category: atendimento
priority: recomendada
depends_on: []
composes_with:
  - atendimento/triagem-mensagens
  - atendimento/resposta-rapida
version: 0.2.0
status: estavel
references:
  - ITIL 4 — Service Request Management Practice Guide (PeopleCert/AXELOS).
  - Zendesk Support Benchmarks — Triage time + Routing time.
---

# Encaminhamento Interno

## Objetivo
Redigir mensagem de repasse de demanda para a área interna responsável, com contexto completo, SLA sugerido e próxima ação esperada.

## Quando usar
- Demanda que pertence a outra área (comercial, suporte, financeiro, RH).
- Escalonamento de ticket para nível 2/3.
- Encaminhamento de lead qualificado para SDR/AE.
- Distribuição para área técnica especializada.
- Triagem de e-mails em caixas compartilhadas.

## Quando NÃO usar
- Quando a demanda é da própria área (resolver localmente).
- Para comunicação simples sem contexto (usar `resposta-rapida` direto ao cliente).

## Estrutura recomendada

| Bloco | Conteúdo | Limite |
|-------|----------|--------|
| **Saudação e assunto** | Direto, indica tema | 1 linha |
| **Resumo da demanda** | Contexto em 3 frases | ≤ 60 palavras |
| **Histórico relevante** | Interações anteriores, ticket #, cliente | Resumo |
| **SLA esperado** | Prazo e prioridade | Explícito |
| **Próxima ação esperada** | O que a área destino deve fazer | 1-2 frases |
| **CTA** | Quando retornar / a quem reportar | 1 linha |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `demanda_original` | string | sim | Mensagem ou resumo da demanda |
| `area_destino` | string | sim | Área que deve receber (Comercial, Suporte N2, Financeiro, RH) |
| `responsavel_destino` | string | não | Pessoa específica (quando conhecida) |
| `contexto_cliente` | dict | sim | Nome, produto, histórico, valor |
| `sla_esperado` | string | sim | Prazo para retorno (ISO 8601 ou relativo: "em até 4h úteis") |
| `prioridade` | enum | sim | alta / media / baixa |
| `canal_interno` | enum | sim | Slack / Teams / E-mail / Sistema de tickets |
| `contexto_adicional` | string | não | Info extra relevante |

## Saídas esperadas
- Mensagem interna com saudação direta.
- Resumo da demanda em 3 frases.
- Contexto do cliente (ticket #, produto, histórico).
- SLA explícito.
- Próxima ação esperada.
- CTA com responsável e prazo.

## Fluxo interno
1. Carregar `config/empresa.yaml` (áreas, responsáveis padrão, SLAs).
2. Receber demanda original e contexto.
3. Identificar área destino (regra de triagem).
4. Resumir demanda em até 3 frases (sem repetir literalmente).
5. Incluir contexto do cliente relevante.
6. Definir SLA conforme política e prioridade.
7. Sugerir próxima ação esperada.
8. Redigir mensagem interna completa.
9. Indicar canal apropriado.

## Boas práticas
- **Resumo objetivo** — sem repetir literalmente a demanda original.
- **Contexto suficiente** — área destino não precisa buscar mais informação.
- **SLA explícito** — prazo em horas ou dias úteis.
- **Prioridade visível** — alta/média/baixa em destaque.
- **Ticket # quando existir** — rastreabilidade.
- **Próxima ação esperada** — não só "verificar".
- **Responsável claro** — pessoa ou papel.
- **Canal adequado** — Slack para urgente, ticket para formal.
- **Sem informação sensível em excesso** — LGPD: minimização.
- **Tracejamento** — confirmar que a área destino recebeu.

## Armadilhas comuns
- Resumir mal e a área destino perde tempo entendendo.
- Sem SLA definido — área destino não prioriza.
- Encaminhar para pessoa errada — retrabalho.
- Misturar demandas (encaminhar várias em uma mensagem só).
- Sem contexto do cliente — área destino fica perdida.
- Incluir dados sensíveis sem necessidade (viola LGPD).
- Encaminhar e esquecer — não acompanhar retorno.
- Sem feedback ao cliente original (cliente fica sem resposta).

## Limitações
- Não envia mensagem automaticamente.
- Não confirma leitura pela área destino.
- Não monitora SLA automaticamente.
- Não acessa organograma em tempo real.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Encaminhamento para suporte N2
- `02-intermediario.md` — Encaminhamento de lead qualificado para vendas
- `03-avancado.md` — Escalonamento de incidente crítico

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Sistemas de tickets (Zendesk, Jira Service Management, Freshdesk, Movidesk)
- Comunicação interna (Slack, Microsoft Teams, Google Chat)
- CRM (RD, HubSpot, Salesforce)
- Plataformas de workflow (Pipefy, BPM)