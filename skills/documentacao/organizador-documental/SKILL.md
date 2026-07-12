---
name: organizador-documental
description: Use para propor estrutura de pastas, convenção de nomes e taxonomia para acervos corporativos.
category: documentacao
priority: opcional
depends_on: []
composes_with:
  - conhecimento/classificador-documentos
  - produtividade/organizador-arquivos
  - documentacao/padronizador-textos
version: 0.2.0
status: estavel
references:
  - ISO 15489-1:2016 — Gestão de documentos.
  - ABNT NBR ISO 8601 — Datas.
  - Conway, P. (Pryor) — Records Management theory.
  - ARMA International — Generally Accepted Recordkeeping Principles (GARP).
---

# Organizador Documental

## Objetivo
Propor estrutura de pastas, convenção de nomes e taxonomia para acervos corporativos, garantindo encontrabilidade, retenção adequada e conformidade.

## Quando usar
- Início de operação ou reorganização de acervo.
- Migração de sistema de gestão documental (DMS).
- Padronização de nomenclatura entre áreas.
- Conformidade com requisitos de retenção (legal, fiscal, contratual).
- Onboarding de equipe em estrutura existente.

## Quando NÃO usar
- Para arquivos pessoais (usar `produtividade/organizador-arquivos`).
- Para biblioteca digital acadêmica (usar padrões de catalogação bibliográfica).
- Para taxonomia de conhecimento (usar `conhecimento/mapa-conhecimento`).

## Princípios de organização documental (ISO 15489, ARMA GARP)

| Princípio | Aplicação |
|-----------|-----------|
| **Integridade** | Documento é confiável, autêntico e completo |
| **Autenticidade** | Proveniência rastreável, sem alteração indevida |
| **Confiabilidade** | Conteúdo representa fato ou ato |
| **Usabilidade** | Encontrável, recuperável, interpretável |
| **Retenção** | Prazo definido conforme legislação ou necessidade |
| **Descarte** | Eliminação controlada quando expirada retenção |

## Estrutura recomendada

| Nível | Convenção | Exemplo |
|-------|-----------|---------|
| **1 - Área / Unidade** | Nome da área ou unidade | `financeiro/`, `comercial/`, `rh/` |
| **2 - Tipo de documento** | Política, contrato, ata, relatório | `politicas/`, `contratos/`, `atas/` |
| **3 - Subtema / Categoria** | Tema específico | `politicas/seguranca/`, `contratos/clientes/` |
| **4 - Documento** | Arquivo individual com convenção de nome | `politicas/seguranca/POL-SEG-007-v1.0.md` |

## Convenção de nomes recomendada

| Componente | Padrão | Exemplo |
|------------|--------|---------|
| **Código** | TIPO-AREA-NNN | `POL-SEG-007` |
| **Título** | Descrição curta, sem espaços especiais | `politica-acesso-dados` |
| **Versão** | `vX.Y` (maior.menor) | `v1.0`, `v1.1` |
| **Data** | ISO 8601 (AAAA-MM-DD) | `2026-07-12` |
| **Status** | (opcional) | `rascunho`, `aprovado`, `arquivado` |

**Formato completo**: `[CÓDIGO]_[título-curto]_v[X.Y]_[AAAA-MM-DD].[ext]`
**Exemplo**: `POL-SEG-007_acesso-dados_v1.0_2026-07-12.pdf`

## Tipos de documento e prefixos sugeridos

| Tipo | Prefixo | Exemplo |
|------|---------|---------|
| Política | POL | POL-COM-001 |
| Procedimento / POP | POP / SOP | POP-FIN-007 |
| Manual | MAN | MAN-TI-003 |
| Formulário | FOR | FOR-RH-012 |
| Ata | ATA | ATA-DIR-2026-001 |
| Contrato | CTR | CTR-CL-2026-0042 |
| Relatório | REL | REL-COM-MENSAL-2026-06 |
| Apresentação | APR | APR-DIR-Q3-2026 |
| Comunicado | COM | COM-RH-2026-15 |
| Memorando | MEM | MEM-FIN-2026-22 |

