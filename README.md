# Office Skills — Biblioteca Corporativa de Skills para IA

> **Office Skills não é uma coleção de prompts. É um framework para desenvolvimento, organização, versionamento e reutilização de Skills corporativas para agentes de IA.**

![Skills](https://img.shields.io/badge/skills-60-blueviolet)
![Categorias](https://img.shields.io/badge/categorias-12-blue)
![Status](https://img.shields.io/badge/status-stable-success)
![Versão](https://img.shields.io/badge/vers%C3%A3o-0.2.0-orange)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

Office Skills é uma biblioteca corporativa inspirada em padrões de engenharia de software (em particular, na disciplina de **Skills como documentação executável** do projeto Superpowers). Cada Skill é um pequeno módulo independente, com responsabilidade clara, prompt interno versionado, exemplos e testes.

## Quick start para empresa-piloto

Se você chegou aqui querendo **usar** o Office Skills em produção, siga estes 3 passos:

### 1. Instalar o plugin (Claude Code)

```bash
# Opcao A: a partir do marketplace (quando publicado no GitHub)
claude marketplace add office-skills/office-skills
claude plugin install office-skills

# Opcao B: instalacao local via clone
git clone https://github.com/office-skills/office-skills.git
claude --plugin-dir ./office-skills
```

### 2. Configurar sua empresa

```bash
# Copie o exemplo e ajuste tom, vocabulario bloqueado e dados de contato
cp config/empresa.example.yaml config/empresa.yaml
# Edite config/empresa.yaml com os dados da sua organizacao
```

### 3. Executar seu primeiro fluxo

Os fluxos mais comuns para começar estão em `docs/fluxos/`:

| Fluxo | Quando usar |
|-------|-------------|
| `proposta-completa` | Responder RFP ou pedido formal de proposta |
| `onboarding-colaborador` | Integrar novo colaborador |
| `fechamento-mensal` | Rotina recorrente de fechamento |
| `atendimento-omnichannel` | Triagem e resposta de mensagens |

Para executar um fluxo:

```bash
# O fluxo e descrito em YAML e pode ser carregado pelo compositor
python3 scripts/validate-flows.py  # valida primeiro
# Em seguida, carregar docs/fluxos/<nome>.yaml via _core/compositor-fluxos
```

### Validar sua instalacao local

```bash
bash scripts/validate.sh
```

Saida esperada: `4 OK / 0 falhas`.

---

## Sobre o projeto

## Mantenedor

**Thiago Macêdo**
E-mail: [contato@thiagomacedo.com.br](mailto:contato@thiagomacedo.com.br)
Site: [https://www.thiagomacedo.com.br](https://www.thiagomacedo.com.br)

Para dúvidas, sugestões, parcerias ou questões de segurança, entre em contato pelos canais acima. Veja [`AUTHORS.md`](AUTHORS.md) para mais detalhes.

## Princípios

1. **Responsabilidade única** — uma Skill faz uma coisa bem feita.
2. **Baixo acoplamento** — Skills conversam via contratos bem definidos (entradas e saídas).
3. **Alta coesão** — todo o conteúdo de uma Skill serve ao mesmo objetivo.
4. **Reutilização** — toda Skill deve servir para múltiplas empresas sem alterar sua estrutura.
5. **Configurabilidade** — a personalização ocorre em variáveis de contexto, não no código da Skill.
6. **Padronização** — toda Skill segue o mesmo formato, nomenclatura e governança.

## Estrutura

```
office-skills/
├── README.md                  ← este arquivo
├── ARCHITECTURE.md            ← decisões arquiteturais
├── GOVERNANCE.md              ← regras de contribuição e revisão
├── CONTRIBUTING.md            ← guia de criação de novas Skills
├── INDEX.md                   ← catálogo navegável
├── CHANGELOG.md               ← histórico de versões
├── LICENSE
├── docs/                      ← documentos de especificação
├── assets/                    ← ativos compartilhados (logos, fontes, planilhas base)
├── scripts/                   ← utilitários de validação e indexação
├── tests/                     ← bateria de testes da biblioteca
└── skills/                    ← biblioteca de Skills organizada por domínio
    ├── _core/                 ← Skills transversais (composição, contexto, estilo)
    ├── comercial/             ← propostas, orçamentos, RFP, follow-up, objeções
    ├── administrativo/        ← e-mails, ofícios, memorandos, comunicados
    ├── financeiro/            ← cobranças, custos, orçamento
    ├── gestao/                ← planos, 5W2H, KPIs, OKRs, riscos, roadmaps
    ├── documentacao/          ← POPs, SOPs, manuais, checklists, FAQs
    ├── rh/                    ← vagas, onboarding, avaliação, feedback
    ├── marketing/             ← LinkedIn, site, cases, campanhas
    ├── atendimento/           ← triagem, resposta rápida, encaminhamento
    ├── suporte/               ← tickets, FAQ técnico, base de conhecimento
    ├── produtividade/         ← resumos, planilhas, apresentações, extratores
    └── conhecimento/          ← tradutor corporativo, classificador, organizador
```

## Anatomia de uma Skill

Toda Skill da biblioteca segue o mesmo layout de pasta:

```
skills/<categoria>/<skill-slug>/
├── SKILL.md         ← definição canônica (frontmatter + instruções)
├── README.md        ← visão geral em linguagem humana
├── prompt.md        ← prompt interno otimizado para o agente
├── examples/
│   ├── 01-basico.md
│   ├── 02-intermediario.md
│   └── 03-avancado.md
├── templates/
│   ├── entrada.template.md
│   └── saida.template.md
└── tests/
    └── casos-de-teste.md
```

## Como usar

### 1. Escolha a Skill pelo domínio

Consulte o `INDEX.md` ou navegue por `skills/<categoria>/`. Cada categoria agrupa Skills afins.

### 2. Forneça as entradas esperadas

Cada Skill declara explicitamente suas entradas. Preencha-as em formato estruturado.

### 3. Receba a saída esperada

A saída respeita o template padrão da Skill, em Markdown pronto para uso ou conversão.

### 4. Combine Skills em fluxos

Skills são componíveis. Exemplos de fluxos prontos estão em `docs/fluxos/`.

## Status da biblioteca

Esta é a **versão inicial (0.1.0)** com catálogo arquitetado, Skills core, comerciais, administrativas, de documentação, gestão, finanças, RH, marketing, atendimento, suporte, produtividade e conhecimento.

## Licença

MIT — veja `LICENSE`.

## Inspiração

A disciplina de "Skills como documentação executável" segue o modelo do projeto [Superpowers](https://github.com/obra/superpowers), adaptando-o de engenharia de software para rotinas corporativas genéricas.