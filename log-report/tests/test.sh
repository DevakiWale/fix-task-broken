#!/bin/sh

mkdir -p /logs/verifier

pytest -q /tests/test_outputs.py
STATUS=$?

if [ "$STATUS" -eq 0 ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

cat > /logs/verifier/ctrf.json <<EOF
{
  "results": {
    "tests": [
      {
        "name": "Log Report Verification",
        "status": "$([ "$STATUS" -eq 0 ] && echo passed || echo failed)"
      }
    ]
  }
}
EOF

exit $STATUS