---
name: organizador-arquivos
description: Use para sugerir estrutura de pastas, convenção de nomes e regras de versionamento para acervos de arquivos.
category: produtividade
priority: opcional
depends_on: []
composes_with:
  - documentacao/organizador-documental
  - conhecimento/classificador-documentos
version: 0.2.0
status: estavel
references:
  - ISO 8601 — Datas e horas.
  - Conway, P. (Pryor) — Records Management principles.
  - ARMA International — Generally Accepted Recordkeeping Principles (GARP).
---

# Organizador de Arquivos

## Objetivo
Propor convenção de nomes, estrutura de pastas e regras de versionamento para um acervo de arquivos, garantindo encontrabilidade e rastreabilidade.

## Quando usar
- Início de projeto novo.
- Reorganização de área após crescimento.
- Padronização entre times ou filiais.
- Migração entre sistemas de armazenamento.
- Onboarding em estrutura existente.

## Quando NÃO usar
- Para acervo já estruturado.
- Para acervo pessoal (não corporativo).
- Para taxonomia documental completa (usar `documentacao/organizador-documental`).

## Convenção de nomes recomendada (PT-BR)

| Componente | Padrão | Exemplo |
|------------|--------|---------|
| **Código** | TIPO-AREA-NNN | `REL-COM-007` |
| **Data** | ISO 8601 (AAAA-MM-DD) | `2026-07-12` |
| **Versão** | `vX.Y` (maior.menor) | `v1.0`, `v1.1` |
| **Status** | (opcional) | `rascunho`, `aprovado`, `arquivado` |
| **Separador** | `_` ou `-` | `REL-COM-007_relatorio-vendas_2026-Q2_v1.0.pdf` |

**Evitar:** caracteres especiais (`!@#$%`), espaços, acentos (depende do sistema), preposições ("de", "da").

## Tipos de documento e prefixos sugeridos

| Tipo | Prefixo | Exemplo |
|------|---------|---------|
| Relatório | REL | REL-COM-MENSAL-2026-06 |
| Apresentação | APR | APR-DIR-Q3-2026 |
| Planilha | PLN | PLN-FIN-ORC-2026-ANUAL |
| Proposta | PROP | PROP-CL-2026-0042 |
| Contrato | CTR | CTR-CL-2026-0042 |
| Nota Fiscal | NF | NF-2026-12345 |
| Política | POL | POL-SEG-001 |
| Procedimento / POP | POP | POP-FIN-007 |
| Manual | MAN | MAN-TI-003 |
| Formulário | FOR | FOR-RH-012 |

## Estrutura recomendada de pastas

| Nível | Convenção | Exemplo |
|-------|-----------|---------|
| **1 - Unidade** | Nome da área ou unidade | `comercial/`, `financeiro/`, `rh/` |
| **2 - Tipo** | Categoria do documento | `propostas/`, `contratos/`, `relatorios/` |
| **3 - Subtema** | Tema específico | `clientes/`, `fornecedores/`, `campanhas/` |
| **4 - Arquivo** | Documento individual | `[CODIGO]_[titulo]_v[X.Y]_[AAAA-MM-DD].[ext]` |

## Estratégias de versionamento

| Estratégia | Quando usar |
|-----------|-------------|
| **Sobrescrita** | Drafts em construção (não publicar) |
| **Sufixo v1.0, v1.1, v2.0** | Versões publicadas |
| **Sufixo -FINAL, -APROVADO** | Documento aprovado para publicação |
| **Snapshot + datas** | Documentos legais (auditoria) |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `tipo_acervo` | enum | sim | corporativo / projeto / pessoal / area |
| `volumetria` | int | sim | Quantidade estimada de arquivos |
| `usuarios` | lista | sim | Quem acessa |
| `restricoes` | lista | não | Limitações de sistema ou compliance |
| `sistema_gestao` | enum | sim | SharePoint / Google Drive / Pasta-rede / DMS |
| `periodicidade_revisao` | string | não | Frequência de limpeza/reorganização |

## Saídas esperadas
- Mapa de estrutura de pastas (multi-nível).
- Convenção de nomes formal.
- Tabela de prefixos por tipo.
- Regra de versionamento.
- Recomendações de backup e auditoria.

## Fluxo interno
1. Receber tipo de acervo, volumetria e usuários.
2. Definir estrutura de pastas por unidade → tipo → tema.
3. Definir convenção de nomes com prefixos padronizados.
4. Definir regra de versionamento (sufixo, datas, snapshot).
5. Recomendar tipo de arquivo por categoria (PDF/A para preservação, DOCX para colaboração).
6. Sugerir política de backup e auditoria.
7. Documentar exceções (arquivos fora do padrão).

## Boas práticas
- **Estrutura rasa** — máximo 4-5 níveis.
- **Convenção fixa** — todos seguem o mesmo padrão.
- **Datas ISO 8601** — ordenável, internacional.
- **Sem caracteres especiais** — quebra em sistemas.
- **Versionamento explícito** — v1.0, v1.1, v2.0.
- **Status claro** — rascunho / aprovado / arquivado.
- **Backup regular** — política automatizada.
- **Auditoria** — log de acessos quando sigilo.
- **Migração** — plano para mover entre sistemas.
- **PDF/A para preservação** — padrão de longa duração.
- **Acessibilidade** — descrições para imagens.

## Armadilhas comuns
- Estrutura profunda demais (mais de 5 níveis).
- Nomes com espaços ou caracteres especiais.
- Sem prefixo de tipo (não dá para filtrar).
- Sem versionamento (sobrescritas acidentais).
- Sem backup (risco de perda).
- Sem auditoria (sem rastreabilidade).
- Sem revisão periódica (acúmulo descontrolado).

## Limitações
- Não move arquivos automaticamente.
- Não detecta duplicatas.
- Não sugere migração automática.
- Não verifica conformidade legal específica.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Acervo pessoal/pequena equipe
- `02-intermediario.md` — Acervo de área comercial
- `03-avancado.md` — Acervo corporativo multi-área com retenção

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- OneDrive / SharePoint (Microsoft 365)
- Google Drive / Workspace
- GED (Docuware, TOTVS, Laserfiche)
- Backup automatizado (Veeam, Acronis, Duplicati)