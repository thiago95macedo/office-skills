#!/usr/bin/env python3
"""
Validador de fluxos executaveis em YAML.

Verifica:
- Cada arquivo docs/fluxos/*.yaml parseia contra flow.schema.json.
- Cada step referencia uma Skill existente.
- Campos input_from referenciam outputs de steps anteriores.
- inputs referenciados existem como outputs de steps anteriores.
"""

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERRO: PyYAML nao encontrado.", file=sys.stderr)
    sys.exit(1)

try:
    import jsonschema
except ImportError:
    print("ERRO: jsonschema nao encontrado.", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
FLOWS_DIR = ROOT / "docs" / "fluxos"
SKILLS_DIR = ROOT / "skills"
SCHEMA_PATH = ROOT / "assets" / "schemas" / "flow.schema.json"


def discover_skills() -> set[str]:
    found = set()
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        for skill_dir in category_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                found.add(f"{category_dir.name}/{skill_dir.name}")
    return found


def main() -> int:
    if not SCHEMA_PATH.exists():
        print(f"ERRO: schema {SCHEMA_PATH} nao encontrado.", file=sys.stderr)
        return 2

    with open(SCHEMA_PATH, encoding="utf-8") as f:
        validator_schema = json.load(f)

    if not FLOWS_DIR.exists():
        print(f"ERRO: pasta {FLOWS_DIR} nao encontrada.", file=sys.stderr)
        return 2

    flow_files = sorted(FLOWS_DIR.glob("*.yaml"))
    if not flow_files:
        print("AVISO: nenhum fluxo YAML encontrado em docs/fluxos/.")
        return 0

    skills = discover_skills()
    errors = []
    warnings = []

    for flow_file in flow_files:
        flow_name = flow_file.stem
        try:
            with open(flow_file, encoding="utf-8") as f:
                flow = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{flow_name}: YAML invalido - {str(e).splitlines()[0]}")
            continue

        try:
            jsonschema.validate(flow, validator_schema)
        except jsonschema.ValidationError as e:
            errors.append(f"{flow_name}: schema invalido - {e.message}")
            continue

        # Cada step deve referenciar Skill existente
        step_outputs = {}
        step_ids_in_order = [s["id"] for s in flow.get("steps", [])]
        for idx, step in enumerate(flow.get("steps", [])):
            sid = step.get("id", "?")
            skill_id = step.get("skill")
            if skill_id not in skills:
                errors.append(
                    f"{flow_name}.{sid}: referencia Skill inexistente: {skill_id}"
                )
            # input_from deve referenciar outputs anteriores ou inputs
            for dst, src in (step.get("input_from") or {}).items():
                if "." in src:
                    src_step, _ = src.split(".", 1)
                    if src_step == "inputs":
                        continue
                    # src_step pode ser um step_id direto, ou um nome
                    # de output (step_id_obj).
                    src_step_base = src_step
                    if src_step_base.endswith("_obj"):
                        src_step_base = src_step_base[:-4]
                    prior_steps = step_ids_in_order[:idx]
                    if src_step in prior_steps or src_step_base in prior_steps:
                        continue
                    warnings.append(
                        f"{flow_name}.{sid}: input_from {src} referencia step desconhecido"
                    )
            step_outputs[sid] = step.get("output", sid)

    print(f"Fluxos analisados: {len(flow_files)}")
    print(f"Skills conhecidas: {len(skills)}")
    print(f"Erros:             {len(errors)}")
    print(f"Avisos:            {len(warnings)}")
    print()

    if errors:
        print("=== ERROS ===")
        for e in errors:
            print(f"  - {e}")
        print()
        return 1

    if warnings:
        print("=== AVISOS ===")
        for w in warnings:
            print(f"  - {w}")
        print()

    print("OK: todos os fluxos parseiam e referenciam Skills validas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
