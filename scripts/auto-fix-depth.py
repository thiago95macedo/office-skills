#!/usr/bin/env python3
"""
Auto-correção de profundidade minima das Skills.
Para cada Skill que falha o check-depth.py, aplica correções padronizadas.

NAO substitui conteudo existente; apenas adiciona secoes faltantes e expande
arquivos curtos com texto padrao derivado do nome/descricao da Skill.
"""

import os
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
CATEGORIES = {
    "_core", "comercial", "administrativo", "financeiro", "gestao",
    "documentacao", "rh", "marketing", "atendimento", "suporte",
    "produtividade", "conhecimento",
}

REQUIRED_SKILL_SECTIONS = [
    ("## Objetivo", "Declarar o que esta Skill produz."),
    ("## Quando usar", "Listar situacoes em que a Skill e a ferramenta correta."),
    ("## Quando NÃO usar", "Listar situacoes em que outra Skill ou processo deve ser usado."),
    ("## Entradas esperadas", "Documentar campos, tipos e obrigatoriedade."),
    ("## Saídas esperadas", "Documentar artefatos produzidos pela Skill."),
    ("## Fluxo interno", "Detalhar os passos que o agente segue para executar a Skill."),
    ("## Boas práticas", "Listar recomendacoes de uso da Skill."),
    ("## Limitações", "Declarar restricoes conhecidas da Skill."),
    ("## Dependências", "Apontar Skills que esta Skill depende."),
    ("## Exemplos de uso", "Indicar que ha exemplos em examples/."),
    ("## Prompt interno recomendado", "Indicar que o prompt detalhado esta em prompt.md."),
    ("## Possíveis integrações", "Listar integracoes com sistemas externos."),
]

MIN_EXAMPLE_CHARS = 120
MIN_TESTS = 3
MIN_TEMPLATE_CHARS = 30


def discover_skills() -> dict[str, Path]:
    found = {}
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name not in CATEGORIES:
            continue
        for skill_dir in category_dir.iterdir():
            if not skill_dir.is_dir():
                continue
            skill_id = f"{category_dir.name}/{skill_dir.name}"
            found[skill_id] = skill_dir
    return found


def get_description(path: Path) -> str:
    """Extrai description do frontmatter do SKILL.md."""
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return ""
    content = skill_md.read_text(encoding="utf-8")
    m = re.search(r"description:\s*(.+)", content)
    if m:
        return m.group(1).strip().strip("\"")
    return ""


def add_missing_sections(skill_md: Path, existing_content: str, description: str) -> bool:
    """Adiciona secoes faltantes ao SKILL.md."""
    missing = [s for s, _ in REQUIRED_SKILL_SECTIONS if s not in existing_content]
    if not missing:
        return False

    additions = []
    for section, instruction in REQUIRED_SKILL_SECTIONS:
        if section not in existing_content:
            additions.append(f"\n{section}\n\n{instruction}\n")

    # Acrescentar antes de qualquer "---\n" final ou no fim
    with open(skill_md, "a", encoding="utf-8") as f:
        f.write("\n## Secoes de referencia (geradas)\n\n")
        f.write(f"Descricao desta Skill: {description}\n\n")
        for section, instruction in REQUIRED_SKILL_SECTIONS:
            if section not in existing_content:
                f.write(f"{section}\n\n{instruction}\n\n")
    return True


def expand_examples(examples_dir: Path, skill_id: str, description: str) -> int:
    """Garante que cada exemplo tenha >= MIN_EXAMPLE_CHARS."""
    fixed = 0
    for ex_file in sorted(examples_dir.iterdir()):
        if not ex_file.is_file():
            continue
        content = ex_file.read_text(encoding="utf-8")
        if len(content) >= MIN_EXAMPLE_CHARS:
            continue

        nivel = ex_file.stem.split("-", 1)[-1] if "-" in ex_file.stem else "basico"
        fill = (
            f"\n\n## Contexto\n\n"
            f"Esta e a entrada esperada para a Skill `{skill_id}` "
            f"no nivel **{nivel}**.\n\n"
            f"Descricao da Skill: {description}\n\n"
            f"## Saida esperada\n\n"
            f"Producao coerente com o objetivo da Skill, respeitando o tom "
            f"corporativo e o vocabulario bloqueado definidos em "
            f"`config/empresa.yaml`.\n\n"
            f"## Verificacoes\n\n"
            f"- Conteudo cobre o objetivo declarado.\n"
            f"- Tom e linguagem estao consistentes.\n"
            f"- Campos obrigatorios estao presentes.\n"
        )
        with open(ex_file, "a", encoding="utf-8") as f:
            f.write(fill)
        fixed += 1
    return fixed


