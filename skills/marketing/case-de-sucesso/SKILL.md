---
name: case-de-sucesso
description: Use para estruturar cases de sucesso a partir de resultados reais do cliente, com aprovação formal e narrativa baseada em evidência.
category: marketing
priority: recomendada
depends_on:
  - _core/redator-corporativo
composes_with:
  - marketing/conteudo-linkedin
  - marketing/conteudo-site
  - marketing/artigo-blog
version: 0.2.0
status: estavel
references:
  - HubSpot — Customer Case Study Structure (componentes canônicos: Company Overview, Challenge, Solution, Results, Takeaway).
  - Mager, R.; Mager, B. How to Measure Success. 1990s.
  - BRASIL. LGPD Lei 13.709/2018 (consentimento para uso de imagem/dados em case público).
---

# Case de Sucesso

## Objetivo
Construir narrativa de case com contexto, desafio, solução, resultados mensuráveis, depoimento e próximos passos, com aprovação formal do cliente.

## Quando usar
- Após projeto bem-sucedido com impacto mensurável.
- Para uso comercial (site, propostas, pitch).
- Para uso institucional (mídia, eventos).
- Para case de onboarding ou case de inovação interna.
- Para alimentar a base de prova social (sales enablement).

## Quando NÃO usar
- Para case sem aprovação formal do cliente.
- Para case sem resultados mensuráveis.
- Para case com cláusulas de confidencialidade ainda ativas.
- Para propaganda ou publieditorial (usar formato específico).

## Componentes canônicos (HubSpot Case Study Framework)

| Componente | Conteúdo | Orientação |
|------------|----------|------------|
| **1. Company Overview** | Apresentação do cliente (setor, porte, mercado) | 2-3 frases |
| **2. Challenge** | Dor ou oportunidade que motivou | Concreto e específico |
| **3. Solution** | Solução aplicada, etapas, diferenciais | Foco em abordagem |
| **4. Results** | Resultados mensuráveis (antes vs depois) | Com números e prazos |
| **5. Takeaway** | Aprendizado generalizável | Útil para outros clientes |

## Estrutura recomendada

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Cliente, projeto, período, aprovação |
| 2 | **Resumo** | 1 parágrafo com problema → solução → resultado |
| 3 | **Contexto do cliente** | Setor, porte, situação inicial |
| 4 | **Desafio** | Dor ou oportunidade |
| 5 | **Solução aplicada** | Etapas, equipe, tecnologias |
| 6 | **Resultados** | Métricas com baseline e comparação |
| 7 | **Depoimento** | Citação do cliente (literal, com nome e cargo) |
| 8 | **Aprendizados** | O que pode servir para outros clientes |
| 9 | **Próximos passos** | Continuidade da parceria, expansão |
| 10 | **CTA** | Contato, avaliação, agendamento |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `cliente.nome` | string | sim | Razão social |
| `cliente.setor` | string | sim | Setor de atuação |
| `cliente.porte` | enum | sim | MEI / EPP / Media / Grande / Enterprise |
| `desafio` | string | sim | Dor ou oportunidade |
| `solucao` | string | sim | O que foi entregue |
| `resultados` | lista | sim | Métricas com baseline e comparação |
| `depoimento` | string | não | Citação do cliente |
| `aprovacao_cliente` | bool | sim | Cliente revisou e autorizou publicação? |
| `aprovador_cliente` | string | sim | Nome e cargo de quem autorizou |
| `data_aprovacao` | data | sim | ISO 8601 |
| `confidencialidade` | enum | sim | publica / restrita-nomeacao / sigilosa |
| `case_format` | enum | sim | blog / video / pdf / institucional / midia |

## Saídas esperadas
- Cabeçalho com aprovação formal registrada.
- Resumo em 1 parágrafo.
- 5 componentes canônicos estruturados.
- Depoimento (quando aplicável) com nome e cargo.
- Próximos passos e CTA.
- Versão de aprovação com responsável e data.

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom institucional).
2. **Confirmar aprovação formal do cliente** — obrigatório (LGPD + ético).
3. Receber dados do projeto (desafio, solução, resultados).
4. Estruturar 5 componentes canônicos (Company, Challenge, Solution, Results, Takeaway).
5. Quantificar resultados com baseline (antes vs depois).
6. Coletar depoimento (literal, com nome e cargo).
7. Validar métricas com cliente antes de publicar.
8. Revisar com cliente a versão final.
9. Submeter para aprovação interna (marketing + comercial).
10. Publicar conforme formato escolhido.

## Boas práticas
- **Aprovação formal** — registro em e-mail ou sistema antes de publicar.
- **Resultados mensuráveis** — antes vs depois, com números.
- **Depoimento literal** — citação exata, com nome e cargo.
- **Clareza de números** — % de aumento, redução de tempo, receita adicional.
- **Narrativa honesta** — sem exagero ou promessas não cumpridas.
- **LGPD** — consentimento para uso de imagem/dados em case público.
- **Versão por canal** — site, LinkedIn, PDF, mídia.
- **Reaproveitamento** — case vira slides para pitch, post, vídeo.
- **Case em séries** — vários cases do mesmo segmento geram cluster de autoridade.
- **Linkagem interna** — case linka para página de serviço/produto.
- **Atualização periódica** — números desatualizados perderam credibilidade.

## Armadilhas comuns
- Publicar sem aprovação do cliente (risco jurídico e ético).
- Resultados sem baseline (não há comparação).
- Hiperbólico ("transformação total") — sem evidência.
- Misturar depoimentos reais e fictícios.
- Sem métricas claras (vago: "resultados incríveis").
- Case desatualizado (números antigos).
- Confidencialidade violada (dados sigilosos em case público).
- Cliente infeliz e case publicado (risco de reputação).
- Tratar como propaganda — perde credibilidade.
- Não atualizar (anúncios referenciando números antigos).

## Limitações
- Não entrevista o cliente (apenas registra depoimento recebido).
- Não coleta métricas automaticamente (depende de CRM, ERP).
- Não produz infográficos ou animações (apenas texto estruturado).
- Não substitui processo de aprovação jurídica.
- Não verifica cláusulas contratuais de confidencialidade.

## Dependências
- `_core/redator-corporativo`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Case de transformação digital em média empresa
- `02-intermediario.md` — Case B2B com múltiplas métricas e depoimento
- `03-avancado.md` — Case com impactos em múltiplos indicadores

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- CRM (RD, HubSpot, Salesforce) — para coleta de métricas
- Site institucional (WordPress, Webflow)
- Slide (PowerPoint, Google Slides, Keynote) — para pitch
- Ferramentas de vídeo (Loom, OBS) — para case em vídeo
- LinkedIn (post e artigo)