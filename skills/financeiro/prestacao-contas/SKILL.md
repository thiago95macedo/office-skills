---
name: prestacao-contas
description: Use para documentar uso de recursos em projeto, viagem, evento ou verba corporativa, com rastreabilidade de cada item.
category: financeiro
priority: recomendada
depends_on: []
composes_with:
  - financeiro/cobranca
  - gestao/plano-acao
  - gestao/gestao-riscos
version: 0.2.0
status: estavel
references:
  - BRASIL. CF/88 arts. 70, 71 e 74 — Fiscalização financeira.
  - BRASIL. Lei 13.019/2014 (MROSC) alterada pela Lei 13.204/2015.
  - BRASIL. IN TCU 84/2020 — Prestação de contas anual.
  - BRASIL. Lei 12.527/2011 — LAI (Lei de Acesso à Informação).
  - CGU. Manual de Tomada de Contas Especial.
  - TCU. Resolução 155/2024 e IN-TCU 98/2025.
---

# Prestação de Contas

## Objetivo
Documentar com transparência, rastreabilidade e auditabilidade o uso de recursos financeiros em projeto, viagem, evento, verba corporativa ou parceria com o setor público.

## Quando usar
- Após viagem corporativa com reembolso.
- Após evento patrocinado pela empresa.
- Em prestação de contas de projeto com verba designada.
- Em auditoria interna (compliance, controle).
- Em prestação de contas ao TCU (órgão público) ou MROSC (OSC parceira).
- Em tomada de contas especial (TCE).

## Quando NÃO usar
- Para simples relatório de despesas pontuais (usar `produtividade/resumo-executivo`).
- Para contabilização fiscal (usar ferramenta contábil — ERP, sistema fiscal).
- Para fluxo de caixa operacional (usar sistema de tesouraria).

## Modalidades de prestação de contas

| Modalidade | Marco legal | Aplicação |
|------------|-------------|-----------|
| **Interna corporativa** | Política interna | Verba de projeto, viagem, evento |
| **MROSC** | Lei 13.019/2014 + 13.204/2015 | OSC parceira da Administração Pública |
| **Anual ao TCU/CGU** | IN TCU 84/2020 | Órgão público federal |
| **Tomada de Contas Especial (TCE)** | Res. TCU 155/2024 + IN-TCU 98/2025 | Apuração de prejuízo específico |
| **Convênio/Acordo** | Decreto e cláusulas específicas | Acordos com governo |

## Estrutura recomendada (compatível com múltiplos marcos)

| # | Bloco | Conteúdo |
|---|-------|----------|
| 1 | **Cabeçalho** | Identificação do projeto, período, responsável, centro de custo |
| 2 | **Resumo executivo** | Totais, saldo, parecer em 1 parágrafo |
| 3 | **Receita / Recursos recebidos** | Origem, valor, data de cada repasse |
| 4 | **Despesas** | Tabela numerada: item, data, fornecedor, NF/recibo, valor, categoria |
| 5 | **Totalização** | Recebido, gasto, saldo (a devolver ou a receber) |
| 6 | **Análise de desvios** | Variações relevantes e justificativas |
| 7 | **Conformidade legal** | Itens conforme / não conforme / com ressalva |
| 8 | **Pendências** | Itens sem comprovante, divergências, prazos |
| 9 | **Parecer** | Aprovado / Pendente / Reprovado com responsável |
| 10 | **Anexos** | Comprovantes, NF, recibos, extratos bancários |
| 11 | **Assinaturas** | Responsável, aprovador, controladoria |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `periodo` | string | sim | Período coberto (datas ou mês/ano) |
| `responsavel` | string | sim | Nome e cargo do responsável |
| `centro_custo` | string | sim | Centro de custo / projeto / convênio |
| `itens` | lista | sim | Despesas com data, fornecedor, NF, valor |
| `valor_total_recebido` | number | sim | Soma dos repasses |
| `valor_total_gasto` | number | sim | Soma das despesas |
| `saldo` | number | sim | Diferença (a devolver ou a receber) |
| `comprovantes` | lista | sim | Referências a NF / recibos / anexos |
| `marco_legal` | enum | sim | corporativo / mrosc / tcu / tce / convenio |
| `aprovador` | string | sim | Quem aprova a prestação |

## Saídas esperadas
- Cabeçalho com identificação completa.
- Tabela numerada de despesas com data, fornecedor, NF, valor.
- Total recebido, gasto, saldo.
- Análise de desvios e justificativas.
- Lista de pendências (comprovantes faltantes).
- Parecer final (aprovado / pendente / reprovado).
- Lista de anexos referenciada.

## Fluxo interno
1. Receber período, responsável e centro de custo.
2. Listar itens numerados sequencialmente (1, 2, 3...).
3. Para cada item, exigir data, fornecedor, NF/recibo, valor, categoria.
4. Calcular totais (recebido, gasto, saldo).
5. Sinalizar itens sem comprovante como pendência.
6. Identificar desvios relevantes (> 10% ou fora da categoria planejada).
7. Validar conformidade legal conforme `marco_legal`.
8. Emitir parecer (aprovado, pendente ou reprovado).
9. Listar anexos (comprovantes digitalizados).
10. Submeter para aprovação antes de arquivar.

## Boas práticas
- **Numerar itens sequencialmente** (rastreabilidade).
- **Citar NF/recibo** de cada item (não aceitar itens sem comprovante).
- **Sinalizar divergências** (categoria, valor, data).
- **Documentar saldo** explicitamente (a devolver ou a receber).
- **Categorização consistente** entre prestações (viagens, alimentação, hospedagem, transporte).
- **Conferência cruzada** com extrato bancário da conta específica (MROSC).
- **Aprovação antes de arquivar** — quem assina a prestação.
- **Arquivo digital** com indexação (palavras-chave, período, projeto).
- **Retenção conforme legislação** (5 anos ou mais, conforme normativo).
- **MROSC**: extrato bancário da conta específica é obrigatório.

## Armadilhas comuns
- Itens sem NF ou recibo (geram pendência automática).
- Itens classificados em categoria errada (alimentação como "material de escritório").
- Saldo não documentado (a devolver ou a receber).
- Falta de assinaturas (responsável, aprovador, controladoria).
- Misturar despesas pessoais com corporativas.
- Prestação fora do prazo (MROSC: anual; TCU: anual; corporativo: variável).
- Não publicar demonstrativos (LAI exige transparência ativa).
- Não devolver saldo não aplicado (MROSC — obrigatório).
- Usar conta pessoal para receber repasse (MROSC — exige conta específica).

## Limitações
- Não verifica autenticidade de comprovantes (responsabilidade do aprovador).
- Não calcula impostos sobre reembolsos (responsabilidade fiscal/contábil).
- Não audita se despesa foi efetivamente necessária (análise qualitativa).
- Não substitui parecer jurídico quando há questionamento de legalidade.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Prestação de contas de viagem corporativa
- `02-intermediario.md` — Prestação de contas de evento patrocinado
- `03-avancado.md` — Prestação de contas MROSC de OSC

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- ERP (SAP, TOTVS, Omie)
- Sistema de reembolso (ExpenseOn, SAP Concur)
- GED (SharePoint, Docuware, TOTVS)
- Portal da Transparência (governo)
- Sistemas de prestação de contas públicas (SICONV, TransfereGov)