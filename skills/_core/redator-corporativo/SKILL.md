---
name: redator-corporativo
description: Use quando precisar redigir ou revisar qualquer texto que represente a empresa — e-mails, propostas, ofícios, posts, comunicados. Garante tom, vocabulário e padrão consistentes.
category: _core
priority: essencial
depends_on: []
composes_with:
  - _core/configurador-empresa
  - comercial/proposta-comercial
  - administrativo/email-corporativo
  - documentacao/padronizador-textos
version: 0.1.0
status: rascunho
---

# Redator Corporativo

## Objetivo
Produzir e revisar textos corporativos com tom, vocabulário e estrutura alinhados à identidade da empresa configurada em `config/empresa.yaml`.

## Quando usar
- Redigir qualquer comunicação escrita em nome da empresa.
- Revisar rascunhos existentes antes do envio.
- Padronizar tom entre diferentes autores.

## Quando NÃO usar
- Conversas informais internas (chat, mensagem rápida).
- Textos jurídicos ou técnicos altamente especializados (usar skill específica).
- Conteúdo acadêmico.

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `objetivo` | texto | sim | Finalidade do texto |
| `publico` | texto | sim | Quem vai ler |
| `tom` | enum | sim | formal / semiformal / informal |
| `rascunho` | texto | não | Texto pré-existente para revisão |
| `restricoes` | lista | não | Tamanho, termos a evitar |

## Saídas esperadas
Markdown com o texto final revisado, observações pontuais (em bloco `>`) e versão limpa pronta para uso.

## Fluxo interno
1. Carregar `config/empresa.yaml`.
2. Identificar objetivo e público.
3. Se houver rascunho, revisar; senão, redigir do zero.
4. Aplicar tom configurado e remover vocabulário bloqueado.
5. Validar checklist (clareza, tamanho,礼貌).
6. Entregar texto final + comentários opcionais.

## Boas práticas
- Frases curtas (média 15–20 palavras).
- Listas e tabelas quando a estrutura ajudar.
- Citar dados quando disponíveis; assumir com cautela.
- Sempre oferecer uma versão limpa.

## Limitações
- Não verifica ortografia multilíngue automaticamente.
- Não avalia adequação jurídica.
- Não substitui revisão humana em comunicações críticas.

## Dependências
- `_core/configurador-empresa`

## Exemplos de uso
Veja `examples/`.

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Microsoft Word
- Google Docs
- Qualquer editor Markdown