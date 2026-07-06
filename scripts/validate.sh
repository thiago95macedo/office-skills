#!/usr/bin/env bash
# Validador da biblioteca Office Skills
# Verifica estrutura padrao de cada Skill e frontmatter minimo.

set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"

ok=0
falhas=0

echo "Office Skills - Validador"
echo "Diretorio raiz: $ROOT"
echo

required_files=("SKILL.md" "README.md" "prompt.md" "examples" "templates" "tests")
required_dirs=("examples" "templates" "tests")

validar_skill() {
  local dir="$1"
  local skill_name
  skill_name=$(basename "$dir")
  local skill_ok=1

  for f in "${required_files[@]}"; do
    if [[ ! -e "$dir/$f" ]]; then
      echo "[FALTA] $skill_name: $f"
      skill_ok=0
      ((falhas++))
    fi
  done

  if [[ -f "$dir/SKILL.md" ]]; then
    if ! grep -q "^name:" "$dir/SKILL.md"; then
      echo "[FRONTMATTER] $skill_name: faltando campo 'name'"
      skill_ok=0
      ((falhas++))
    fi
    if ! grep -q "^description:" "$dir/SKILL.md"; then
      echo "[FRONTMATTER] $skill_name: faltando campo 'description'"
      skill_ok=0
      ((falhas++))
    fi
    if ! grep -q "^category:" "$dir/SKILL.md"; then
      echo "[FRONTMATTER] $skill_name: faltando campo 'category'"
      skill_ok=0
      ((falhas++))
    fi
    if ! grep -q "^version:" "$dir/SKILL.md"; then
      echo "[FRONTMATTER] $skill_name: faltando campo 'version'"
      skill_ok=0
      ((falhas++))
    fi
  fi

  if [[ $skill_ok -eq 1 ]]; then
    echo "[OK]      $skill_name"
    ((ok++))
  fi
}

shopt -s nullglob
for categoria in "$SKILLS_DIR"/*; do
  if [[ -d "$categoria" ]]; then
    for skill_dir in "$categoria"/*; do
      if [[ -d "$skill_dir" ]]; then
        validar_skill "$skill_dir"
      fi
    done
  fi
done

echo
echo "Resultado: $ok OK / $falhas falhas"
exit $falhas