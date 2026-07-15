# Task: Log Report

You are given an Apache‑style access log file located at `/app/access.log`.  
Your job is to analyse the traffic and produce a JSON report with the following statistics:

- `total_requests`   – total number of HTTP requests (each log line is one request)
- `unique_ips`       – number of distinct client IP addresses
- `top_path`         – the URL path that was requested most often (e.g., `/index.html`)
- `top_path_count`   – how many times that top path was requested

Write your report to `/app/report.json`.

## Success Criteria

1. The report file `/app/report.json` exists.
2. The file contains valid JSON with exactly the four fields listed above.
3. The values in the report are numerically correct according to the access log.

The log is in the standard combined log format (e.g.  
`127.0.0.1 - - [01/Jan/2026:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`).  
You may use any tools available in the environment (Python, `awk`, `grep`, etc.).