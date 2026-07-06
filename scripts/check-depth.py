#!/usr/bin/env python3
"""
Validador de profundidade minima das Skills.
Garante que cada Skill tem a estrutura e conteudo minimos exigidos.

Verifica por Skill:
- SKILL.md contem 12 secoes obrigatorias
- examples/ tem >= 3 arquivos com conteudo minimo
- tests/casos-de-teste.md tem >= 3 casos verificaveis
- templates/entrada.template.md e templates/saida.template.md existem
- schema.yaml existe
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
    "## Objetivo",
    "## Quando usar",
    "## Quando NÃO usar",
    "## Entradas esperadas",
    "## Saídas esperadas",
    "## Fluxo interno",
    "## Boas práticas",
    "## Limitações",
    "## Dependências",
    "## Exemplos de uso",
    "## Prompt interno recomendado",
    "## Possíveis integrações",
]

MIN_EXAMPLES = 3
MIN_EXAMPLE_CHARS = 100
MIN_TESTS = 3
MIN_TEMPLATE_CHARS = 20


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


def check_skill(skill_id: str, path: Path) -> list[str]:
    errors = []

    # 1. SKILL.md com 12 secoes
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_id}: SKILL.md ausente")
        return errors  # sem o resto, nao da pra checar
    content = skill_md.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_SKILL_SECTIONS if s not in content]
    if missing:
        errors.append(f"{skill_id}: SKILL.md sem secoes: {', '.join(missing)}")

    # 2. schema.yaml existe
    if not (path / "schema.yaml").exists():
        errors.append(f"{skill_id}: schema.yaml ausente")

    # 3. examples/ com >= 3 arquivos e conteudo minimo
    examples_dir = path / "examples"
    if not examples_dir.exists():
        errors.append(f"{skill_id}: pasta examples/ ausente")
    else:
        examples = [f for f in examples_dir.iterdir() if f.is_file()]
        if len(examples) < MIN_EXAMPLES:
            errors.append(
                f"{skill_id}: examples/ tem {len(examples)} arquivos "
                f"(minimo {MIN_EXAMPLES})"
            )
        else:
            for ex in examples:
                try:
                    size = ex.stat().st_size
                except OSError:
                    size = 0
                if size < MIN_EXAMPLE_CHARS:
                    errors.append(
                        f"{skill_id}: exemplo {ex.name} tem apenas {size} chars "
                        f"(minimo {MIN_EXAMPLE_CHARS})"
                    )

    # 4. tests/casos-de-teste.md com >= 3 casos verificaveis
    tests_file = path / "tests" / "casos-de-teste.md"
    if not tests_file.exists():
        errors.append(f"{skill_id}: tests/casos-de-teste.md ausente")
    else:
        test_content = tests_file.read_text(encoding="utf-8")
        # procurar padroes "## Caso N" ou "### Caso N"
        cases = re.findall(r"^##+\s+Caso\s+\d+", test_content, re.MULTILINE)
        if len(cases) < MIN_TESTS:
            errors.append(
                f"{skill_id}: casos-de-teste.md tem {len(cases)} casos "
                f"(minimo {MIN_TESTS})"
            )

    # 5. templates/entrada.template.md e templates/saida.template.md
    for tpl_name in ("entrada.template.md", "saida.template.md"):
        tpl = path / "templates" / tpl_name
        if not tpl.exists():
            errors.append(f"{skill_id}: templates/{tpl_name} ausente")
        else:
            try:
                size = tpl.stat().st_size
            except OSError:
                size = 0
            if size < MIN_TEMPLATE_CHARS:
                errors.append(
                    f"{skill_id}: templates/{tpl_name} tem {size} chars "
                    f"(minimo {MIN_TEMPLATE_CHARS})"
                )

    return errors


def main() -> int:
    skills = discover_skills()
    if not skills:
        print("ERRO: nenhuma Skill encontrada.", file=sys.stderr)
        return 2

    all_errors = []
    for skill_id, path in sorted(skills.items()):
        errs = check_skill(skill_id, path)
        all_errors.extend(errs)

    print(f"Skills analisadas: {len(skills)}")
    print(f"Erros encontrados: {len(all_errors)}")
    print()

    if all_errors:
        print("=== ERROS DE PROFUNDIDADE ===")
        for e in all_errors:
            print(f"  - {e}")
        print()
        print("FALHA: corrija os erros acima.")
        return 1

    print("OK: todas as Skills atendem profundidade minima.")
    return 0


if __name__ == "__main__":
    sys.exit(main())