---
name: configurador-empresa
description: Use para carregar variáveis de personalização da empresa (tom, vocabulário, dados de contato, assinatura) consumidas pelas demais Skills.
category: _core
priority: recomendada
depends_on: []
composes_with:
  - _core/redator-corporativo
  - todas as Skills que dependem de contexto corporativo
version: 0.1.0
status: rascunho
---

# Configurador de Empresa

## Objetivo
Carregar e expor variáveis de configuração da empresa para uso transversal em todas as Skills.

## Quando usar
- Sempre que uma Skill precisar de tom, vocabulário, dados de contato ou identidade da empresa.
- Em fluxos compostos, antes das demais Skills.

## Quando NÃO usar
- Para armazenar dados sensíveis (tokens, senhas).
- Para informações que mudam em tempo real (preços, estoque).

## Entradas esperadas
| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-------------|-----------|
| `caminho_config` | string | sim | Caminho do YAML de configuração |
| `override` | dict | não | Sobreposições em runtime |

## Saídas esperadas
Dicionário de configuração validado, pronto para uso.

## Fluxo interno
1. Localizar `config/empresa.yaml`.
2. Carregar YAML.
3. Aplicar overrides de runtime (se houver).
4. Validar campos obrigatórios.
5. Expor configuração como variável de contexto.

## Boas práticas
- Nunca versionar dados sensíveis no repositório.
- Manter arquivo versionado apenas como `empresa.example.yaml`.
- Validar assinatura obrigatória ao carregar.

## Limitações
- Não acessa credenciais armazenadas em cofres.
- Não sincroniza em tempo real entre instâncias.

## Dependências
- Nenhuma

## Possíveis integrações
- Vault
- AWS Secrets Manager
- Variáveis de ambiente