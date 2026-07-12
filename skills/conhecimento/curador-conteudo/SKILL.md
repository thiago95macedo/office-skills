---
name: curador-conteudo
description: Use para selecionar, organizar e resumir conteúdos relevantes para um objetivo definido (curadoria, não criação).
category: conhecimento
priority: opcional
depends_on:
  - produtividade/resumo-executivo
composes_with:
  - marketing/artigo-blog
  - suporte/base-conhecimento
  - marketing/conteudo-linkedin
version: 0.2.0
status: estavel
references:
  - Bhargava, R. Manifesto Content Curation. 2009 (origem do conceito moderno).
  - Dalkir, K. Knowledge Management in Theory and Practice. 4. ed. 2023.
  - Halvorson, K.; Rach, M. Content Strategy for the Web. 2. ed. 2012.
  - BRASIL. Lei 9.610/1998 — Lei de Direitos Autorais (citação e referência).
---

# Curador de Conteúdo

## Objetivo
Selecionar, organizar e resumir conteúdos relevantes de fontes variadas para um objetivo definido, distinguindo curadoria (organizar o que existe) de criação (produzir conteúdo novo).

## Quando usar
- Newsletter interna setorial.
- Briefing temático para gestão.
- Preparação de treinamento (curadoria antes da criação).
- Atualização de base de conhecimento (curadoria de fontes externas).
- Estratégia de conteúdo para redes sociais.

## Quando NÃO usar
- Para conteúdo único a resumir (usar `produtividade/resumo-executivo`).
- Para criação de conteúdo original (usar `marketing/artigo-blog`).
- Para curadoria de fontes sem objetivo claro (perde foco).

## Princípios da curadoria (Bhargava, 2009)

| Princípio | Aplicação |
|-----------|-----------|
| **Agregação** | Reunir o melhor conteúdo |
| **Distilação** | Extrair essência (não apenas linkar) |
| **Elevação** | Adicionar contexto e valor |
| **Mashup** | Combinar fontes para nova perspectiva |
| **Sequência** | Ordenar para narrativa |
| **Cronologia** | Quando tempo importa |

## Workflow de curadoria (4 passos)

| Etapa | Ação |
|-------|------|
| **1. Descobrir** | Buscar fontes relevantes |
| **2. Filtrar** | Aplicar critérios de relevância |
| **3. Organizar** | Estruturar por tema, tempo ou importância |
| **4. Publicar** | Distribuir com contexto e atribuição |

## Atribuição e direitos autorais (Lei 9.610/1998)

- **Citar fonte** — sempre, com link e data de acesso.
- **Resumir** — não reproduzir integralmente sem permissão.
- **Quote curto** — até 30% com citação explícita.
- **Link original** — preserve a possibilidade de ir à fonte.
- **Respeitar paywalls** — não quebre付费 controles.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo` | string | sim | Por que esta curadoria existe |
| `publico` | string | sim | Quem vai consumir |
| `fontes` | lista | sim | Fontes disponíveis (URL, arquivo, referência) |
| `formato_saida` | enum | sim | newsletter / briefing / dossier / thread / report |
| `idioma` | enum | sim | pt-BR (padrão) |
| `frequencia` | string | não | Cadência (semanal, quinzenal) |
| `tamanho_max` | int | não | Tamanho máximo de saída |

## Saídas esperadas
- Lista curada com organização lógica.
- Resumo por item (essência, não só link).
- Atribuição completa de cada fonte.
- Contexto adicional (por que isso importa).
- Chamada para ação (opcional).

## Fluxo interno
1. Carregar `config/empresa.yaml` (template de newsletter, marca).
2. Receber objetivo, público, fontes.
3. Filtrar fontes por relevância (critério claro).
4. Ler/extrair essência de cada fonte.
5. Organizar (por tema, por tempo, por relevância).
6. Adicionar contexto (por que isso importa para o público).
7. Adicionar atribuição completa.
8. Definir CTA (se aplicável).
9. Validar respeito a direitos autorais.

## Boas práticas
- **Curar ≠ criar** — distinção clara.
- **Atribuição obrigatória** — Lei 9.610/1998.
- **Resumo próprio** — não copiar e colar.
- **Link para fonte** — preserve a possibilidade de aprofundar.
- **Contexto agregado** — por que isso importa.
- **Distinção fato/opinião** — credibilidade.
- **Data de acesso** — informação datada envelhece.
- **Diversidade de fontes** — não só um veículo.
- **Frequência consistente** — leitor cria expectativa.
- **Curadoria contínua** — não é one-shot.

## Armadilhas comuns
- Reproduzir conteúdo sem atribuição (viola Lei 9.610/1998).
- Agregar sem agregar valor (spam de links).
- Sem curadoria crítica (só republicação).
- Sem contexto (leitor precisa de "por que isso importa").
- Misturar fato e opinião sem distinguir.
- Conteúdo desatualizado.
- Viés de fonte única.
- Curadoria reativa (sem critério claro).

## Limitações
- Não pesquisa em tempo real (depende de input).
- Não mede engajamento dos itens curados.
- Não traduz conteúdo automaticamente.
- Não detecta conteúdo desatualizado automaticamente.

## Dependências
- `produtividade/resumo-executivo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Newsletter setorial semanal
- `02-intermediario.md` — Briefing temático para gestão
- `03-avancado.md` — Dossiê de pesquisa de mercado

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Agregadores (Feedly, Inoreader, Pocket)
- Newsletters (Substack, Beehiiv)
- CMS (WordPress, Ghost)
- Ferramentas de monitoramento (Google Alerts, Mention)