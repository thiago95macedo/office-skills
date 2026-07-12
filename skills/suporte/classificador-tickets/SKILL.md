---
name: classificador-tickets
description: Use para classificar tickets de suporte por categoria ITIL, prioridade (Impacto × Urgência) e produto/área.
category: suporte
priority: essencial
depends_on: []
composes_with:
  - suporte/faq-tecnico
  - suporte/base-conhecimento
  - atendimento/triagem-mensagens
version: 0.2.0
status: estavel
references:
  - ITIL 4 — Incident Management Practice Guide (PeopleCert/AXELOS).
  - HDI Support Center Standards (Informa TechTarget).
  - KCS® v6 Practices Guide — Consortium for Service Innovation.
  - BRASIL. LGPD Lei 13.709/2018 (categoria especial de dados).
---

# Classificador de Tickets

## Objetivo
Classificar tickets de suporte por categoria ITIL (Incidente, Solicitação de Serviço, Problema, Mudança), prioridade (Impacto × Urgência) e produto/área, sugerindo SLA e artigo relacionado.

## Quando usar
- Triagem automática de tickets omnichannel (e-mail, chat, WhatsApp, telefone).
- Auto-classificação no help desk.
- SLA inicial baseado em regras.
- Roteamento para fila ou agente correto.
- Integração com IA conversacional.

## Quando NÃO usar
- Quando o ticket já vem classificado por canal integrado.
- Para problemas muito específicos que exigem engenheiro (encaminhar como já classificado).

## Categorias ITIL 4

| Tipo | Definição | Exemplo |
|------|-----------|---------|
| **Incidente** | Interrupção não planejada ou redução de qualidade | Sistema fora do ar |
| **Solicitação de Serviço** | Pedido predefinido do usuário | Reset de senha |
| **Problema** | Causa raiz de um ou mais incidentes | Bug recorrente |
| **Mudança** | Adição/modificação/remoção que pode afetar o serviço | Atualização de sistema |
| **Consulta / Pedido de Informação** | Dúvida genérica | Como usar funcionalidade |

## Matriz Prioridade = Impacto × Urgência

| | **Urgência Alta** | **Urgência Média** | **Urgência Baixa** |
|---|---|---|---|
| **Impacto Alto** (muitos usuários/serviços críticos) | P1 (Crítico) | P2 (Alto) | P3 (Médio) |
| **Impacto Médio** (departamento ou grupo) | P2 (Alto) | P3 (Médio) | P4 (Baixo) |
| **Impacto Baixo** (usuário individual) | P3 (Médio) | P4 (Baixo) | P5 (Planejamento) |

**SLA sugerido (ITIL alinhado):**

| Prioridade | Resposta inicial | Resolução alvo |
|------------|------------------|----------------|
| P1 | Imediata / 15 min | 4h |
| P2 | 30 min | 8h |
| P3 | 2h | 24h |
| P4 | 4h | 72h |
| P5 | 8h | Próximo ciclo |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `descricao` | string | sim | Texto do ticket |
| `canal` | enum | sim | email / chat / whatsapp / telefone / portal |
| `cliente_vip` | bool | não | Cliente prioritário (escalonar) |
| `usuarios_afetados` | int | não | Quantos usuários impactados |
| `regras_categorizacao` | dict | sim | Regras de negócio (palavras-chave, mapeamentos) |
| `historico_cliente` | dict | não | Tickets anteriores do mesmo cliente |

## Saídas esperadas
- Tipo ITIL (Incidente / Solicitação / Problema / Mudança / Consulta).
- Categoria funcional (ex: "Acesso/Login", "Performance", "Integração").
- Prioridade P1-P5.
- SLA sugerido.
- Produto/área responsável.
- Sugestão de artigo da base de conhecimento.
- Sinalização de cliente VIP.
- Alerta para LGPD (se houver dados sensíveis).

## Fluxo interno
1. Carregar regras de categorização de `config/empresa.yaml`.
2. Receber descrição e metadados do ticket.
3. Detectar palavras-chave (login, erro, lento, cobrança, etc.).
4. Mapear para tipo ITIL.
5. Identificar categoria funcional.
6. Calcular prioridade por Impacto × Urgência.
7. Sugerir SLA baseado em prioridade.
8. Mapear para produto/área responsável.
9. Sugerir artigos relacionados da base.
10. Sinalizar cliente VIP, LGPD, ou exceções.

## Boas práticas
- **Regras explícitas** — não inferir com LLM apenas (combinar com regras).
- **Cliente VIP** — escalação automática (B2B: contas-chave).
- **LGPD** — sinalizar quando ticket contém dados sensíveis (saúde, financeiro, criança).
- **Falso positivo** — palavras-chave genéricas ("erro") exigem análise adicional.
- **Histórico do cliente** — reincidência eleva prioridade.
- **SLA documentado** — sempre visível no ticket.
- **Categorização estável** — evitar mudança de categoria durante ciclo.
- **Auto-aprendizado** — corrigir classificações errôneas (KCS).
- **Idioma** — classificar corretamente PT-BR vs. PT-PT vs. EN.
- **Encaminhamento inteligente** — fila correta, não só primeira opção.

## Armadilhas comuns
- Classificação incorreta por palavra-chave ambígua.
- Prioridade subestimada em cliente VIP.
- Não detectar LGPD (dados sensíveis tratados sem cuidado).
- SLA genérico (sem considerar contrato ou criticidade).
- Reclassificação durante atendimento (gera ruído).
- Não registrar histórico (reincidência não detectada).
- Categoria inexistente — agente fica perdido.

## Limitações
- Não acessa telemetria de sistemas automaticamente.
- Não classifica anexos binários (logs, screenshots exigem OCR).
- Não substitui triagem humana para tickets ambíguos.
- Não detecta sarcasmo ou ironia.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Classificação de ticket simples (reset de senha)
- `02-intermediario.md` — Incidente com múltiplos usuários
- `03-avancado.md` — Escalação por LGPD + cliente VIP

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Sistemas de tickets (Zendesk, Jira Service Management, Freshdesk, Movidesk)
- Plataforma de chatbot (Watson, Dialogflow, Blip)
- Knowledge base (Confluence, Notion, Document360)
- CRM (HubSpot Service, Salesforce Service Cloud)