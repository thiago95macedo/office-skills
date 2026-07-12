---
name: faq-corporativo
description: Use para construir FAQ interno ou externo, com perguntas claras, respostas precisas e referência a responsável.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - suporte/faq-tecnico
  - atendimento/triagem-mensagens
  - suporte/base-conhecimento
version: 0.2.0
status: estavel
references:
  - Nielsen Norman Group — Writing for the Web (jk Nielsen).
  - Krug, S. Don't Make Me Think, Revisited. 3. ed. 2013.
  - KCS® v6 Practices Guide — Consortium for Service Innovation.
  - Zendesk CX Trends 2024.
---

# FAQ Corporativo

## Objetivo
Organizar perguntas frequentes com respostas consistentes, claras, concisas e com referência a responsável, otimizando atendimento e reduzindo dúvidas repetitivas.

## Quando usar
- Centralizar dúvidas frequentes de clientes ou colaboradores.
- Reduzir carga de atendimento humano (deflection para autoatendimento).
- Padronizar respostas a perguntas recorrentes.
- Apoiar onboarding de novos colaboradores.
- Documentar políticas internas (RH, compliance, financeiro).

## Quando NÃO usar
- Para documentação técnica aprofundada (usar `manual-tecnico` ou `pop-sop`).
- Para política ou norma corporativa (usar documento normativo formal).
- Para FAQ público de SEO (usar conteúdo estruturado + schema.org FAQPage).

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Tema, versão, data, responsável pela manutenção |
| 2 | **Sumário** | Links para seções / perguntas |
| 3 | **Perguntas por categoria** | Agrupadas por tema (não ordem cronológica) |
| 4 | **Pergunta** | Linguagem do usuário (não linguagem interna) |
| 5 | **Resposta** | Clara, concisa, objetiva |
| 6 | **Responsável** | Quem mantém a resposta atualizada |
| 7 | **Última atualização** | Data da última revisão |
| 8 | **Próximo passo** | Link, contato ou ação esperada |

## Anatomia de uma boa pergunta/resposta

| Aspecto | Boa prática |
|---------|-------------|
| **Pergunta** | Linguagem do usuário (como ele perguntaria); sem jargão |
| **Resposta** | 2-5 frases para perguntas simples; mais para perguntas complexas |
| **Primeira frase** | Resposta direta (não "depende...") |
| **Detalhamento** | Passos numerados ou bullets quando a sequência importa |
| **Links** | Para documento, formulário ou página relacionada |
| **CTA** | Próximo passo claro quando relevante |
| **Responsável** | Nome ou área que pode atualizar a resposta |
| **Data** | Última revisão |

## Princípios de redação (Nielsen, Krug)

- **Escaneabilidade** — usuário escaneia, não lê (Nielsen).
- **Conclusão primeiro** — não construir suspense; resposta direta.
- **Menos é mais** — menos texto, mais clareza.
- **Heading descritivo** — pergunta como usuário faria.
- **Sem ambiguidade** — evitar "talvez", "geralmente", "depende".
- **Consistência** — mesmo padrão em todas as respostas.

## Categorização recomendada

| Tipo | Exemplo |
|------|---------|
| **Geral** | O que é [empresa/produto]? |
| **Comercial** | Como comprar? Qual preço? |
| **Técnico** | Como instalar? Como usar? |
| **Administrativo** | Como solicitar? Qual prazo? |
| **Suporte** | Onde reportar problema? Qual SLA? |
| **Política** | Qual política de troca? |
| **Contato** | Como falar com humano? |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tema` | string | sim | Tema do FAQ |
| `audiencia` | enum | sim | interno / externo / clientes / colaboradores |
| `perguntas_respostas` | lista | sim | Lista de pares pergunta/resposta |
| `categorias` | lista | não | Agrupamento por categoria |
| `responsavel_manutencao` | string | sim | Quem mantém atualizado |
| `canal_publicacao` | enum | sim | site / intranet / help-center / PDF |

## Saídas esperadas
- Cabeçalho com metadados.
- Sumário navegável.
- Perguntas agrupadas por categoria.
- Respostas claras, concisas, com responsável e data.
- Próximo passo quando aplicável.

## Fluxo interno
1. Receber tema, audiência e lista de perguntas/respostas.
2. Reorganizar perguntas por categoria lógica (não ordem de recebimento).
3. Reformular perguntas na linguagem do usuário.
4. Redigir respostas diretas (conclusão primeiro).
5. Detalhar com bullets/passos numerados quando a sequência importa.
6. Atribuir responsável por resposta (ou categoria).
7. Registrar data de última atualização.
8. Indicar próximo passo (link, contato, formulário).
9. Adicionar cabeçalho com versionamento.

## Boas práticas
- **Resposta direta** — primeira frase já responde.
- **Escaneabilidade** — bullets, negrito em termos-chave.
- **Conclusão antes da explicação** — "Sim, aceitamos troca em 30 dias" antes do detalhe.
- **Linguagem do usuário** — não jargão interno.
- **Links ativos** — para próxima ação ou documento.
- **Responsável nominal** — quem atualiza a resposta.
- **Data de revisão** — FAQ desatualizado perde credibilidade.
- **Versionamento** — histórico de mudanças relevantes.
- **Acessibilidade** — HTML semântico, contraste, compatível com leitor de tela.
- **Multi-canal** — versão web + versão impressa + versão chatbot.
- **Métricas** — taxa de leitura, taxa de resolução (autoatendimento).
- **Search-friendly** — perguntas como usuário pesquisaria.

## Armadilhas comuns
- Resposta vaga ("depende", "geralmente", "talvez").
- Resposta longa demais — usuário desiste antes do final.
- Misturar perguntas fáceis e difíceis sem categorização.
- Sem responsável — ninguém atualiza e a FAQ defasa.
- Sem data de revisão — sem sinal de obsolescência.
- Linguagem corporativa em vez de linguagem do usuário.
- Sem link ou CTA — usuário fica sem próximo passo.
- FAQ desatualizado (informação incorreta).
- Misturar perguntas de públicos diferentes (cliente + colaborador).
- Categorização confusa (não ajuda a encontrar).

## Limitações
- Não substitui atendimento humano para casos complexos.
- Não substitui documentação técnica aprofundada.
- Não escala para FAQs muito extensos (>100 perguntas) sem taxonomia robusta.
- Não detecta perguntas novas (mecanismo separado de listening social).

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — FAQ de programa interno (RH)
- `02-intermediario.md` — FAQ público de produto
- `03-avancado.md` — FAQ de help-center técnico com taxonomia

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Help center / knowledge base (Zendesk, Freshdesk, Intercom, HubSpot)
- Chatbot / IA conversacional (respostas automáticas)
- Site institucional (schema.org FAQPage para SEO)
- Intranet corporativa (Notion, Confluence)
- Base de conhecimento (KCS — Knowledge-Centered Service)