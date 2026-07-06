#!/usr/bin/env bash
# Office Skills - Validador consolidado
# Executa todos os checks de qualidade da biblioteca.

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT"

echo "======================================"
echo "  Office Skills - Validacao Completa"
echo "======================================"
echo

PASS=0
FAIL=0

# 1. Estrutura minima por Skill
echo "--- 1. Estrutura minima das Skills ---"
total=0
ok=0
fail_list=""
for d in skills/*/*/; do
    [ -d "$d" ] || continue
    total=$((total + 1))
    skill_ok=1
    for f in SKILL.md README.md prompt.md schema.yaml; do
        if [ ! -e "${d}${f}" ]; then
            fail_list="${fail_list}  - ${d}${f} ausente"$'\n'
            skill_ok=0
        fi
    done
    for f in examples templates tests; do
        if [ ! -d "${d}${f}" ]; then
            fail_list="${fail_list}  - ${d}${f}/ ausente"$'\n'
            skill_ok=0
        fi
    done
    if [ $skill_ok -eq 1 ]; then ok=$((ok + 1)); fi
done
if [ "$ok" -eq "$total" ]; then
    echo "  [OK] Estrutura: $ok/$total Skills"
    PASS=$((PASS + 1))
else
    echo "  [FALHA] Estrutura: $ok/$total Skills"
    printf "%b" "$fail_list"
    FAIL=$((FAIL + 1))
fi
echo

# 2. Schemas de contrato
echo "--- 2. Schemas de contrato (schema.yaml) ---"
if python3 scripts/validate-contracts.py; then
    PASS=$((PASS + 1))
else
    FAIL=$((FAIL + 1))
fi
echo

# 3. Profundidade minima
echo "--- 3. Profundidade minima ---"
if python3 scripts/check-depth.py; then
    PASS=$((PASS + 1))
else
    FAIL=$((FAIL + 1))
fi
echo

# 4. Fluxos executaveis
echo "--- 4. Fluxos executaveis ---"
if python3 scripts/validate-flows.py; then
    PASS=$((PASS + 1))
else
    FAIL=$((FAIL + 1))
fi
echo "======================================"
echo "  Resultado: $PASS OK / $FAIL falhas"
echo "======================================"

exit $FAIL
