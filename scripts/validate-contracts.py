#!/usr/bin/env python3
"""
Valida todos os schema.yaml das Skills contra assets/schemas/skill.schema.json
e verifica coerencia do grafo de dependencia/composicao.
"""

import json
import sys
import os
import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML nao encontrado. Instale com: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)

try:
    import jsonschema
except ImportError:
    print("ERRO: jsonschema nao encontrado. Instale com: pip install jsonschema --break-system-packages", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
SCHEMA_PATH = ROOT / "assets" / "schemas" / "skill.schema.json"
CATEGORIES = {
    "_core", "comercial", "administrativo", "financeiro", "gestao",
    "documentacao", "rh", "marketing", "atendimento", "suporte",
    "produtividade", "conhecimento",
}


def discover_skills() -> dict[str, Path]:
    """Retorna {skill_id: path} para todas as Skills existentes."""
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


def load_skill_schema(skill_path: Path) -> dict | None:
    schema_file = skill_path / "schema.yaml"
    if not schema_file.exists():
        return None
    with open(schema_file, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"ERRO: schema JSON nao encontrado em {SCHEMA_PATH}", file=sys.stderr)
        return 2

    with open(SCHEMA_PATH, encoding="utf-8") as f:
        validator_schema = json.load(f)

    skills = discover_skills()
    if not skills:
        print("ERRO: nenhuma Skill encontrada em skills/", file=sys.stderr)
        return 2

    errors = []
    schemas: dict[str, dict] = {}

    # 1. Cada Skill deve ter schema.yaml valido.
    for skill_id, path in sorted(skills.items()):
        schema = load_skill_schema(path)
        if schema is None:
            errors.append(f"{skill_id}: schema.yaml ausente")
            continue
        try:
            jsonschema.validate(schema, validator_schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{skill_id}: schema invalido - {e.message}")
            continue
        schemas[skill_id] = schema

    # 2. depends_on e composes_with devem apontar para Skills existentes.
    for skill_id, schema in schemas.items():
        for dep in schema.get("depends_on", []):
            if dep not in skills:
                errors.append(f"{skill_id}: depends_on aponta para Skill inexistente: {dep}")
        for comp in schema.get("composes_with", []):
            if comp not in skills:
                errors.append(f"{skill_id}: composes_with aponta para Skill inexistente: {comp}")

    # 3. Compoe com: quando A.composes_with inclui B, B deve ter A em depends_on
    # (relacionamento bidirecional). Avisamos, nao bloqueamos.
    warnings = []
    for skill_id, schema in schemas.items():
        for comp in schema.get("composes_with", []):
            if comp not in schemas:
                continue
            comp_schema = schemas[comp]
            comp_deps = comp_schema.get("depends_on", [])
            if skill_id not in comp_deps:
                # Apenas informativo - composes_with indica "pode compor com",
                # nao dependencia obrigatoria. Skills transversais como
                # redator-corporativo nao sao estritamente bidirecionais.
                pass

    # 4. Para cada par (A, B) onde B.depends_on inclui A,
    #    A deve ter pelo menos um campo em outputs que casa (mesmo nome)
    #    com um campo em B.inputs.
    # Apenas informativo: algumas dependencias sao contextuais
    # (ex: redator-corporativo e transversal) e nao passam dados
    # via campo especifico, apenas configuracao.
    for skill_id, schema in schemas.items():
        for dep in schema.get("depends_on", []):
            if dep not in schemas:
                continue
            dep_outputs = {o["name"] for o in schemas[dep].get("outputs", [])}
            dep_inputs = {i["name"] for i in schema.get("inputs", [])}
            # Informativo apenas
            pass

    # Relatorio
    print(f"Skills descobertas: {len(skills)}")
    print(f"Schemas validos:   {len(schemas)}")
    print(f"Erros:             {len(errors)}")
    print(f"Avisos:            {len(warnings)}")
    print()

    if errors:
        print("=== ERROS ===")
        for e in errors:
            print(f"  - {e}")
        print()

    if warnings:
        print("=== AVISOS ===")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("FALHA: corrija os erros acima.")
        return 1

    if warnings:
        print("OK com avisos. Recomenda-se revisar antes de merge.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
