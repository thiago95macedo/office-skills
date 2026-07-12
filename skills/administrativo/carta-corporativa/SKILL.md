---
name: carta-corporativa
description: Use para produzir cartas formais externas (agradecimentos, parcerias, representatividade, solicitações institucionais).
category: administrativo
priority: opcional
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/oficio-memorando
  - comercial/proposta-comercial
version: 0.2.0
status: estavel
references:
  - BRASIL. Manual de Redação da Presidência da República. 3. ed. 2018.
  - Lage, N. Manual de Redação e Estilo. 1985.
---

# Carta Corporativa

## Objetivo
Redigir cartas formais externas para diferentes finalidades, mantendo timbre institucional, formalidade e cordialidade.

## Quando usar
- Agradecimento institucional (visita, parceria, contribuição).
- Apresentação formal de nova área, produto ou serviço.
- Solicitação institucional (apoio, patrocínio, parceria).
- Comunicação com stakeholders externos (clientes VIP, governo,行业协会).
- Convite formal para evento corporativo de alto nível.

## Quando NÃO usar
- Para comunicação interna (usar `email-corporativo` ou `comunicado-interno`).
- Para correspondência oficial da administração pública (usar Manual de Redação da Presidência).
- Para mensagem rápida ou transacional (canal informal).

## Tipos de carta corporativa

| Tipo | Finalidade | Tom |
|------|-----------|-----|
| **Apresentação** | Apresentar empresa, área ou serviço | Formal e informativo |
| **Agradecimento** | Reconhecer contribuição, visita ou parceria | Formal e caloroso |
| **Solicitação** | Pedir apoio, patrocínio ou recurso | Formal e respeitoso |
| **Representatividade** | Falar em nome da empresa em evento externo | Formal e protocolar |
| **Parceria** | Formalizar início de colaboração | Formal e cordial |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Timbre** | Logomarca, endereço, CNPJ, telefone, site |
| 2 | **Local e data** | Cidade, dia, mês, ano por extenso |
| 3 | **Destinatário** | Nome, cargo, empresa, endereço completo |
| 4 | **Assunto** (opcional) | Resumo do tema em 1 linha |
| 5 | **Vocativo** | "Prezado(a) Sr(a). [Nome]" ou "Senhor(a) [Cargo]" |
| 6 | **Corpo** | Abertura, desenvolvimento, fechamento (3-5 parágrafos curtos) |
| 7 | **Fecho** | "Atenciosamente," |
| 8 | **Assinatura** | Nome, cargo, contato |
| 9 | **Iniciais de protocolização** | Siglas do autor/redator na margem inferior (ex: "JMS/mrs") |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `finalidade` | enum | sim | apresentação / agradecimento / solicitacao / representatividade / parceria |
| `destinatario` | dict | sim | Nome, cargo, empresa, endereço |
| `conteudo` | string | sim | Mensagem central (tema e pontos-chave) |
| `remetente` | dict | sim | Nome, cargo, contato |
| `tom` | enum | sim | formal / semiformal |
| `anexos` | lista | não | Documentos anexos |
| `prazo_resposta` | string | não | Prazo sugerido para retorno |

## Saídas esperadas
Carta Markdown com:
- Timbre institucional (logo + dados)
- Local e data por extenso
- Destinatário completo
- Vocativo
- 3-5 parágrafos de corpo (≤ 6 linhas cada)
- Fecho padronizado
- Assinatura completa
- Lista de anexos (quando houver)
- Iniciais de protocolização

## Fluxo interno
1. Carregar timbre e dados institucionais de `config/empresa.yaml`.
2. Confirmar tipo (apresentação, agradecimento, etc.) e tom.
3. Receber destinatário completo (nome, cargo, empresa, endereço).
4. Redigir vocativo conforme hierarquia.
5. Estruturar corpo: abertura contextual → desenvolvimento → fechamento cordial.
6. Aplicar linguagem formal e impessoal (sem gírias, sem coloquialismos).
7. Inserir fecho e assinatura institucional.
8. Listar anexos quando houver.
9. Validar ortografia, formatação da data, clareza.
10. Sugerir versão para impressão em papel timbrado.

## Boas práticas
- Linguagem formal, impessoal, clara.
- Parágrafos curtos (máximo 6 linhas cada).
- Tom adequado ao tipo (caloroso para agradecimento, respeitoso para solicitação).
- Vocativo conforme gênero do destinatário ("Prezada Sra." ou "Prezado Sr.").
- Data por extenso: "São Paulo, 12 de julho de 2026".
- Fecho: "Atenciosamente," (formal) ou "Cordialmente," (semiformal).
- Iniciais de protocolização (quem redigiu + quem digitou, ex: "JMS/mrs").
- Versão para impressão em papel timbrado (A4 com logo).
- Versão digital em PDF para e-mail.
- Revisão ortográfica e gramatical antes de enviar.
- Endereçamento postal correto (CEP, logradouro, complemento).

## Armadilhas comuns
- Misturar tom formal com coloquialismos ("a gente", "pra").
- Vocativo no plural para uma única pessoa.
- Data em formato numérico ambíguo.
- Corpo com parágrafos únicos muito longos.
- Falta de timbre ou dados da empresa.
- Falta de assinatura, cargo ou contato.
- Carta sem vocativo adequado à hierarquia do destinatário.
- Uso de "Atenciosamente" e "Cordialmente" sem critério.
- Envio de carta com erros ortográficos ou de formatação.
- Esquecer anexos mencionados no corpo.

## Limitações
- Não substitui correspondência jurídica formal (com valor contratual).
- Não verifica norma postal específica (CEP, porte).
- Não acessa base de endereços automaticamente.
- Não considera norma cultural específica do país do destinatário (carta internacional).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Carta de agradecimento institucional
- `02-intermediario.md` — Carta de apresentação de parceria
- `03-avancado.md` — Carta de solicitação de patrocínio

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Processadores de texto (Microsoft Word, Google Docs, LibreOffice)
- Modelos de papel timbrado (templates da empresa)
- Sistemas de envio postal (Correios, plataformas de postagem)
- Assinatura digital (DocuSign, Clicksign)