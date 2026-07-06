# Governança — Office Skills

Este documento define como a biblioteca é mantida, revisada e evoluída.

## Papéis

| Papel | Responsabilidade |
|-------|-----------------|
| **Mantenedor** | Aprova PRs, define roadmap, resolve conflitos |
| **Curador de domínio** | Revisa Skills dentro de uma categoria específica |
| **Autor** | Cria ou altera Skills conforme `CONTRIBUTING.md` |
| **Consumidor** | Usa Skills em projetos; abre issues quando algo falha |

## Ciclo de vida de uma Skill

```
[Ideia] → [Rascunho] → [Revisão] → [Estável] → [Deprecada]
```

- **Ideia:** proposta em issue ou discussão.
- **Rascunho:** Skill existe mas não passou em revisão.
- **Revisão:** PR aberto, aguardando curador.
- **Estável:** mergeada e indexada.
- **Deprecada:** substituída por outra; visível no catálogo com tarja.

## Critérios para aprovar uma Skill

1. Tem responsabilidade única.
2. Segue a estrutura padrão de pastas.
3. Tem frontmatter completo.
4. Documenta entradas, saídas e fluxo interno.
5. Tem pelo menos três casos de teste.
6. Não duplica Skill existente (buscar antes de criar).
7. Não depende de fornecedor sem isolá-lo em adaptador.
8. Tem versão semântica definida.
9. Está no diretório de categoria correto.

## Versionamento

| Mudança | Versão |
|---------|--------|
| Correção textual sem alterar comportamento | patch |
| Novo exemplo, novo teste, esclarecimento | minor |
| Mudança incompatível de contrato | major |

## Política de depreciação

- Skill em depreciação continua no repositório por 2 versões minor.
- README e SKILL.md ganham aviso `> DEPRECATED`.
- INDEX.md marca a Skill com `⚠️`.

## Como abrir uma issue

Use os templates em `.github/ISSUE_TEMPLATE/` (quando existirem) ou descreva:

1. **Contexto** — onde você usou a Skill.
2. **Problema** — o que aconteceu.
3. **Resultado esperado** — o que deveria ter acontecido.
4. **Sugestão** — como corrigir.

## Como abrir um PR

1. Crie branch a partir de `main`: `git checkout -b skill/<slug>`.
2. Siga o `CONTRIBUTING.md`.
3. Rode `scripts/validate.sh` antes de pedir revisão.
4. Descreva no PR quais Skills foram alteradas e por quê.
5. Aguarde revisão do curador do domínio correspondente.

## Código de conduta

Respeito, objetividade e clareza. Críticas devem ser técnicas e fundamentadas.