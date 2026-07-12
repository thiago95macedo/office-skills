---
name: classificador-documentos
description: Use para classificar documentos por tipo (contrato, NF, relatório, proposta, ata) e tema automaticamente, com LGPD-aware.
category: conhecimento
priority: essencial
depends_on: []
composes_with:
  - documentacao/organizador-documental
  - produtividade/extrator-dados
  - gestao/prestacao-contas
version: 0.2.0
status: estavel
references:
  - Dublin Core Metadata Element Set (DCMI).
  - ISO 23081-1:2017 — Records management metadata.
  - BRASIL. LGPD Lei 13.709/2018 (categorias especiais de dados).
  - BRASIL. Decreto 10.278/2020 — Documentos digitais (padrões de classificação).
---

# Classificador de Documentos

## Objetivo
Classificar documentos por tipo (contrato, NF, relatório, proposta, ata, política) e tema (comercial, financeiro, RH), com tag de sensibilidade LGPD e caminho sugerido.

## Quando usar
- Triagem automática de documentos em GED.
- Organização de acervos migrados.
- Indexação para busca.
- Triagem inicial de e-mails com anexos.
- Auto-classificação em sistemas de gestão documental.

## Quando NÃO usar
- Para documento já classificado.
- Para documentos com regras específicas de compliance (usar processo dedicado).
- Para PDFs escaneados sem OCR.

## Tipos de documento brasileiros (referência)

| Tipo | Características | Prefixo sugerido |
|------|----------------|------------------|
| **Contrato** | Partes, objeto, valor, vigência | CTR |
| **Proposta comercial** | Escopo, preço, validade | PROP |
| **Nota Fiscal (NF)** | CNPJ/CPF, valor, impostos | NF |
| **Relatório** | Período, métricas, conclusões | REL |
| **Ata** | Reunião, data, participantes | ATA |
| **Política** | Norma interna, versão, aprovação | POL |
| **POP/SOP** | Procedimento, etapas, responsável | POP |
| **Manual** | Documentação técnica ou de processo | MAN |
| **Memorando** | Comunicação interna formal | MEM |
| **Ofício** | Comunicação externa formal | OF |
| **Recibo** | Comprovante de pagamento | REC |
| **Atestado** | Declaração de fato | ATEST |

## Categorias de sensibilidade (LGPD)

| Nível | Tipo de dado | Medida |
|-------|--------------|--------|
| **Público** | Marketing, institucional | Acesso amplo |
| **Interno** | Operacional, administrativo | Acesso por colaborador |
| **Confidencial** | Estratégico, financeiro | Acesso por papel |
| **Restrito** | Pessoal, jurídico, sigilo | Acesso auditado, base legal explícita |
| **Sensível (LGPD art. 5º, II)** | Saúde, criança, opinião política, dado biométrico | Acesso excepcional + base legal |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `documentos` | lista | sim | Lista de documentos a classificar |
| `taxonomia` | dict | sim | Categorias permitidas |
| `saida_desejada` | enum | sim | tags / pasta / rota / todas |
| `lgpd_aware` | bool | sim | Detectar dados sensíveis? (default: true) |
| `caminho_destino` | string | não | Raiz do GED para sugerir caminho |

## Saídas esperadas
- Tipo do documento (com confiança).
- Tema/categoria.
- Tags de sensibilidade.
- Caminho sugerido no GED.
- Lista de documentos sensíveis (LGPD) para revisão.
- Estatísticas de cobertura.

## Fluxo interno
1. Receber lista de documentos e taxonomia.
2. Para cada documento, extrair metadados (título, data, remetente, palavras-chave).
3. Classificar por tipo (baseado em heurísticas + taxonomia).
4. Classificar por tema (área/departamento).
5. Detectar dados sensíveis (LGPD art. 5º, II).
6. Sugerir caminho no GED conforme taxonomia e organização.
7. Marcar para revisão humana quando confiança < 0.7.
8. Listar documentos sensíveis para verificação adicional.

## Boas práticas
- **Taxonomia explícita** — não inferir tipos fora do permitido.
- **Confiança por documento** — saber quando revisar.
- **LGPD em primeiro plano** — sinalizar dados sensíveis automaticamente.
- **Metadados consistentes** — schema conhecido (Dublin Core, ISO 23081).
- **Caminho reproduzível** — fórmula `unidade/tipo/ano/codigo`.
- **Auditoria** — log de classificações para revisão posterior.
- **Retenção vinculada** — documento + prazo de retenção.
- **Backup de metadados** — não perder indexação.
- **Acessibilidade** — descrições para imagens, OCR para PDFs.

## Armadilhas comuns
- Classificação incorreta por nome ambíguo.
- Não detectar LGPD (dados sensíveis sem tratamento).
- Tag de sensibilidade padrão (sem análise real).
- Classificação sem logs (sem auditoria).
- Múltiplas tags conflitantes (sobreposição).
- Caminho inexistente no GED (sugestão inválida).

## Limitações
- Não lê PDFs sem OCR.
- Não acessa sistema de arquivos diretamente.
- Não detecta fraude documental.
- Não substitui revisão humana em compliance.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Triagem de pasta de e-mails
- `02-intermediario.md` — Organização de acervo de NF
- `03-avancado.md` — Migração com LGPD em massa

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- GED (SharePoint, Docuware, TOTVS)
- OCR (Google Vision, Tesseract, AWS Textract)
- ECM (Alfresco, Nuxeo)
- Sistemas de classificação automática (ML)