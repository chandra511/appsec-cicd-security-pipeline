# AppSec CI/CD Security Pipeline

Author: chandra

## Project overview

This project demonstrates how to add application security checks into a CI/CD workflow. It includes a small Flask app, secure headers, input validation, unit tests, Bandit SAST scanning, OWASP ZAP DAST configuration, vulnerability notes, and remediation documentation.

## Why this project matters 

Application Security and DevSecOps roles pay well when the candidate can connect vulnerabilities to engineering workflows. This project shows a person can find issues, explain risk, and place checks inside a pipeline instead of doing one-time manual testing only.

## Skills demonstrated

- Secure Flask baseline
- Security headers
- Input validation
- Automated unit tests
- SAST with Bandit
- DAST planning with OWASP ZAP
- GitHub Actions security workflow
- Vulnerability documentation and remediation notes
- Docker-based local deployment

## Tools used

- Python Flask
- Pytest
- GitHub Actions
- Bandit
- OWASP ZAP
- Docker

## Repo structure

- `app/` - sample application code
- `tests/` - automated application and security-header tests
- `.github/workflows/` - CI workflow
- `scan/` - scan scripts and ZAP rule configuration
- `docs/` - vulnerability, remediation, threat-model, and runbook notes
- `Dockerfile` - local container image
- `docker-compose.yml` - local compose setup
- `requirements-dev.txt` - local test and security-scan dependencies

## How to use

1. Create a Python virtual environment.
2. Install dependencies from `app/requirements.txt` or `requirements-dev.txt`.
3. Run the app with `py -3.13 app/sample_app.py`.
4. Run tests with `py -3.13 -m pytest tests`.
5. Run SAST with `bash scan/bandit_scan.sh` or `scan/run_local_checks.ps1`.
6. Review findings in `docs/vulnerability-report.md`.

## Safety note

Use OWASP ZAP only against applications you own or have written authorization to test.
