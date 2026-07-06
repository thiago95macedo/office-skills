# Office Skills — Marketplace Claude Code

Este repositório é um **marketplace de plugins Claude Code** que entrega a biblioteca Office Skills.

## Estrutura de plugin

```
office-skills/
├── .claude-plugin/
│   ├── marketplace.json     ← manifesto do marketplace (este repo)
│   ├── plugin.json          ← manifesto do plugin individual
│   └── README.md            ← este arquivo
├── skills/                  ← 60 Skills distribuídas em 12 categorias
├── docs/                    ← fluxos compostos, mapa de dependências
├── assets/                  ← templates-base compartilhados
├── config/                  ← exemplo de configuração por empresa
├── scripts/                 ← validador e utilitários
├── README.md                ← apresentação institucional
├── ARCHITECTURE.md          ← decisões arquiteturais (ADRs)
├── GOVERNANCE.md            ← governança da biblioteca
├── CONTRIBUTING.md          ← guia de contribuição
├── INDEX.md                 ← catálogo navegável
├── CHANGELOG.md             ← histórico de versões
└── LICENSE                  ← MIT
```

## Como instalar

### Via marketplace (recomendado)

Após publicar o repositório no GitHub (ou outro host git), adicione-o como marketplace no Claude Code e instale o plugin:

```bash
# Adicionar o marketplace (apontando para o repositório)
claude marketplace add office-skills/office-skills

# Instalar o plugin
claude plugin install office-skills
```

### Via clone local

```bash
git clone https://github.com/office-skills/office-skills.git
claude --plugin-dir ./office-skills
```

## Manifesto do plugin

O arquivo `.claude-plugin/plugin.json` declara:

- **name**: `office-skills`
- **version**: `0.1.0`
- **description**: biblioteca de 60 Skills em 12 domínios
- **license**: MIT
- **keywords**: corporate, productivity, automation, etc.

## Manifesto do marketplace

O arquivo `.claude-plugin/marketplace.json` declara este repositório como marketplace e lista o plugin `office-skills` como instalável.

## Personalização por empresa

Para usar o plugin com personalização de tom, vocabulário e identidade da sua empresa, copie `config/empresa.example.yaml` para `config/empresa.yaml` (que está no `.gitignore`) e ajuste conforme necessário.

As Skills consomem este arquivo em runtime; nenhuma Skill precisa ser duplicada.

## Próximos passos

Veja `docs/mapa-dependencias.md` para entender como as Skills se compõem e `docs/fluxos/` para receitas prontas.

## Contato

Mantenedor: **Thiago Macêdo** — [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br) — [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)

## Contato

Mantenedor: **Thiago Macêdo** — [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br) — [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)