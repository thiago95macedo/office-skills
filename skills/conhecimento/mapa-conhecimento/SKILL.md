---
name: mapa-conhecimento
description: Use para mapear ativos de conhecimento da empresa (documentos, especialistas, bases, ferramentas) com taxonomia e identificação de lacunas.
category: conhecimento
priority: recomendada
depends_on:
  - conhecimento/classificador-documentos
composes_with:
  - suporte/base-conhecimento
  - conhecimento/curador-conteudo
version: 0.2.0
status: estavel
references:
  - Nonaka, I.; Takeuchi, H. The Knowledge-Creating Company. 1995 (modelo SECI).
  - Dalkir, K. Knowledge Management in Theory and Practice. 4. ed. 2023.
  - APQC — Knowledge Management framework.
  - BRASIL. Lei 13.709/2018 — LGPD (cuidado com dados pessoais no mapa).
---

# Mapa de Conhecimento

## Objetivo
Inventariar ativos de conhecimento da empresa (documentos, especialistas, bases, ferramentas), identificar lacunas e especialistas por domínio.

## Quando usar
- Onboarding de nova gestão ou direção.
- Planejamento de sucessão.
- Auditoria de gestão do conhecimento.
- Antes de reestruturação ou fusão.
- Identificação de riscos de perda de conhecimento (Key Person Risk).

## Quando NÃO usar
- Para FAQ específico de produto (usar `suporte/faq-tecnico`).
- Para classificação de documentos individuais (usar `conhecimento/classificador-documentos`).
- Para taxonomia de GED (usar `documentacao/organizador-documental`).

## Dimensões do mapa de conhecimento

| Dimensão | O que captura |
|----------|--------------|
| **Tácito** | Conhecimento na cabeça das pessoas (expert, especialista) |
| **Explícito** | Documentado (políticas, manuais, bases) |
| **Estruturado** | Em sistemas (CRM, ERP, BI) |
| **Cultura** | Práticas, rituais, hábitos da empresa |
| **Ferramentas** | Plataformas que sustentam o conhecimento |
| **Relações** | Quem ensina quem, quem consulta quem |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Período, áreas cobertas, responsável |
| 2 | **Visão geral** | Resumo executivo do mapa |
| 3 | **Ativos por área** | Documentos, bases, ferramentas, especialistas |
| 4 | **Especialistas-chave** | Pessoas com conhecimento crítico (key persons) |
| 5 | **Lacunas** | Áreas sem documentação ou sem especialistas |
| 6 | **Riscos** | Pessoas-chave em risco de saída, conhecimento em risco |
| 7 | **Oportunidades** | Conhecimento reutilizável, parcerias internas |
| 8 | **Plano de ação** | Onde documentar, quem entrevistar, quando |
| 9 | **LGPD** | Cuidados com dados pessoais no mapa |
| 10 | **Anexos** | Lista de documentos, bases, ferramentas detalhadas |

## Modelo SECI (Nonaka & Takeuchi)

| Modo | Conversão | Exemplo |
|------|-----------|---------|
| **Socialização** | Tácito → Tácito | Mestre → aprendiz (observação) |
| **Externalização** | Tácito → Explícito | Entrevista → documentação |
| **Combinação** | Explícito → Explícito | Documentos → manual |
| **Internalização** | Explícito → Tácito | Leitura → prática |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `areas` | lista | sim | Áreas da empresa a mapear |
| `documentos` | lista | não | Documentos identificados |
| `especialistas` | lista | não | Pessoas-chave (nome, área, expertise) |
| `ferramentas` | lista | não | Plataformas de conhecimento |
| `lacunas_suspeitas` | lista | não | Áreas sem cobertura |
| `objetivo` | enum | sim | onboarding-gestao / auditoria / fusao / sucessao |

## Saídas esperadas
- Mapa visual (markdown ou mermaid).
- Lista de especialistas-chave com expertise.
- Inventário de ativos por área.
- Lacunas identificadas.
- Riscos de perda de conhecimento.
- Plano de ação para preencher lacunas.
- Alertas LGPD (dados sensíveis no mapa).

## Fluxo interno
1. Carregar `config/empresa.yaml` (áreas, organograma).
2. Receber dados de entrada (áreas, documentos, especialistas).
3. Mapear ativos por dimensão (tácito, explícito, estruturado, etc.).
4. Identificar especialistas-chave e riscos de sucessão.
5. Identificar lacunas (áreas sem docs, sem especialistas).
6. Construir plano de ação (entrevistas, documentação).
7. Sinalizar dados sensíveis (LGPD) para tratamento especial.

## Boas práticas
- **Visão holística** — não apenas documentos.
- **Especialistas identificados** — nomes + expertise + disponibilidade.
- **Lacunas explícitas** — não esconder o que falta.
- **Riscos de sucessão** — pessoa-chave em saída = conhecimento em risco.
- **Plano de ação** — onde documentar, quem entrevistar.
- **LGPD** — não expor dados pessoais sensíveis no mapa compartilhado.
- **Atualização periódica** — anual ou semestral.
- **Validação com áreas** — não impor de cima para baixo.
- **Linguagem acessível** — mapa é para gestores, não especialistas.
- **Visual** — diagrama ajuda mais que tabela.

## Armadilhas comuns
- Mapear só documentos (ignorar conhecimento tácito).
- Não identificar especialistas-chave (risco de saída).
- Expor dados sensíveis sem tratamento.
- Mapa desatualizado.
- Mapa sem dono (ninguém mantém).
- Mapa excessivamente detalhado (perde utilidade).
- Sem plano de ação (mapa sem execução).

## Limitações
- Não entrevista especialistas (apenas usa dados fornecidos).
- Não acessa bases de conhecimento automaticamente.
- Não detecta tacit knowledge sem entrevista.
- Não mede qualidade dos ativos mapeados.

## Dependências
- `conhecimento/classificador-documentos`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Onboarding de nova diretoria
- `02-intermediario.md` — Auditoria de gestão do conhecimento
- `03-avancado.md` — Mapeamento antes de fusão

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Ferramentas de KM (Confluence, Notion, Guru)
- Organograma corporativo (HRIS, Pontotel, Senior)
- Bases internas (BI, CRM, ERP)
- Ferramentas de visualização (Mermaid, Miro, Whimsical)