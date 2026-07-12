---
name: gerador-apresentacao
description: Use para estruturar apresentações (slides) com storyline claro, slides objetivos e CTA.
category: produtividade
priority: essencial
depends_on:
  - _core/redator-corporativo
composes_with:
  - produtividade/resumo-executivo
  - comercial/proposta-comercial
  - comercial/one-pager
version: 0.2.0
status: estavel
references:
  - Kawasaki, G. The 10-20-30 Rule of PowerPoint. 2005 (10 slides, 20 min, 30pt).
  - Duarte, N. Slide:ology. 2008 / Resonate. 2010 / Illuminate. 2016.
  - Gallo, C. The Presentation Secrets of Steve Jobs. 2009 / Talk Like TED. 2014.
  - Minto, B. The Pyramid Principle. 1985 (estrutura lógica de comunicação executiva).
---

# Gerador de Apresentação

## Objetivo
Estruturar apresentação completa (storyline, slides, mensagens-chave, CTA) pronta para produção visual em PowerPoint, Google Slides ou Keynote.

## Quando usar
- Apresentações executivas para diretoria.
- Pitches comerciais para clientes.
- Apresentações técnicas ou treinamento.
- Status report de projeto.
- Apresentação para conselho ou investidores.

## Quando NÃO usar
- Para apresentações improvisadas (sem estrutura).
- Para apresentações longas (>30 slides) que exigem outro formato.
- Para demos de produto (usar demo script dedicado).

## Regra 10-20-30 (Guy Kawasaki)

| Dimensão | Limite |
|----------|--------|
| **10 slides** | Máximo |
| **20 minutos** | Duração ideal |
| **30 pontos** | Tamanho mínimo de fonte |

## Storylines reconhecidas

| Storyline | Estrutura | Quando usar |
|-----------|-----------|-------------|
| **Problema → Solução → Prova → Ação** | 4 atos | Pitch comercial |
| **Pirâmide de Minto** | Conclusão → Argumentos → Evidências | Comunicação executiva |
| **Resonate (Duarte)** | Audience as hero, conflito, transformação | Apresentações inspiracionais |
| **SCQA** (Situation, Complication, Question, Answer) | McKinsey clássico | Briefing executivo |
| **BLUF** (Bottom Line Up Front) | Conclusão primeiro | Status report |

## Estrutura recomendada de slides

| Slide | Conteúdo | Limite |
|-------|----------|--------|
| **Capa** | Título + subtítulo + autor + data | 1 slide |
| **Resumo executivo** | Conclusão + 3 bullets de apoio | 1-2 slides |
| **Contexto** | Por que estamos aqui | 1-2 slides |
| **Problema/oportunidade** | Dor ou gap | 1-2 slides |
| **Proposta** | O que estamos propondo | 2-4 slides |
| **Evidências/prova** | Dados, cases, depoimentos | 2-3 slides |
| **Plano de ação** | Próximos passos | 1-2 slides |
| **CTA** | O que pedimos à audiência | 1 slide |
| **Apêndices** | Detalhes extras (opcional) | 2-5 slides |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo` | string | sim | Objetivo da apresentação |
| `publico` | string | sim | Audiência |
| `duracao_minutos` | int | sim | Tempo total disponível |
| `mensagens_chave` | lista | sim | 3-5 mensagens principais |
| `cta` | string | sim | Decisão/ação pedida à audiência |
| `storyline` | enum | sim | problema-solucao / piramide / resonate / scqa / bluf |
| `evidencias` | lista | não | Dados, cases, depoimentos |
| `tom` | enum | sim | formal / inspiracional / tecnico |

## Saídas esperadas
- Storyline escolhida.
- Estrutura de slides numerados.
- Título e mensagens-chave por slide.
- Sugestão de visual por slide.
- Slide de CTA destacado.
- Apêndices (quando aplicável).
- Respeitando regra 10-20-30 quando relevante.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom, marca, cores).
2. Validar regra 10-20-30 (ou ajustar conforme audiência).
3. Escolher storyline conforme objetivo.
4. Estruturar slides conforme template.
5. Definir título e 1 mensagem por slide.
6. Sugerir visual por slide (gráfico, imagem, bullets).
7. Destacar CTA no final.
8. Adicionar apêndices quando necessário.
9. Validar duração total estimada.

## Boas práticas
- **1 ideia por slide** — não sobrecarregar.
- **Headline declarativa** — slide title é afirmação, não rótulo.
- **Visual > texto** — gráfico > tabela > lista.
- **Conclusão primeiro** — slide de resumo executivo antes do detalhe.
- **Storyline clara** — quem assistiu do meio entende o recado.
- **Fonte ≥ 30pt** (regra Kawasaki) — exceto rodapés e citações.
- **Poucas cores** — paleta da marca.
- **Sem animação desnecessária** — uma transição limpa basta.
- **Notas do apresentador** — para quem apresenta, não no slide.
- **Apêndice para detalhe** — não poluir slide principal.
- **Repetir slide-chave** — mensagem principal retorna no final.
- **Hand-off claro** — slide final diz o que precisa ser decidido.

## Armadilhas comuns
- Slide com 80 palavras — ninguém lê.
- Headline vaga ("Resultados") — substituir por afirmação.
- Visual decorativo sem dados (pie chart 3D).
- Animações excessivas (distraem).
- Sem CTA final.
- Duração > 30 min sem interação.
- Apresentador lê o slide.
- Apêndice virou o conteúdo principal.
- Sem teste no projetor (cores distorcidas).

## Limitações
- Não gera PPTX nativo.
- Não cria imagens ou gráficos nativos (apenas sugere).
- Não aplica templates visuais específicos.
- Não verifica acessibilidade visual automaticamente.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Apresentação executiva (10 slides)
- `02-intermediario.md` — Pitch comercial (problema-solução-prova-ação)
- `03-avancado.md` — Apresentação para conselho com apêndices

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- PowerPoint, Google Slides, Keynote
- Canva, Figma (templates)
- Bibliotecas de ícones (Noun Project, Flaticon)
- Geradores de gráficos (Datawrapper, Flourish)