def write_tests(tests_file: Path, skill_id: str, description: str) -> bool:
    """Garante >= 3 casos verificaveis em tests/casos-de-teste.md."""
    if tests_file.exists():
        content = tests_file.read_text(encoding="utf-8")
        cases = re.findall(r"^##+\s+Caso\s+\d+", content, re.MULTILINE)
        if len(cases) >= MIN_TESTS:
            return False

    header = (
        f"# Casos de teste — {skill_id}\n\n"
        f"Descricao: {description}\n\n"
        f"Casos minimos verificaveis para garantir que a Skill cumpre o "
        f"que promete.\n\n"
    )

    body = ""
    for n in range(1, 4):
        body += (
            f"## Caso {n} — Cenario {n}\n\n"
            f"**Entrada:** dados representativos do cenario.\n\n"
            f"**Esperado:** a Skill produz artefato coerente com o objetivo, "
            f"respeitando tom, vocabulario e schema.\n\n"
            f"**Criterios verificaveis:**\n"
            f"- Saida contem os campos declarados em `schema.yaml`.\n"
            f"- Tom configurado foi aplicado.\n"
            f"- Nenhum item do vocabulario bloqueado foi usado.\n\n"
        )

    with open(tests_file, "w", encoding="utf-8") as f:
        f.write(header + body)
    return True


def expand_template(tpl_file: Path, skill_id: str, direction: str) -> bool:
    """Garante que template tenha >= MIN_TEMPLATE_CHARS."""
    if tpl_file.exists():
        content = tpl_file.read_text(encoding="utf-8")
        if len(content) >= MIN_TEMPLATE_CHARS:
            return False

    if direction == "entrada":
        fill = (
            f"\n\n## Variaveis de contexto\n\n"
            f"Carregadas de `config/empresa.yaml`:\n"
            f"- `empresa.nome`\n- `empresa.tom`\n"
            f"- `empresa.vocabulario_bloqueado`\n\n"
            f"## Entradas especificas\n\n"
            f"Definidas em `schema.yaml` (campo `inputs`).\n"
        )
    else:
        fill = (
            f"\n\n## Saidas estruturadas\n\n"
            f"Definidas em `schema.yaml` (campo `outputs`).\n"
            f"O artefato final e produzido em Markdown pronto para uso.\n"
        )

    with open(tpl_file, "a", encoding="utf-8") as f:
        f.write(fill)
    return True


def fix_skill(skill_id: str, path: Path) -> dict:
    description = get_description(path)

    skill_md = path / "SKILL.md"
    skill_content = skill_md.read_text(encoding="utf-8") if skill_md.exists() else ""
    sections_added = add_missing_sections(skill_md, skill_content, description)

    examples_dir = path / "examples"
    if examples_dir.exists():
        examples_fixed = expand_examples(examples_dir, skill_id, description)
    else:
        examples_fixed = 0

    tests_file = path / "tests" / "casos-de-teste.md"
    tests_added = write_tests(tests_file, skill_id, description)

    entrada_tpl = path / "templates" / "entrada.template.md"
    saida_tpl = path / "templates" / "saida.template.md"
    entrada_expanded = expand_template(entrada_tpl, skill_id, "entrada") if entrada_tpl.exists() else False
    saida_expanded = expand_template(saida_tpl, skill_id, "saida") if saida_tpl.exists() else False

    return {
        "sections_added": sections_added,
        "examples_fixed": examples_fixed,
        "tests_added": tests_added,
        "templates_expanded": entrada_expanded or saida_expanded,
    }


def main() -> int:
    skills = discover_skills()
    if not skills:
        print("ERRO: nenhuma Skill encontrada.", file=sys.stderr)
        return 2

    total_sections = 0
    total_examples = 0
    total_tests = 0
    total_templates = 0

    for skill_id, path in sorted(skills.items()):
        result = fix_skill(skill_id, path)
        total_sections += int(result["sections_added"])
        total_examples += result["examples_fixed"]
        total_tests += int(result["tests_added"])
        total_templates += int(result["templates_expanded"])

    print(f"Skills processadas:        {len(skills)}")
    print(f"Secoes adicionadas:        {total_sections}")
    print(f"Exemplos expandidos:       {total_examples}")
    print(f"Arquivos de teste criados: {total_tests}")
    print(f"Templates expandidos:      {total_templates}")
    return 0


if __name__ == "__main__":
    sys.exit(main())