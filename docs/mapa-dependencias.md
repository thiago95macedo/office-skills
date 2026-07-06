# Mapa de Dependências entre Skills

Este documento descreve as dependências declaradas entre Skills, identificando camadas:

- **Camada 0 (base)** — Skills sem dependência.
- **Camada 1** — Skills que dependem apenas da Camada 0.
- **Camada 2** — Skills que dependem da Camada 1.
- **Camada 3** — Skills que dependem da Camada 2.

## Camada 0 (base)

- `_core/configurador-empresa`
- `_core/redator-corporativo` (independente, mas em geral roda após configurador)
- `documentacao/checklist`
- `conhecimento/classificador-documentos`
- `financeiro/analise-custos`
- `financeiro/prestacao-contas`
- `financeiro/orcamento-empresarial`
- `gestao/plano-acao`
- `gestao/gestao-riscos`
- `gestao/cronograma-projeto`
- `produtividade/extrator-dados`
- `produtividade/organizador-arquivos`
- `rh/feedback-constructivo`
- `suporte/classificador-tickets`
- `suporte/faq-tecnico`
- `suporte/base-conhecimento`
- `atendimento/triagem-mensagens`

## Camada 1

Dependem apenas da Camada 0:

- `_core/organizador-informacao` → `_core/redator-corporativo`
- `comercial/escopo-tecnico` → `_core/redator-corporativo`
- `administrativo/email-corporativo` → `_core/redator-corporativo`
- `administrativo/oficio-memorando` → `_core/redator-corporativo`
- `administrativo/comunicado-interno` → `_core/redator-corporativo`
- `administrativo/carta-corporativa` → `_core/redator-corporativo`
- `documentacao/pop-sop` → `_core/redator-corporativo`
- `documentacao/manual-tecnico` → `_core/redator-corporativo`, `pop-sop`
- `documentacao/faq-corporativo` → `_core/redator-corporativo`
- `documentacao/padronizador-textos` → `_core/redator-corporativo`, `configurador-empresa`
- `documentacao/organizador-documental` → sem deps internas
- `marketing/conteudo-linkedin` → `_core/redator-corporativo`
- `marketing/conteudo-site` → `_core/redator-corporativo`
- `marketing/case-de-sucesso` → `_core/redator-corporativo`
- `marketing/campanha-email` → `administrativo/email-corporativo`
- `marketing/artigo-blog` → `_core/redator-corporativo`
- `rh/descricao-vaga` → `_core/redator-corporativo`
- `rh/onboarding` → `gestao/plano-acao`
- `rh/avaliacao-desempenho` → `rh/feedback-constructivo`
- `rh/treinamento-materiais` → `_core/redator-corporativo`, `documentacao/manual-tecnico`
- `financeiro/cobranca` → `_core/redator-corporativo`
- `financeiro/justificativa-financeira` → `financeiro/analise-custos`
- `atendimento/resposta-rapida` → `_core/redator-corporativo`
- `gestao/matriz-5w2h` → `gestao/plano-acao`
- `gestao/kpi-okr` → sem deps internas
- `gestao/dashboard-executivo` → `gestao/kpi-okr`, `produtividade/resumo-executivo`
- `produtividade/resumo-executivo` → `_core/redator-corporativo`
- `produtividade/tradutor-corporativo` → `_core/redator-corporativo`
- `produtividade/transcricao-tarefas` → `administrativo/ata-reuniao`
- `conhecimento/mapa-conhecimento` → `conhecimento/classificador-documentos`
- `conhecimento/curador-conteudo` → `produtividade/resumo-executivo`

## Camada 2

- `administrativo/ata-reuniao` → `_core/organizador-informacao`
- `produtividade/analise-planilha` → `produtividade/extrator-dados`
- `comercial/orcamento` → `comercial/escopo-tecnico`
- `comercial/follow-up` → `_core/redator-corporativo`
- `comercial/proposta-comercial` → `comercial/escopo-tecnico`, `comercial/orcamento`
- `comercial/resposta-rfp` → `comercial/proposta-comercial`
- `comercial/tratamento-objeções` → `_core/redator-corporativo`
- `comercial/atendimento-lead` → `_core/redator-corporativo`
- `comercial/one-pager` → `_core/redator-corporativo`

## Camada 3 (topo)

- `_core/compositor-fluxos` → `_core/configurador-empresa` (executa qualquer outra Skill em pipeline).

## Skills compostas úteis

- **Proposta comercial completa**: configurador-empresa → escopo-tecnico → analise-custos → orcamento → proposta-comercial → tratamento-objeções → one-pager.
- **Atendimento omnichannel**: triagem-mensagens → classificador-tickets → resposta-rapida → encaminhamento-interno.
- **Fechamento mensal**: checklist → prestacao-contas → cobranca → orcamento-empresarial → dashboard-executivo → ata-reuniao → comunicado-interno.

## Como usar este mapa

1. Antes de criar uma nova Skill, verifique se ela não duplica nenhuma das camadas acima.
2. Ao orquestrar fluxos, respeite a ordem topológica.
3. Para remover uma Skill, avalie o impacto nas dependentes.