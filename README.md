# Fix Terminal-Bench 2 (Harbor) Task

This repository contains my solution for the **Project Dynamo – Fix the Broken Terminal-Bench 2 (Harbor) Task** assessment.

## Overview

The original Harbor task contained several authoring issues related to task configuration, environment reproducibility, verifier implementation, and task instructions. The task was repaired to follow the Terminal-Bench 2 (Harbor) specification and verified using the Harbor runner.

## Issues Fixed

- Corrected `task.toml` structure and metadata.
- Updated the artifact declaration to match the generated output.
- Rewrote `instruction.md` with clear and verifiable success criteria.
- Fixed the Docker environment to remove leaked solution files and improve reproducibility.
- Replaced the weak verifier with a verifier that validates the actual report contents.
- Added proper generation of:
  - `/logs/verifier/reward.txt`
  - `/logs/verifier/ctrf.json`
- Ensured the verifier fails for incorrect solutions and succeeds only for valid output.

## Project Structure

```
log-report/
├── environment/
│   └── Dockerfile
├── solution/
│   └── solve.py
├── tests/
│   ├── test_outputs.py
│   └── test.sh
├── instruction.md
├── task.toml
└── access.log
```

## Running the Task

### Oracle

```bash
harbor run -p . -a oracle
```

Expected result:

- Reward: **1**

### No-op Agent

```bash
harbor run -p . --agent nop
```

Expected result:

- Reward: **0**

## Verification

The verifier independently parses `access.log`, computes the expected statistics, and compares them with the generated `report.json`.

The following fields are validated:

- `total_requests`
- `unique_ips`
- `top_path`
- `top_path_count`

The verifier writes:

```
/logs/verifier/reward.txt
/logs/verifier/ctrf.json
```

## Technologies

- Python 3.11
- Docker
- Harbor (Terminal-Bench 2)
- Pytest

## Author

**Devaki Wale**

GitHub: https://github.com/DevakiWale