## Categorização por sensibilidade (LGPD)

| Nível | Tipo | Medida |
|-------|------|--------|
| **Público** | Marketing, institucional | Acesso amplo |
| **Interno** | Operacional, administrativo | Acesso por colaborador |
| **Confidencial** | Estratégico, financeiro, RH | Acesso por papel/área |
| **Restrito** | Pessoal, jurídico, sigilo | Acesso por nome, auditado |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tipo_acervo` | enum | sim | corporativo / projeto / área / pessoal |
| `volumetria_estimada` | int | sim | Quantidade estimada de documentos |
| `usuarios` | lista | sim | Quem acessa (áreas, papéis) |
| `requisitos_retencao` | dict | não | Prazos de retenção por tipo |
| `nivel_sigilo` | enum | sim | publico / interno / confidencial / restrito |
| `sistema_gestao` | enum | sim | SharePoint / Google Drive / pasta-rede / DMS |

## Saídas esperadas
- Mapa de estrutura de pastas (multi-nível).
- Convenção de nomes formal.
- Tabela de prefixos por tipo de documento.
- Política de retenção por categoria.
- Regras de acesso por nível de sigilo.
- Guia de uso para colaboradores.

## Fluxo interno
1. Receber tipo de acervo, volumetria, usuários e nível de sigilo.
2. Definir estrutura de pastas por área → tipo → categoria.
3. Definir convenção de nomes com prefixos padronizados.
4. Mapear retenção por tipo (fiscal, legal, contratual).
5. Definir regras de acesso por nível de sigilo.
6. Gerar guia de uso para colaboradores.
7. Documentar exceções (documentos que fogem do padrão).

## Boas práticas
- **Estrutura rasa** — evitar mais de 4-5 níveis de profundidade.
- **Convenção fixa** — todos os autores seguem o mesmo padrão.
- **Nomes descritivos** — título do documento legível.
- **Datas em ISO 8601** — `AAAA-MM-DD` (ordenável, internacional).
- **Versionamento explícito** — `vX.Y` no nome do arquivo.
- **Categorização por sensibilidade** — separar público, interno, confidencial, restrito.
- **Retenção definida** — quanto tempo cada tipo fica arquivado.
- **Descarte controlado** — eliminação registrada, conforme retenção.
- **Busca otimizada** — nomenclatura que ajuda em busca (palavras-chave).
- **Auditoria** — log de quem acessou/criou/alterou.
- **Migração** — plano para transferir entre sistemas.
- **Backup** — política de cópia de segurança conforme criticidade.
- **Acessibilidade** — descrições alternativas para imagens, PDF/A para preservação.

## Armadilhas comuns
- Estrutura profunda demais (mais de 5 níveis) — usuário não encontra.
- Nomes com caracteres especiais (`!@#$%`) — quebra em sistemas.
- Sem prefixo de tipo — não é possível filtrar por tipo.
- Sem versionamento — sobrescritas acidentais.
- Sem retenção definida — acúmulo infinito de documentos.
- Múltiplas cópias sem sincronização — versões conflitantes.
- Falta de auditoria — sem rastreabilidade de acessos.
- Categoria sigilosa sem controle de acesso.
- Documentos sem metadata (autor, data, área).

## Limitações
- Não substitui classificação por conteúdo (usar `classificador-documentos`).
- Não acessa DMS em tempo real (depende de integração).
- Não realiza migração automática entre sistemas.
- Não verifica conformidade legal específica (usar consultoria jurídica).

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Estrutura de acervo de área comercial
- `02-intermediario.md` — Estrutura corporativa multi-área
- `03-avancado.md` — Estrutura com retenção e LGPD

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- DMS (SharePoint, Docuware, TOTVS, Laserfiche)
- Google Drive / Workspace
- OneDrive / SharePoint
- ECM (Alfresco, Nuxeo)
- Sistemas de backup (Veeam, Acronis)