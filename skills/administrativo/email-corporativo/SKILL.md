---
name: email-corporativo
description: Use para redigir e-mails profissionais (externos ou internos) com tom, estrutura e tamanho adequados.
category: administrativo
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/comunicado-interno
  - comercial/follow-up
  - comercial/atendimento-lead
version: 0.2.0
status: estavel
references:
  - Muñoz, J. R. A arte de escrever bem. 2005.
  - Rilke, S. Letters to a Young Poet. 1929 (sobre concisão epistolar).
  - LGPD Lei 13.709/2018 — tratamento de dados pessoais.
---

# E-mail Corporativo

## Objetivo
Produzir e-mails profissionais (internos ou externos) com assunto claro, abertura cordial, conteúdo objetivo, CTA explícito e assinatura padronizada.

## Quando usar
- Resposta a cliente, fornecedor ou parceiro (externo).
- Comunicação interna com ação requerida (externo-interno).
- Acompanhamento de solicitação ou processo.
- Convite formal para reunião, evento ou apresentação.

## Quando NÃO usar
- Para comunicado amplo (usar `comunicado-interno`).
- Para mensagem rápida em chat corporativo (usar ferramenta de chat).
- Para notificação transacional automática (usar template de sistema).

## Estrutura recomendada

| Bloco | Orientação | Limite sugerido |
|-------|------------|-----------------|
| **Assunto** | Resumo objetivo do conteúdo | ≤ 8 palavras / ≤ 60 caracteres |
| **Pré-cabeçalho** (preview) | Complementa assunto | ≤ 90 caracteres |
| **Saudação** | Cordial e personalizada | 1 linha |
| **Contexto** | Por que está escrevendo | 1-2 frases |
| **Mensagem central** | Conteúdo principal | 1-3 parágrafos |
| **CTA** | Próximo passo desejado | 1 frase destacada |
| **Fechamento** | Cortesia | 1 linha ("Atenciosamente", "Cordialmente") |
| **Assinatura** | Nome, cargo, contatos, links | Bloco padronizado |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `destinatario` | string | sim | Nome do destinatário |
| `destinatario_email` | string | não | E-mail (se for envio direto) |
| `assunto` | string | sim | Linha de assunto |
| `mensagem_central` | string | sim | Conteúdo principal |
| `tom` | enum | sim | formal / semiformal / informal |
| `anexos` | lista | não | Lista de anexos referenciados |
| `prazo_resposta` | string | não | Prazo sugerido para retorno |
| `cta` | string | sim | Próximo passo desejado |

## Saídas esperadas
E-mail em Markdown com blocos:
- Assunto + pré-cabeçalho
- Saudação
- Corpo (contexto + mensagem + CTA)
- Fechamento
- Assinatura padronizada
- Lista de anexos (quando houver)

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom, assinatura padrão, contatos).
2. Validar assunto (≤ 8 palavras, sem CAIXA ALTA, sem emojis).
3. Definir saudação conforme tom ("Prezado Sr.", "Olá", etc.).
4. Estruturar corpo: contexto → mensagem → CTA.
5. Aplicar tom e remover `vocabulario_bloqueado`.
6. Inserir assinatura padrão (nome, cargo, empresa, telefone, LinkedIn).
7. Listar anexos explicitamente ("Segue em anexo: ...").
8. Validar LGPD: sem dados sensíveis sem necessidade.
9. Entregar versão limpa + observações opcionais.

## Boas práticas
- Assunto com ≤ 8 palavras, descritivo, sem CAIXA ALTA, sem "URGENTE!" desnecessário.
- Saudação personalizada (usar nome do destinatário quando conhecido).
- Corpo até 3 parágrafos principais; usar bullets quando ajudar.
- CTA explícito: o que você quer que o destinatário faça.
- Fechamento consistente: "Atenciosamente" (formal) ou "Cordialmente" (semiformal).
- Assinatura completa: nome, cargo, empresa, telefone, site, LinkedIn.
- Listar anexos explicitamente ("Segue em anexo: Proposta Comercial v2.pdf").
- Responder em até 24h (regra de netiqueta corporativa).
- **LGPD**: não enviar dados pessoais sensíveis sem necessidade; usar canais criptografados para isso.
- Evitar "Responder a todos" desnecessariamente; usar Cc/Bcc com critério.

## Armadilhas comuns
- Assunto vago ("Dúvida", "Importante", "Encaminhando") — destinatário não sabe do que se trata.
- E-mail longo demais — ninguém lê acima de 200 palavras sem motivo.
- Múltiplos assuntos em um único e-mail — fragmentar.
- Sem CTA — destinatário não sabe o que fazer.
- Anexos esquecidos ou sem referenciamento no corpo.
- Encaminhar e-mails com cabeçalhos enormes — limpar antes.
- Misturar assuntos profissionais e pessoais.
- Cc/Bcc mal utilizado (expor lista de distribuição).
- Reply All desnecessário.

## Limitações
- Não verifica ortografia multilíngue automaticamente.
- Não acessa calendário do destinatário para sugerir horários.
- Não envia e-mail automaticamente (gera conteúdo para revisão humana).
- Não avalia adequação jurídica (LGPD, compliance, sigilo bancário).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Resposta a cliente
- `02-intermediario.md` — Follow-up pós-reunião
- `03-avancado.md` — Cobrança diplomática

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Clientes de e-mail (Outlook, Gmail, Apple Mail)
- CRM (Pipedrive, HubSpot, Salesforce)
- Assinatura eletrônica (DocuSign, Clicksign)
- Trackers de e-mail (Mixmax, Yesware, Mailtrack)