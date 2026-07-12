---
name: comunicado-interno
description: Use para comunicar mudanças, decisões ou fatos relevantes para colaboradores internos.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
  - rh/onboarding
version: 0.2.0
status: estavel
references:
  - Drucker, P. Management Challenges for the 21st Century. 1999.
  - Heath, C.; Heath, D. Made to Stick. 2007 (sobre comunicação que fixa).
---

# Comunicado Interno

## Objetivo
Informar mudanças, decisões ou fatos relevantes à empresa de forma clara, uniforme, rastreável e com CTA explícito (ação esperada do colaborador).

## Quando usar
- Mudanças estruturais (reorganização, novos processos, ferramentas).
- Decisões que afetam a rotina dos colaboradores.
- Marcos ou resultados relevantes da empresa.
- Lançamento de programa interno (benefício, treinamento, política).
- Avisos urgentes ou de segurança.

## Quando NÃO usar
- Para comunicação individual ou 1:1 (usar `feedback-constructivo` ou `email-corporativo`).
- Para comunicado oficial do CEO (usar canal institucional com aprovação da diretoria).
- Para informações confidenciais ou estratégicas sensíveis (canal restrito).

## Estrutura recomendada (5 blocos)

| Bloco | Conteúdo | Orientação |
|-------|----------|------------|
| **1. Contexto** | Por que estamos comunicando | 1-2 frases |
| **2. O que muda** | Mudança concreta | Bullet claro |
| **3. O que NÃO muda** | Garantir estabilidade | Bullet claro |
| **4. Por que importa** | Impacto no colaborador ou negócio | 1-2 frases |
| **5. Próximos passos / CTA** | Ação esperada, prazo, canal de dúvidas | Explícito |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `publico` | string | sim | Quem recebe (todos, área X, cargo Y) |
| `mensagem_central` | string | sim | Conteúdo principal |
| `tom` | enum | sim | formal / semiformal / informal |
| `canal` | enum | sim | mural / email / intranet / Slack/Teams |
| `data_publicacao` | data | sim | Data de veiculação (ISO 8601) |
| `cta` | string | sim | Ação esperada do colaborador |
| `prazo_duvidas` | string | não | Onde e até quando esclarecer dúvidas |
| `origem` | dict | não | Quem está comunicando (autor, área) |

## Saídas esperadas
Comunicado Markdown com:
- Cabeçalho (origem, data, versão)
- 5 blocos padrão
- CTA destacado
- Rodapé com canal de dúvidas
- Tags opcionais para categorização

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom e formato institucional).
2. Receber mensagem central e público-alvo.
3. Estruturar 5 blocos: contexto, o que muda, o que não muda, impacto, CTA.
4. Aplicar tom conforme público (formal para toda empresa, semiformal para área).
5. Selecionar CTA mais objetivo ("A partir de dd/mm, todos os pedidos serão feitos via X").
6. Indicar canal e prazo para dúvidas.
7. Validar checklist (clareza, ausência de ambiguidade, tom, CTA).
8. Sugerir formato por canal (mural curto, e-mail expandido, intranet com anexos).

## Boas práticas
- **Mensagem única** por comunicado — não misturar temas.
- **O que muda vs o que NÃO muda** — reduz ansiedade da mudança.
- **Por que importa** — colaboradores entendem o "wIIFM" (what's in it for me).
- **CTA explícito** — o que o colaborador deve fazer (ou não fazer).
- **Data de início da mudança** sempre explícita.
- **Canal de dúvidas** com responsável e prazo.
- **Linguagem simples** — evitar jargão corporativo.
- **Tamanho proporcional à urgência** — comunicado urgente curto.
- **Confirmação de leitura** quando crítico (compliance, segurança).
- **Acessibilidade** — formato compatível com leitores de tela, contraste adequado.

## Armadilhas comuns
- Comunicado ambíguo ("em breve traremos mais informações" — sem prazo).
- Misturar boas e más notícias sem estrutura (ansiedade desnecessária).
- Tom corporativo vazio ("Estamos comprometidos com a excelência") sem conteúdo.
- Sem CTA — colaboradores não sabem o que fazer.
- Distribuição sem segmentação (todos recebem o que é de área específica).
- Ignorar impacto emocional (mudanças estruturais pedem cuidado).
- Não responder perguntas no prazo prometido.
- Versão "definitiva" enviada antes da aprovação da liderança.

## Limitações
- Não verifica conformidade com políticas internas de comunicação.
- Não valida necessidade de comunicação formal via Diretoria/Compliance.
- Não garante leitura ou compreensão pelo público.
- Não substitui treinamento quando a mudança exigir capacitação.
- Não considera restrições de sigilo ou compliance (LGPD, controles internos).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Lançamento de benefício
- `02-intermediario.md` — Migração de ferramenta
- `03-avancado.md` — Reorganização estrutural

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- E-mail corporativo (Outlook, Gmail)
- Intranet (SharePoint, Notion, Confluence)
- Slack / Microsoft Teams (canais oficiais)
- Murais físicos (versão para impressão)
- Plataformas de RH (HRIS, BambooHR, Pontotel)