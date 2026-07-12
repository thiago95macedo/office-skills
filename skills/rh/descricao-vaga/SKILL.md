---
name: descricao-vaga
description: Use para redigir descrições de vaga objetivas, atrativas, inclusivas e alinhadas à cultura da empresa brasileira.
category: rh
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - rh/treinamento-materiais
  - marketing/conteudo-linkedin
  - rh/onboarding
version: 0.2.0
status: estavel
references:
  - BRASIL. Lei 13.146/2015 — Lei Brasileira de Inclusão da Pessoa com Deficiência.
  - BRASIL. Lei 13.709/2018 — LGPD (dados em currículo).
  - Chiavenato, I. Recursos Humanos: O capital humano das organizações. 2014.
  - Dutra, J. S. Competências: conceitos, instrumentos e aplicações. 2017.
---

# Descrição de Vaga

## Objetivo
Produzir descrição de vaga completa, objetiva, atrativa, inclusiva e alinhada à cultura da empresa, conforme práticas reconhecidas de recrutamento no Brasil.

## Quando usar
- Abertura de nova posição (CLT, PJ, estágio, trainee).
- Reposição de vaga (desligamento, promoção, realocação).
- Recriação de posição com escopo atualizado.
- Estruturação de programa de estágio ou trainee.

## Quando NÃO usar
- Para descrição interna sucinta (usar memorando ou ficha de cargo).
- Para contratação internacional (usar versão com idioma adicional).
- Para recrutamento de executivo C-level (processo separado).

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Título da vaga** | Nome do cargo + área + local |
| 2 | **Sobre a empresa** | Descrição institucional resumida |
| 3 | **Sobre o cargo** | Propósito em 1-2 frases |
| 4 | **Responsabilidades** | 5-8 entregas principais (verbo no infinitivo) |
| 5 | **Requisitos obrigatórios** | Formação, experiência técnica, certificações |
| 6 | **Requisitos diferenciais** | Plus que agrega mas não elimina |
| 7 | **Competências comportamentais** | Habilidades interpessoais esperadas |
| 8 | **Modelo de trabalho** | Presencial / híbrido / remoto; jornada |
| 9 | **Benefícios** | Lista honesta e verificável |
| 10 | **Salário e faixa** | Faixa salarial ou "a combinar" |
| 11 | **Etapas do processo** | Triagem → entrevistas → teste → oferta |
| 12 | **Como se candidatar** | Link, e-mail ou plataforma (Gupy, Vagas.com, LinkedIn) |

## Boas práticas brasileiras

| Aspecto | Orientação |
|---------|------------|
| **Linguagem inclusiva** | Evitar gênero: "você será responsável por..." (não "o analista será"). Usar "profissional", "pessoa". |
| **Sem discriminação** | Não citar idade, estado civil, religião, aparência. Apenas formação e experiência. |
| **Benefícios verificáveis** | Listar o que realmente é oferecido (VT, VR, plano de saúde, convênio, PLR). |
| **Faixa salarial** | CLT permite informar faixa. Lei 14.611/2023 torna obrigatório para empresas com 100+ colaboradores (em negociação coletiva ou convenção). |
| **Modelo de trabalho** | CLT permite 100% remoto, híbrido ou presencial. Detalhar jornada. |
| **Acessibilidade** | Indicar que o processo é acessível a PCD (Lei 8.213/91 — cota de 2-5%). |
| **Cidade e UF** | Sempre especificar. |
| **Tipo de contrato** | CLT, PJ, estágio, trainee, temporário — explicitar. |
| **Prazo de candidatura** | Definir data de fechamento. |
| **Idioma** | PT-BR (padrão); inglês se exigido no cargo. |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `cargo` | string | sim | Nome do cargo |
| `area` | string | sim | Departamento ou área |
| `reporta_para` | string | sim | Cargo do superior direto |
| `missao` | string | sim | Propósito da posição em 1-2 frases |
| `responsabilidades` | lista | sim | 5-8 entregas principais |
| `requisitos_obrigatorios` | lista | sim | Formação, experiência, habilidades técnicas |
| `requisitos_diferenciais` | lista | não | Plus que agrega valor |
| `competencias_comportamentais` | lista | sim | Soft skills esperados |
| `beneficios` | lista | sim | Lista honesta e verificável |
| `modelo_trabalho` | enum | sim | presencial / hibrido / remoto |
| `localizacao` | string | sim | Cidade e UF |
| `faixa_salarial` | dict | não | Mínimo e máximo em BRL |
| `tipo_contrato` | enum | sim | CLT / PJ / Estagio / Trainee / Temporario |
| `canal_candidatura` | enum | sim | Gupy / Vagas.com / LinkedIn / e-mail / site |

