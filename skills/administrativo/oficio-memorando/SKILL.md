---
name: oficio-memorando
description: Use para produzir ofícios e memorandos internos formais, com numeração, destinatário, assunto, conteúdo e assinatura.
category: administrativo
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - administrativo/email-corporativo
  - administrativo/comunicado-interno
version: 0.2.0
status: estavel
references:
  - BRASIL. Manual de Redação da Presidência da República. 3. ed. 2018.
  - ABNT NBR 14724 — Trabalhos acadêmicos (estrutura referencial).
  - ABNT NBR 6028 — Resumo (norma correlata).
---

# Ofício / Memorando

## Objetivo
Padronizar comunicações formais internas com estrutura rígida, numeração sequencial e auditabilidade, conforme padrões da administração pública e corporativa.

## Quando usar
- Comunicação formal entre unidades da mesma organização (memorando).
- Comunicação formal com órgãos externos (ofício).
- Documentação de decisões ou solicitações que precisam de rastreabilidade.
- Cumprimento de requisito regulatório ou contratual.

## Quando NÃO usar
- Para comunicação rápida (usar `email-corporativo`).
- Para divulgação ampla sem destinatário específico (usar `comunicado-interno`).
- Para documentos com força contratual (usar minuta jurídica com revisão especializada).

## Diferenças: Ofício x Memorando

| Aspecto | Ofício | Memorando |
|---------|--------|-----------|
| Destinatário | Externo (outro órgão, empresa, pessoa) | Interno (mesma organização) |
| Numeração | Sequencial anual por órgão expedidor | Sequencial por unidade ou geral |
| Forma de tratamento | "Senhor(a)" / "Prezado(a)" | Mais flexível, mas impessoal |
| Padrão | Manual de Redação da Presidência (3ª ed.) | Padrão interno da organização |
| Anexo comum | Documentos comprobatórios | Cópias para conhecimento |

## Estrutura recomendada (Manual de Redação da Presidência + ABNT)

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Timbre, brasão ou logo da organização |
| 2 | **Número** | Sequencial (Ofício nº 123/AAAA ou Memorando nº 45/AAAA) |
| 3 | **Local e data** | Cidade, dia, mês, ano por extenso |
| 4 | **Tipo e natureza** | "Ofício" ou "Memorando" |
| 5 | **Destinatário** | Nome, cargo, instituição, endereço |
| 6 | **Assunto** | Resumo do tema em até 1 linha (destacado) |
| 7 | **Vocativo** | "Senhor(a) [Cargo]", "Prezado(a) Sr(a)." |
| 8 | **Corpo** | Abertura, desenvolvimento, fechamento |
| 9 | **Fecho** | "Atenciosamente," |
| 10 | **Assinatura** | Nome, cargo, matrícula (quando aplicável) |
| 11 | **Anexos** | Lista de documentos anexos (se houver) |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tipo` | enum | sim | oficio \| memorando |
| `numero` | string | sim | Sequencial (ex: 123/AAAA) |
| `destinatario` | dict | sim | Nome, cargo, instituição, endereço |
| `assunto` | string | sim | Resumo do tema |
| `conteudo` | string | sim | Mensagem central |
| `anexos` | lista | não | Documentos anexos |
| `remetente` | dict | sim | Nome, cargo, matrícula do signatário |
| `prazo_resposta` | string | não | Prazo sugerido para retorno |

## Saídas esperadas
Documento Markdown com:
- Cabeçalho institucional
- Numeração sequencial datada
- Local e data por extenso
- Destinatário completo
- Assunto destacado
- Corpo impessoal
- Fecho e assinatura padronizados
- Lista de anexos (quando aplicável)

## Fluxo interno
1. Carregar timbre e dados institucionais de `config/empresa.yaml`.
2. Confirmar tipo (ofício ou memorando) e número sequencial.
3. Definir destinatário completo (nome, cargo, instituição, endereço).
4. Redigir assunto em até 1 linha (substantivo + complemento).
5. Selecionar vocativo conforme hierarquia e tom.
6. Estruturar corpo em 3 parágrafos: contexto → solicitação/exposição → fechamento cortês.
7. Aplicar linguagem impessoal ("subscrito", "solicita-se", "informa-se").
8. Inserir fecho padrão e assinatura.
9. Listar anexos quando houver.
10. Validar checklist (numeração, data, formalidade, ausência de marcas pessoais).

## Boas práticas
- Linguagem impessoal e objetiva (sem "eu", "você").
- Parágrafos curtos (máximo 6 linhas cada).
- Numeração sequencial anual bem controlada.
- Sem ambiguidade: cada frase tem significado único.
- Assunto claro e específico (não usar "Assunto diversos").
- Data completa por extenso: "São Paulo, 12 de julho de 2026".
- Fecho padronizado: "Atenciosamente," (corrigido conforme Manual de Redação).
- Verbo no pretérito ou presente do indicativo.
- Sem adjetivos vazios ("cordialmente solicitando", "com a devida vênia" — só quando juridicamente apropriado).
- Sem rasuras ou correções visíveis.
- Versão digital assinada eletronicamente quando aplicável.

## Armadilhas comuns
- Confundir ofício com memorando (externo × interno).
- Assunto genérico ("Referente ao assunto").
- Vocativo errado ("Prezados" para uma pessoa; "Senhor" para mulher).
- Misturar "Atenciosamente" e "Cordialmente" sem critério.
- Fechos inadequados ("Beijos", "Abraços", "T+").
- Data em formato numérico ambíguo (07/12/26).
- Falta de assinatura, cargo ou matrícula.
- Corpo com parágrafos únicos muito longos.

## Limitações
- Não substitui parecer jurídico para temas contratuais.
- Não verifica conformidade com regimento interno específico.
- Não emite protocolo (sistema de numeração deve estar conectado).
- Não verifica adequação hierárquica do remetente.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Memorando interno entre áreas
- `02-intermediario.md` — Ofício para órgão público
- `03-avancado.md` — Ofício com anexos múltiplos

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Sistema de protocolo (SEI, SAP, sistemas internos)
- GED (SharePoint, Docuware, TOTVS)
- Assinatura eletrônica (ICP-Brasil, DocuSign, Clicksign)
- Plataformas de processo eletrônico (PROJUDI, PJe)