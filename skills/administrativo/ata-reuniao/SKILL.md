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
version: 0.2.0
status: estavel
references:
  - BRASIL. Manual de Redação da Presidência da República. 3. ed. 2018.
  - ABNT NBR ISO 8601 — Formato de data e hora.
  - Drucker, P. The Effective Executive. 1967 (sobre atas e follow-up).
---

# Ata de Reunião

## Objetivo
Documentar formalmente os assuntos tratados em reunião (presencial, virtual ou híbrida), garantindo rastreabilidade das decisões, ações e responsáveis.

## Quando usar
- Reuniões de comitê, diretoria ou conselho com decisões registradas.
- Reuniões de projeto com marcos definidos.
- Reuniões de alinhamento entre áreas que precisam de histórico.
- Reuniões contratuais, societárias ou assembleias (com ajustes).

## Quando NÃO usar
- Para alinhamentos rápidos sem necessidade de registro (usar resumo de chat).
- Para brainstorm (usar ata livre, sem estrutura formal).
- Para reuniões confidenciais com conteúdo sigiloso (usar ata restrita + termo de confidencialidade).

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Título, data, hora início/fim, local ou plataforma |
| 2 | **Convocação** | Quem convocou e meio (se relevante) |
| 3 | **Participantes** | Lista nominal com cargo/área, presenças e ausências justificadas |
| 4 | **Pauta** | Tópicos na ordem de discussão |
| 5 | **Discussões** | Resumo objetivo de cada tópico (fatos, não opiniões) |
| 6 | **Decisões** | Frases declarativas ("Aprovado...", "Definido...", "Decidido...") |
| 7 | **Ações** | Tabela: ação, responsável, prazo |
| 8 | **Próxima reunião** | Data, hora, local se já definida |
| 9 | **Aprovação** | Assinatura do presidente e do secretário da mesa |
| 10 | **Anexos** | Lista de documentos, slides, planilhas referenciados |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `notas_reuniao` | string | sim | Notas brutas ou transcrição |
| `participantes` | lista | sim | Nome, cargo, presença (P/F/J) |
| `data_hora_local` | dict | sim | Data ISO 8601, hora início/fim, local ou link |
| `pauta` | lista | sim | Tópicos tratados |
| `decisoes` | lista | sim | Decisões tomadas |
| `acoes` | lista | sim | Ações com responsável e prazo |
| `proxima_reuniao` | dict | não | Data e pauta da próxima |
| `anexos` | lista | não | Documentos referenciados |

## Saídas esperadas
Documento Markdown estruturado com:
- Cabeçalho com metadados (data, local, duração)
- Lista nominal de participantes
- Pauta na ordem tratada
- Discussões resumidas
- Decisões em frases declarativas
- Tabela de ações (responsável + prazo)
- Próxima reunião agendada
- Bloco de assinatura

## Fluxo interno
1. Carregar `config/empresa.yaml` (modelo institucional).
2. Receber notas brutas, transcrição ou tópicos falados.
3. Organizar cronologicamente pela pauta.
4. Distinguir fato de opinião (registrar apenas o que foi decidido, não debates longos).
5. Redigir decisões em frases declarativas ("Aprovado...", "Definido...").
6. Construir tabela de ações com responsável, prazo e indicador de entrega.
7. Definir próxima reunião (data, local, pauta preliminar).
8. Listar anexos (slides, planilhas, contratos).
9. Validar formatação ISO 8601 para data e hora.
10. Submeter para aprovação do secretário/presidente antes de distribuir.

## Boas práticas
- Linguagem impessoal ("foi decidido", "foi aprovado" — não "eu decidi", "o time quer").
- Decisões em frases declarativas e objetivas.
- Ações com responsável nominal e prazo explícito (formato ISO 8601).
- Próxima reunião com data confirmada, não "a definir".
- Discussões resumidas (2-3 frases por tópico), sem exaustividade.
- Siglas expandidas na primeira menção.
- Nomes próprios grafados corretamente (confirmar grafia).
- Marcar itens com divergência não resolvida ("pendente de alinhamento com X").
- Duração real registrada (hora início × hora fim).
- Aprovação por assinatura ou ata eletrônica (plataformas com aceite).

## Armadilhas comuns
- Ata redigida com viés ou juízo de valor sobre os participantes.
- Decisões vagas ("será estudado", "será avaliado") — definir responsável e prazo.
- Ações sem dono ou prazo ("a equipe vai ver").
- Misturar discussão com decisão (separar claramente).
- Não registrar divergências (perder rastreabilidade).
- Próxima reunião indefinida ("em breve").
- Erros de grafia em nomes e números.
- Pauta fora de ordem (não refletir sequência real).
- Atraso na distribuição (lembrar: ata deve ir aos participantes em até 5 dias úteis).

## Limitações
- Não substitui gravação/transcrição quando necessário (anexar link).
- Não verifica quorum (responsabilidade do presidente da mesa).
- Não tem valor jurídico sem assinatura e protocolização (quando aplicável).
- Não detecta conflitos de interesse ou vigência de procuração (responsabilidade da mesa).

## Dependências
- `_core/organizador-informacao`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Reunião de equipe semanal
- `02-intermediario.md` — Comitê de projeto
- `03-avancado.md` — Reunião de diretoria com decisões estratégicas

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Calendário corporativo (Google Calendar, Outlook)
- Ferramentas de videoconferência (Zoom, Teams, Meet) com gravação
- GED (SharePoint, Notion, Confluence)
- Sistemas de gestão de tarefas (Asana, Trello, Jira) — para ações da ata
- Plataformas de assinatura (DocuSign, Clicksign)