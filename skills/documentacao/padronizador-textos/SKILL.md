---
name: padronizador-textos
description: Use para aplicar padrão da casa (tom, vocabulário, formatação) a textos existentes sem alterar o conteúdo técnico.
category: documentacao
priority: recomendada
depends_on:
  - _core/redator-corporativo
  - _core/configurador-empresa
composes_with:
  - todas as Skills que produzem texto
version: 0.2.0
status: estavel
references:
  - Strunk, W.; White, E. B. The Elements of Style. 4. ed. 2000.
  - Microsoft Writing Style Guide. Microsoft. 2024.
  - Google developer documentation style guide. Google.
  - Krug, S. Don't Make Me Think, Revisited. 3. ed. 2013.
---

# Padronizador de Textos

## Objetivo
Revisar textos existentes para alinhar tom, vocabulário e formatação ao padrão da empresa, **sem alterar o conteúdo técnico ou o significado original**.

## Quando usar
- Revisar texto redigido por outra pessoa antes de publicação.
- Padronizar tom entre diferentes autores de uma equipe.
- Aplicar vocabulário bloqueado (concorrentes, gírias, regionalismos).
- Adequar texto a novo tom corporativo (rebrand, fusão, mudança de mercado).
- Revisar documentação antiga para novo padrão editorial.

## Quando NÃO usar
- Para redigir texto novo (usar `redator-corporativo`).
- Para revisão técnica (fatos, dados, lógica) — esse papel é técnico, não editorial.
- Para tradução (usar `tradutor-corporativo`).

## Categorias de padronização

| Categoria | O que revisa | Exemplos |
|-----------|--------------|----------|
| **Tom** | Formalidade, postura, voz | Formal → semiformal; "você" → "Sr(a)." |
| **Vocabulário** | Termos preferidos, palavras bloqueadas | "solução completa" → evitar; "cliente" → "parceiro" |
| **Formatação** | Markdown, títulos, listas, ênfase | H1 → H2 quando aplicável; bullets consistentes |
| **Ortografia/gramática** | Acentos, concordância, regência | "beneficiente" → "beneficente" |
| **Estilo** | Frases, parágrafos, escaneabilidade | Parágrafos longos → bullets |
| **Acessibilidade** | Contraste, alt text, semântica | Imagens sem descrição |
| **Conformidade legal** | LGPD, compliance, disclaimers | Dados pessoais sem consentimento |

## Workflow de padronização

| Etapa | Ação | Resultado |
|-------|------|-----------|
| 1. **Inventário** | Listar inconsistências encontradas | Mapa de desvios |
| 2. **Classificação** | Categorizar cada desvio | Tipo e severidade |
| 3. **Correção automática** | Aplicar regras claras (ortografia, formatação) | Mudanças mecânicas |
| 4. **Correção assistida** | Sugerir mudanças para tom e vocabulário | Sugestões ao autor |
| 5. **Preservação do sentido** | Verificar que técnica foi mantida | Texto fiel ao original |
| 6. **Validação** | Revisão por humano em pontos críticos | Aprovação |
| 7. **Versionamento** | Registrar mudanças | Histórico |

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `texto_original` | string | sim | Texto a ser padronizado |
| `alvos_padronizacao` | lista | sim | tom / vocabulario / formatacao / ortografia / estilo / acessibilidade / legal |
| `nivel_rigor` | enum | sim | conservador / padrao / agressivo |
| `preservar_significado` | bool | sim | Se deve manter sentido técnico (default: true) |
| `config_empresa` | string | sim | `config/empresa.yaml` (vocabulário bloqueado, tom) |

## Saídas esperadas
- Texto padronizado (mantendo significado).
- Lista de alterações aplicadas (por categoria).
- Sugestões para revisão humana (mudanças estilísticas).
- Versão original + versão padronizada (diff).

## Fluxo interno
1. Carregar `config/empresa.yaml` (tom padrão, vocabulário bloqueado, regras).
2. Receber texto original.
3. Identificar desvios por categoria (tom, vocabulário, formatação, etc.).
4. Aplicar correções mecânicas (ortografia, formatação Markdown).
5. Sugerir mudanças para tom e vocabulário (não automáticas; requerem revisão).
6. Validar que o significado técnico foi preservado.
7. Sinalizar mudanças que exigem aprovação humana.
8. Entregar versão padronizada + diff de alterações.

## Boas práticas
- **Preservar sentido** — padronização é estilística, não técnica.
- **Vocabulário bloqueado** — substituir termos proibidos por equivalentes.
- **Tom consistente** — formal/semiformal conforme `config/empresa.yaml`.
- **Markdown limpo** — H1-H6 em sequência; bullets consistentes.
- **Frases curtas** — média 15-20 palavras.
- **Sem jargão desnecessário** — adaptar para audiência.
- **Concordância e regência** — revisar português.
- **Acessibilidade** — imagens com alt text, contraste.
- **Diff visível** — permitir que autor revise mudanças.
- **Não automáticas para mudanças estilísticas** — sugerir, não impor.
- **Versionamento** — registrar alterações.
- **Validação humana** — autor original revisa antes de publicar.

## Armadilhas comuns
- **Alterar significado** — "benefícios fiscais" → "benefícios contábeis" (mudou sentido!).
- **Padronização excessiva** — texto fica genérico, perde voz do autor.
- **Tom errado** — forçar formalidade onde original era informal e adequado.
- **Markdown inconsistente** — mistura de `*` e `-` para bullets.
- **Substituir termos técnicos** por sinônimos incorretos.
- **Esquecer vocabulário regional** — uniformizar sem considerar contexto.
- **Quebrar URLs ou referências** — substituição de termo altera identificadores.
- **Não documentar mudanças** — autor não sabe o que mudou.

## Limitações
- Não detecta erros técnicos (fatos, dados, lógica).
- Não substitui revisão humana para textos críticos (jurídico, médico, financeiro).
- Não acessa contexto suficiente para entender ironia, sarcasmo, regionalismo.
- Não garante que a mensagem emocional foi preservada.

## Dependências
- `_core/redator-corporativo`
- `_core/configurador-empresa`

## Exemplos de uso
Veja `examples/`:
- `01-basico.md` — Padronização de tom
- `02-intermediario.md` — Padronização com vocabulário bloqueado
- `03-avancado.md` — Padronização multilíngue (PT-BR / EN)

## Prompt interno recomendado
Veja `prompt.md`.

## Possíveis integrações
- Editores Markdown (Typora, Obsidian, VS Code)
- ProWritingAid, LanguageTool, Grammarly (gramática)
- Processadores de texto (Word, Google Docs com suplementos)
- CMS com revisão (WordPress, Drupal, Contentful)