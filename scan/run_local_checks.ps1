# Author: chandu

$ErrorActionPreference = "Stop"

py -3.13 -m pip install -r requirements-dev.txt
py -3.13 -m pytest tests
py -3.13 -m bandit -r app -f json -o docs/bandit-report.json

Write-Output "Local AppSec checks completed."
