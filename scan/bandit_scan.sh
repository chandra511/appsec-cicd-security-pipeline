#!/usr/bin/env bash

# Author: chandu

set -e

bandit -r app -f json -o docs/bandit-report.json

echo "Bandit report generated at docs/bandit-report.json"
