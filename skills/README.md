# Skills — Visão geral

Esta pasta contém todas as Skills da biblioteca Office Skills, organizadas por domínio.

## Categorias

| Categoria | Sigla | Quantidade | Escopo |
|-----------|-------|-----------|--------|
| Core | `_core` | 4 | Skills transversais (composição, contexto, estilo) |
| Comercial | `comercial` | 8 | Propostas, orçamentos, RFP, follow-up, objeções |
| Administrativo | `administrativo` | 5 | E-mails, ofícios, atas, comunicados, cartas |
| Financeiro | `financeiro` | 5 | Análise de custos, cobrança, orçamento, prestação |
| Gestão | `gestao` | 6 | Planos, 5W2H, KPI/OKR, riscos, cronograma, dashboard |
| Documentação | `documentacao` | 6 | POP/SOP, manuais, checklists, FAQ, padronizador |
| RH | `rh` | 5 | Vagas, onboarding, feedback, avaliação, treinamento |
| Marketing | `marketing` | 5 | LinkedIn, site, cases, campanhas, blog |
| Atendimento | `atendimento` | 3 | Triagem, resposta rápida, encaminhamento |
| Suporte | `suporte` | 3 | Classificador de tickets, FAQ técnico, base |
| Produtividade | `produtividade` | 7 | Resumo, planilha, apresentação, extrator, tradução |
| Conhecimento | `conhecimento` | 3 | Classificador, mapa de conhecimento, curadoria |

**Total: 60 Skills**

## Como navegar

- Use `INDEX.md` na raiz para ver a tabela com todas as Skills e prioridades.
- Entre em cada pasta `skills/<categoria>/<slug>/` para acessar SKILL.md, README.md, prompt.md, examples/, templates/ e tests/.
- Use `docs/fluxos/` para receitas que combinam várias Skills.

## Prioridades

- ⭐ **Essencial** — primeira onda de adoção.
- 🔶 **Recomendada** — segunda onda; adoção por áreas específicas.
- ⚪ **Opcional** — casos especiais ou baixa frequência.

## Dependências transversais

- `_core/redator-corporativo` é a dependência mais comum. Carrega tom corporativo.
- `_core/configurador-empresa` fornece contexto (tom, vocabulário, contato).
- `_core/organizador-informacao` é usada para estruturar conteúdo bruto.
- `_core/compositor-fluxos` encadeia Skills em pipelines.

## Validação

Rode `scripts/validate.sh` para verificar estrutura padronizada de todas as Skills.

```bash
bash scripts/validate.sh
```