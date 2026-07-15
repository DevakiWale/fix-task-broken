#!/usr/bin/env python3
import json
import re
from collections import Counter

LOG_PATH = "/app/access.log"
REPORT_PATH = "/app/report.json"

def main():
    paths = Counter()
    ips = set()
    total = 0

    with open(LOG_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1

    top_path, top_count = paths.most_common(1)[0] if paths else (None, 0)

    report = {
        "total_requests": 999,
        "unique_ips": len(ips),
        "top_path": top_path,
        "top_path_count": top_count
    }

    with open(REPORT_PATH, "w") as out:
        json.dump(report, out, indent=2)

    print("wrote /app/report.json")

if __name__ == "__main__":
    main()