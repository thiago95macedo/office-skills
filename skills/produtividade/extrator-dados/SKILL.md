---
name: extrator-dados
description: Use para extrair dados estruturados (campos, tabelas, listas) de texto não estruturado conforme schema definido.
category: produtividade
priority: essencial
depends_on: []
composes_with:
  - produtividade/analise-planilha
  - conhecimento/classificador-documentos
version: 0.2.0
status: estavel
references:
  - JSON Schema Draft 2020-12 — padrão para validação de estrutura.
  - Pydantic — Python data validation.
  - BRASIL. LGPD Lei 13.709/2018 (dados pessoais em extração).
---

# Extrator de Dados

## Objetivo
Converter texto não estruturado em dados estruturados (JSON, CSV, YAML) conforme schema definido, com sinalização de ambiguidades e confiança.

## Quando usar
- Migração de planilhas legadas (papel → digital).
- Extração de dados de PDFs, e-mails, contratos.
- Padronização de cadastros (clientes, produtos, fornecedores).
- ETL simplificado para análise.
- Construção de datasets de treinamento.

## Quando NÃO usar
- Para dados já estruturados.
- Para documentos com regras complexas e baixa confiabilidade (acima de 80% de erro).
- Para extração em tempo real em alto volume (usar pipeline dedicado).

## Estrutura recomendada de saída

```json
{
  "registros": [
    {
      "campo1": "valor",
      "campo2": "valor",
      "_confianca": {
        "campo1": 0.95,
        "campo2": 0.60
      }
    }
  ],
  "excecoes": [
    {
      "trecho": "texto original",
      "motivo": "campo não identificado",
      "acao_sugerida": "revisão manual"
    }
  ],
  "estatisticas": {
    "total_processado": 100,
    "extraidos": 92,
    "parciais": 5,
    "falhas": 3,
    "confianca_media": 0.87
  }
}
```

## Política de ambiguidade

| Política | Comportamento | Quando usar |
|----------|--------------|-------------|
| **estrito** | Falha se houver ambiguidade | Dados críticos (contratos, NF) |
| **moderado** | Sinaliza ambiguidade, segue | Cadastros gerais |
| **permissivo** | Inferir valor plausível | Bulk import de baixa criticidade |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `fonte` | texto/path | sim | Texto bruto ou arquivo |
| `schema_destino` | dict | sim | Estrutura JSON Schema, exemplo ou template |
| `politica_ambiguo` | enum | sim | estrito / moderado / permissivo |
| `idioma` | enum | sim | pt-BR / en / es |
| `contexto_dominio` | string | não | Domínio de negócio (ex: "NF de restaurante") |
| `poucos_exemplos` | lista | não | Few-shot examples para melhorar extração |

## Saídas esperadas
- Lista de registros no schema definido.
- Lista de exceções com trecho original e motivo.
- Confiança média por campo.
- Estatísticas de cobertura.
- Sugestões de revisão manual.

## Fluxo interno
1. Carregar texto fonte.
2. Carregar schema destino.
3. Identificar entidades conforme schema.
4. Mapear texto para campos.
5. Sinalizar ambiguidades.
6. Aplicar política de ambiguidade.
7. Produzir saída estruturada.
8. Calcular confiança por campo.
9. Listar exceções para revisão humana.
10. Validar com schema (JSON Schema validation).

## Boas práticas
- **Schema explícito** — definição clara antes de começar.
- **Poucos exemplos (few-shot)** — aumenta precisão.
- **Política de ambiguidade explícita** — definir antes.
- **Confiança por campo** — identifica onde revisar.
- **Validação de schema** — saída não-conforme é erro.
- **Tratamento de LGPD** — mascarar ou omitir dados pessoais sensíveis.
- **Idempotência** — processar mesma entrada duas vezes = mesmo resultado.
- **Logs de exceção** — permitir reprocessamento.
- **Comparação com original** — permitir auditoria.
- **Validação humana em baixa confiança** — campos com confiança < 0.7.
- **Documentar transformações** — como campos foram normalizados.

## Armadilhas comuns
- Aceitar tudo sem validar (precisão baixa).
- Política de ambiguidade errada (estrito demais ou permissivo demais).
- Não documentar transformações (impossível auditar).
- Misturar formatos de data (DD/MM/AAAA vs. MM/DD/AAAA).
- Não normalizar nomes (Maria Silva vs. SILVA, MARIA vs. MARIA DA SILVA).
- Não tratar LGPD (dados pessoais em massa).
- Sem validação de schema (saída quebrada).
- Inferência em massa sem revisão (alucinações).

## Limitações
- Não lê anexos sem OCR.
- Não acessa imagens complexas.
- Não infere estrutura desconhecida.
- Não substitui validação humana em dados críticos.

## Dependências
- Nenhuma

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Extração de lista simples
- `02-intermediario.md` — Extração de NF de PDF
- `03-avancado.md` — Extração em massa com política permissiva

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- OCR (Tesseract, Google Cloud Vision, AWS Textract)
- RPA (UiPath, Automation Anywhere)
- Ferramentas de ETL (Apache Airflow, n8n)
- Plataformas low-code (Make, n8n, Zapier)