## Saídas esperadas
- Título da vaga claro.
- Descrição institucional breve.
- 5-8 responsabilidades em verbos no infinitivo.
- Requisitos separados em obrigatórios e diferenciais.
- Benefícios verificáveis.
- Modelo de trabalho e localização.
- Faixa salarial (quando aplicável).
- Etapas do processo seletivo.
- CTA de candidatura com canal e prazo.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom institucional, benefícios padrão).
2. Receber dados da vaga.
3. Redigir propósito em frase concisa e inspiradora.
4. Listar responsabilidades (verbo no infinitivo, mensuráveis).
5. Separar requisitos obrigatórios e diferenciais.
6. Listar benefícios de forma atrativa sem exagero.
7. Definir faixa salarial ou "a combinar" conforme política.
8. Especificar modelo de trabalho, localização, tipo de contrato.
9. Indicar etapas do processo e canal de candidatura.
10. Validar conformidade com LGPD (consentimento para tratamento de dados).
11. Validar acessibilidade para PCD.

## Boas práticas
- Linguagem inclusiva (sem gênero, sem idade, sem estado civil).
- Sem discriminação velada (vestuário, aparência, formação de elite específica).
- Benefícios verificáveis (sem promessas vazias).
- Responsabilidades mensuráveis (verbo no infinitivo + objeto + critério).
- Faixa salarial informada (Lei 14.611/2023 — empresas 100+).
- Cidade e UF explícitas.
- Tipo de contrato claro.
- Canal de candidatura único e funcional.
- Prazo de candidatura definido.
- Etapas do processo transparentes.
- Tom profissional mas humano (sem ser robótico).
- Ortografia e gramática impecáveis (a vaga é vitrine da marca).

## Armadilhas comuns
- Uso de gênero ("o analista" / "a assistente") — preferir "profissional" ou "pessoa".
- Discriminação velada (idade, bairro, formação específica).
- Benefícios inflados ou genéricos.
- Faixa salarial não informada (perde candidatos qualificados).
- Vaga sem prazo (deixa processo em aberto indefinidamente).
- Modelo de trabalho vago ("híbrido a combinar" — não diz quantos dias).
- Responsabilidades vagas ("trabalhar em equipe") — sem verbo mensurável.
- Requisitos impossíveis ("júnior com 10 anos de experiência").
- Mistura CLT e PJ sem esclarecer implicações.
- Falta de canal acessível (e-mail pessoal, WhatsApp pessoal).
- Esquecer de incluir "aceitamos PCD".

## Limitações
- Não publica automaticamente em plataformas.
- Não gera versão mobile-friendly (apenas conteúdo).
- Não substitui análise de perfil do candidato.
- Não acessa base de talentos internos.
- Não verifica conformidade com convenção coletiva específica.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Vaga CLT operacional
- `02-intermediario.md` — Vaga CLT técnica + híbrido
- `03-avancado.md` — Programa de trainee estruturado

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- ATS (Gupy, Greenhouse, Lever, Workable)
- LinkedIn Jobs, Indeed, Catho, Vagas.com
- Página de carreiras do site institucional
- Banco de talentos interno (RHIS, Pontotel, Senior)