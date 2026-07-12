---
name: checklist
description: Use para criar listas de verificação aplicáveis a rotinas críticas (auditoria, manutenção, onboarding, fechamento mensal, release).
category: documentacao
priority: essencial
depends_on: []
composes_with:
  - documentacao/pop-sop
  - gestao/plano-acao
  - rh/onboarding
  - administrativo/ata-reuniao
version: 0.2.0
status: estavel
references:
  - Gawande, A. The Checklist Manifesto. 2009.
  - PMI. PMBOK Guide. 8. ed. 2025.
  - Reason, J. Human Error. 1990.
  - Boeing/Airbus — Crew Resource Management (CRM).
---

# Checklist

## Objetivo
Criar listas de verificação operacionais para rotinas críticas, com itens objetivos, agrupados por categoria, marcando ponto crítico quando aplicável. Inspirado em *The Checklist Manifesto* (Gawande, 2009) e nas práticas de Crew Resource Management (aviação).

## Quando usar
- Auditoria interna ou externa (ISO, SOX, ANVISA, BACEN).
- Rotinas de manutenção preventiva ou corretiva.
- Onboarding e offboarding de colaboradores.
- Fechamento mensal (contábil, fiscal, RH).
- Release de software em produção.
- Procedimentos médicos ou de segurança.

## Quando NÃO usar
- Para narrar processo longo (usar `pop-sop` ou `manual-tecnico`).
- Para diagnóstico (usar 5 Porquês ou Ishikawa).
- Para lista de desejos ou brainstorm (usar lista livre, sem formatação de checklist).

## Tipos de checklist (classificação)

| Tipo | Uso | Estrutura |
|------|-----|-----------|
| **Leitura** (read-do) | Cada item é lido em voz alta durante a execução | Numerado, em ordem |
| **Desempenho** (do-confirm) | Executor faz e depois confere | Agrupado por fase |
| **Verificação** (challenge) | Terceiro confere a execução do primeiro | Independente |
| **Pontos críticos** | Lista os passos que exigem atenção redobrada | Marcados com ⚠️ |

## Estrutura recomendada

```
[Cabeçalho]
- Título do checklist
- Finalidade
- Código (CHK-XXX-NN)
- Versão / Data
- Responsável pela execução

[Corpo]
- Categoria 1
  - [ ] Item verificável (responsável | prazo)
  - [ ] ⚠️ Item crítico (responsável | prazo)
- Categoria 2
  - [ ] ...

[Rodapé]
- Evidências / registros
- Ação em caso de não-conformidade
- Aprovação
```

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `finalidade` | string | sim | Para que serve o checklist |
| `itens` | lista | sim | Itens verificáveis (verbo no infinitivo) |
| `agrupamento` | dict | não | Categorias e sub-grupos |
| `pontos_criticos` | lista | não | Itens marcados como críticos |
| `responsaveis` | lista | sim | Donos nominais (por item ou categoria) |
| `evidencias` | lista | não | Onde o que é registrado |
| `tipo` | enum | sim | leitura / desempenho / verificação / criticos |

## Saídas esperadas
Checklist Markdown com checkboxes (`- [ ]`), agrupamento por categoria, pontos críticos destacados, responsável por item e seção de evidências.

## Fluxo interno
1. Receber finalidade e tipo de checklist.
2. Listar itens verificáveis com verbo no infinitivo.
3. Agrupar itens por categoria lógica.
4. Marcar pontos críticos com ⚠️.
5. Atribuir responsável nominal a cada item (ou categoria).
6. Definir onde cada item gera evidência.
7. Indicar ação em caso de não-conformidade.
8. Adicionar cabeçalho com versionamento e aprovação.

## Boas práticas
- Itens curtos e verificáveis (1 frase cada, verbo no infinitivo).
- Ordem lógica (cronológica ou por categoria).
- Pontos críticos destacados visualmente (⚠️).
- Responsável nominal por item (não "a equipe").
- Máximo 9 itens por categoria (regra 7±2 de Miller).
- Itens binários (sim/não) — evitar "verificar se está bom".
- Definir ação padrão se item falhar.
- Manter atualizado: revisar a cada uso ou ciclo.

## Limitações
- Não substitui treinamento do executor.
- Não cobre julgamento situacional (para isso, use POP com verbos).
- Não detecta falhas se itens forem marcados sem verificação real (falso positivo humano).
- Não escala para processos muito longos (nesse caso, dividir em múltiplos checklists).

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Checklist de fechamento mensal contábil
- `02-intermediario.md` — Checklist de pré-voo (inspirado em aviação)
- `03-avancado.md` — Checklist de auditoria ISO 9001

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Sistemas de GRC (governance, risk, compliance)
- Formulários digitais (Google Forms, Typeform, Microsoft Forms)
- Apps de checklist (SafetyCulture / iAuditor, SiteDocs)
- GED e ferramentas de qualidade (SGQ)