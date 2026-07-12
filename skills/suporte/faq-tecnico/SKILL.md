---
name: faq-tecnico
description: Use para construir FAQ técnico sobre produtos/serviços com respostas verificáveis e links para documentação.
category: suporte
priority: recomendada
depends_on: []
composes_with:
  - documentacao/faq-corporativo
  - suporte/base-conhecimento
  - classificador-tickets
version: 0.2.0
status: estavel
references:
  - Krug, S. Don't Make Me Think, Revisited. 3. ed. 2013.
  - Nielsen, J. — Writing for the Web (escaneabilidade).
  - KCS® v6 Practices Guide — Consortium for Service Innovation.
  - Dalkir, K. Knowledge Management in Theory and Practice. 4. ed. 2023.
---

# FAQ Técnico

## Objetivo
Construir FAQ técnico com perguntas frequentes, respostas precisas, links para documentação técnica e indicador de versão do produto/serviço.

## Quando usar
- Base de conhecimento pública (clientes externos).
- Central de ajuda de produto (help center).
- Autoatendimento técnico.
- Documentação de troubleshooting comum.

## Quando NÃO usar
- Para FAQ institucional geral (usar `documentacao/faq-corporativo`).
- Para documentação técnica completa (usar `documentacao/manual-tecnico`).
- Para POPs internos (usar `documentacao/pop-sop`).

## Estrutura recomendada

| Bloco | Conteúdo |
|-------|----------|
| **Cabeçalho** | Produto, versão, data, responsável |
| **Sumário** | Navegação por categoria |
| **Categorias** | Instalação, Configuração, Uso, Troubleshooting |
| **Pergunta** | Linguagem do usuário |
| **Resposta** | Curta, técnica, com passos numerados |
| **Links** | Para documentação completa |
| **Versão do produto** | Indicada em cada resposta |
| **Última atualização** | Data |
| **Contato para suporte humano** | Quando necessário |

## Anatomia de boa resposta técnica

| Aspecto | Orientação |
|---------|------------|
| **Resposta direta** | Sim/Não/Depende — 1 frase na primeira linha |
| **Pré-requisitos** | Versão do produto, sistema operacional |
| **Passos numerados** | Sequência lógica |
| **Comandos** | Bloco de código formatado |
| **Capturas de tela** | Quando ajudam (não substituem texto) |
| **Erros comuns** | "Se aparecer erro X, faça Y" |
| **Links profundos** | Para doc oficial |
| **Versão do produto** | Sempre indicada |

## Princípios de redação técnica

- **Resposta escaneável** — Krug, Nielsen: bullets, parágrafos curtos.
- **Conclusão primeiro** — resposta antes da explicação.
- **Sem ambiguidade** — passos verificáveis.
- **Versionamento** — resposta vinculada à versão do produto.
- **Testado** — passos foram realmente executados.
- **Semarketing** — técnico não vende, informa.
- **Sem jargão desnecessário** — explicar termos quando essencial.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `produto` | string | sim | Nome do produto/serviço |
| `versao_produto` | string | sim | Versão atual |
| `perguntas_respostas` | lista | sim | Pares pergunta/resposta |
| `referencias` | lista | sim | Links para doc oficial |
| `audiencia` | enum | sim | cliente-externo / parceiro / interno |
| `categoria` | enum | sim | instalacao / configuracao / uso / troubleshooting / faq |
| `responsavel_manutencao` | string | sim | Equipe dona |

## Saídas esperadas
- Cabeçalho com produto, versão e data.
- Sumário navegável.
- Perguntas agrupadas por categoria.
- Respostas com passos numerados.
- Bloco de código formatado para comandos.
- Links para documentação técnica.
- Data de última atualização.
- Canal para suporte humano.

## Fluxo interno
1. Carregar `config/empresa.yaml` (produto, versão).
2. Receber lista de perguntas e respostas.
3. Categorizar perguntas (Instalação, Uso, Troubleshooting).
4. Reescrever perguntas na linguagem do usuário.
5. Redigir respostas com conclusão primeiro.
6. Adicionar passos numerados quando a sequência importa.
7. Formatar comandos em bloco de código.
8. Adicionar links para documentação técnica.
9. Indicar versão do produto em cada resposta.
10. Definir responsável pela manutenção.

## Boas práticas
- **Conclusão primeiro** — "Sim, basta..." / "Não, isso não é suportado".
- **Comandos em bloco de código** com syntax highlighting.
- **Capturas de tela** com alt text descritivo.
- **Erro → Solução** — "Se você ver o erro E404, siga X".
- **Links internos profundos** — para seção específica da doc.
- **Versionamento** — vincular resposta à versão do produto.
- **Responsável técnico** — manter respostas atualizadas.
- **Atualização periódica** — conteúdo envelhece com release.
- **Busca otimizada** — perguntas como usuário pesquisaria.
- **Sem ambiguidade** — passos verificáveis.
- **Acessibilidade** — compatível com leitor de tela.

## Armadilhas comuns
- Resposta desatualizada (não vinculou à versão).
- Comandos não testados (criam confusão).
- Sem link para doc oficial (referência fraca).
- Linguagem de marketing (técnico não convence, informa).
- Sem passos numerados ("configure X" — como?).
- Código sem syntax highlighting.
- Sem alternativa para versões antigas.
- Erro comum sem solução.
- Imagens sem alt text.
- Atualização lenta (releases sem atualização do FAQ).

## Limitações
- Não testa links quebrados (depende de ferramenta separada).
- Não acessa base de código do produto.
- Não gera animações ou GIFs.
- Não mede resolução por autoatendimento (depende de métricas).

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — FAQ de onboarding de usuário
- `02-intermediario.md` — FAQ de troubleshooting com comandos
- `03-avancado.md` — FAQ de API com exemplos de código

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Help center (Zendesk Guide, Freshdesk, Document360)
- Knowledge base (Confluence, Notion, GitBook)
- CMS técnico (Docusaurus, Mintlify, ReadMe)
- Search engine interno (Algolia, Elasticsearch)