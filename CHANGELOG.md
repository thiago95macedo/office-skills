# Changelog — Office Skills

Todas as alterações relevantes da biblioteca. Formato inspirado em Keep a Changelog, versionamento SemVer.

## Mantenedor

**Thiago Macêdo** — [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br) — [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)

## [0.2.0] — 2026-07-06

### Adicionado
- **Schema formal de contrato por Skill**: `assets/schemas/skill.schema.json` e `schema.yaml` em cada uma das 60 Skills, validando inputs, outputs e tipos.
- **Validador de contratos**: `scripts/validate-contracts.py` verifica coerencia do grafo de dependencias e composicao. Resultado atual: 60/60 Skills validas, 0 erros, 0 avisos.
- **Validador de profundidade**: `scripts/check-depth.py` garante que cada Skill tenha SKILL.md com 12 secoes obrigatorias, 3+ exemplos, 3+ casos de teste, templates e schema.yaml. Resultado atual: 60/60 Skills aprovadas.
- **Fluxos executaveis**: `assets/schemas/flow.schema.json` e 10 fluxos em `docs/fluxos/*.yaml` com mapeamento explicito input_from entre steps. Validados por `scripts/validate-flows.py`.
- **Validador consolidado**: `scripts/validate.sh` encadeia os 4 checks (estrutura, contratos, profundidade, fluxos). Resultado atual: 4/4 OK.
- **CI no GitHub Actions**: `.github/workflows/validate.yml` roda os validadores em cada PR e push.
- **Manifesto de plugin Claude Code**: `.claude-plugin/marketplace.json` e `.claude-plugin/plugin.json` permitem instalacao via Claude Code marketplace.
- **README com quick start**: secao dedicada para empresa-piloto com 3 passos (instalar, configurar, executar fluxo).
- **Identificacao do mantenedor**: Thiago Macedo, contato@thiagomacedo.com.br, https://www.thiagomacedo.com.br, em todos os documentos institucionais.

### Mudancas tecnicas
- Frontmatter de todos os SKILL.md atualizado para `version: 0.2.0` e `status: estavel`.
- Pasta `comercial/tratamento-objeções` renomeada para `comercial/tratamento-objecoes` (kebab-case ASCII puro) e todas as referencias corrigidas.
- Schema YAML adicionado em todas as 60 Skills; antigos SKILL.md sem as 12 secoes foram completados via script.
- `examples/*.md` expandidos para >= 120 caracteres; `tests/casos-de-teste.md` reescritos com 3 casos verificaveis cada.

## [0.1.0] — 2026-07-05

### Adicionado
- Estrutura raiz do repositório