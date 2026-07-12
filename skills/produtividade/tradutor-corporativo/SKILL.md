---
name: tradutor-corporativo
description: Use para traduzir textos preservando tom corporativo, terminologia técnica e estilo da empresa, com foco em PT-BR/EN.
category: produtividade
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/artigo-blog
  - marketing/conteudo-site
version: 0.2.0
status: estavel
references:
  - ISO 17100:2015 — Serviços de tradução (requisitos mínimos).
  - Newmark, P. A Textbook of Translation. 1988 (abordagem comunicativa).
  - Jakobson, R. On Linguistic Aspects of Translation. 1959 (equivalência dinâmica).
  - BRASIL. LGPD Lei 13.709/2018 (transferência internacional de dados).
---

# Tradutor Corporativo

## Objetivo
Traduzir textos corporativos preservando terminologia técnica, tom corporativo e estilo da empresa, com glossário de marca e nota de decisões.

## Quando usar
- Documentação técnica multilíngue (EN, ES, PT-BR).
- Site institucional multilíngue.
- E-mails com clientes internacionais.
- Contratos e propostas bilíngues (não juramentados).
- Material de marketing multilíngue.

## Quando NÃO usar
- Para tradução juramentada (usar tradutor público — RT).
- Para tradução literária (usar tradutor especializado).
- Para tradução de patentes (usar especialista técnico-jurídico).
- Para tradução jurada em processos judiciais.

## Princípios de tradução corporativa

| Princípio | Aplicação |
|-----------|-----------|
| **Equivalência comunicativa** | Sentido > literal |
| **Terminologia consistente** | Glossário de marca obrigatório |
| **Tom preservado** | Formal/semiformal mantido |
| **Localização (L10n)** | Adaptar moeda, data, formato |
| **Transcriação** | Quando literal não funciona (marketing) |

## Adaptações críticas para PT-BR

| Elemento | Adaptação |
|----------|-----------|
| **Moeda** | USD $ → BRL R$ conforme contexto; checar cotação se aplicável |
| **Data** | ISO 8601 (AAAA-MM-DD) ou por extenso ("12 de julho de 2026") |
| **Endereço** | CEP + logradouro, adaptar formato BR |
| **Fuso horário** | UTC → America/Sao_Paulo (-03:00) |
| **Telefone** | +55 (11) 91234-5678 |
| **CNPJ/CPF** | 00.000.000/0001-00 / 000.000.000-00 |
| **Siglas** | BACEN (não "BCB" / "Central Bank"), CVM, ANVISA, ANATEL |
| **Termos legais** | LGPD (não "GDPR" quando contexto é Brasil) |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `texto_origem` | string | sim | Texto a ser traduzido |
| `idioma_origem` | enum | sim | pt-BR / en / es |
| `idioma_destino` | enum | sim | pt-BR / en / es |
| `glossario` | dict | sim | Termos de marca obrigatórios |
| `tom` | enum | sim | formal / semiformal / informal / tecnico |
| `audiencia` | string | sim | Quem vai ler (cliente, executivo, técnico) |
| `notas_contexto` | string | não | Instruções adicionais |

## Saídas esperadas
- Texto traduzido.
- Termos do glossário aplicados.
- Notas sobre decisões de tradução.
- Adaptações localizadas (moeda, data, formato).
- Alerta para ambiguidades.

## Fluxo interno
1. Carregar `config/empresa.yaml` (glossário, tom).
2. Identificar idioma origem e destino.
3. Detectar termos técnicos que exigem glossário.
4. Traduzir preservando tom.
5. Aplicar adaptações localizadas (moeda, data, formato).
6. Sinalizar termos do glossário.
7. Adicionar notas sobre decisões difíceis.
8. Validar consistência terminológica.

## Boas práticas
- **Glossário prévio** — não improvisar termos de marca.
- **Tom consistente** — formal/semiformal mantido.
- **Equivalência, não literal** — significado > palavras.
- **Localização** — moeda, data, endereço, formato BR.
- **Notas de tradução** — para o leitor corporativo.
- **Transcriação** — em marketing, adaptar o sentimento.
- **Consistência terminológica** — mesmo termo em todo o texto.
- **Glossário bilíngue** — EN ↔ PT-BR.
- **Não traduzir marca própria** — Google Translate é "Google Translate" no Brasil.
- **Siglas brasileiras** — usar termo oficial (BACEN, CVM, ANVISA).

## Armadilhas comuns
- Tradução literal (false friends).
- Não adaptar moeda (USD para contexto brasileiro).
- Não adaptar formato de data (MM/DD vs. DD/MM).
- Misturar PT-BR com PT-PT (ex: "telemóvel" em vez de "celular").
- Traduzir nome próprio (Google, WhatsApp).
- Esquecer de adaptar endereço/telefone/CNPJ.
- Perder nuance do tom original.
- Misturar variantes linguísticas.

## Limitações
- Não traduz imagens (apenas texto).
- Não certifica tradução juramentada.
- Não é adequado para documentos legais vinculantes.
- Não substitui revisão humana em textos críticos.
- Não detecta ironia ou humor cultural.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — E-mail corporativo EN → PT-BR
- `02-intermediario.md` — Página institucional PT-BR → EN
- `03-avancado.md` — Documentação técnica multilíngue com glossário

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- CAT tools (SDL Trados, memoQ, Smartcat)
- TMS (Translation Management Systems — Lokalise, Crowdin)
- Memória de tradução (TM) corporativa
- Ferramentas de glossário (TermBase)