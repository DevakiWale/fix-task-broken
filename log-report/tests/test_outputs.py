#!/usr/bin/env python3

import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")


def expected_report():
    """Compute the expected report from the input access log."""
    paths = Counter()
    ips = set()
    total = 0

    with LOG_PATH.open() as f:
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

    return {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": top_path,
        "top_path_count": top_count,
    }


def test_report_exists():
    """Success Criterion 1: The report file /app/report.json exists."""
    assert REPORT_PATH.exists(), "report.json was not created"


def test_report_schema():
    """Success Criterion 2: The report contains valid JSON with exactly the required fields."""
    with REPORT_PATH.open() as f:
        report = json.load(f)

    assert isinstance(report, dict)

    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
        "top_path_count",
    }


def test_report_values():
    """Success Criterion 3: The report values are correct according to the access log."""
    expected = expected_report()

    with REPORT_PATH.open() as f:
        actual = json.load(f)

    assert actual == expected