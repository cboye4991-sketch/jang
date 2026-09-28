#!/usr/bin/env bash
# Jàng — test de l'API Dify sans MVP (S5)
# Usage :
#   export DIFY_API_KEY="app-xxxxxxxx"      # clé du workflow Jang_Correcteur_v1 — ne jamais la committer
#   bash dify/webhook/test-api.sh                  # lance T1
#   bash dify/webhook/test-api.sh "JNG-PC-07 : a = g cos 30 = 8,5 m/s²"
set -euo pipefail

if [ -z "${DIFY_API_KEY:-}" ]; then
  echo "Définis d'abord la clé : export DIFY_API_KEY=app-..." >&2
  exit 1
fi

QUERY="${1:-JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L}"

# Corps JSON construit par Python (gère accents, guillemets et retours à la ligne)
BODY=$(QUERY="$QUERY" python3 -c '
import json, os, time
print(json.dumps({"inputs": {"query": os.environ["QUERY"]},
                  "response_mode": "blocking",
                  "user": "jang-test-%d" % time.time()}))
')

curl -sS --max-time 30 -X POST "https://api.dify.ai/v1/workflows/run" \
  -H "Authorization: Bearer ${DIFY_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$BODY" \
| python3 -c '
import json, sys
raw = sys.stdin.read()
try:
    r = json.loads(raw)
except ValueError:
    print("ÉCHEC : pas de réponse JSON de Dify (réseau ?)", raw[:300]); sys.exit(1)
d = r.get("data", {})
if d.get("status") != "succeeded":
    print("ÉCHEC :", json.dumps(r, ensure_ascii=False, indent=2)); sys.exit(1)
print(d["outputs"].get("answer", d["outputs"]))
print("\n— durée : %.1f s · tokens : %s" % (d.get("elapsed_time", 0), d.get("total_tokens")))
'
