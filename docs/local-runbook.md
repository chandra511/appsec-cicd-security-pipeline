# Local Runbook

Author: chandu

## Run the app locally

```powershell
cd appsec-cicd-demo
py -3.13 -m pip install -r app\requirements.txt
py -3.13 app\sample_app.py
```

Open:

- `http://localhost:5000/`
- `http://localhost:5000/health`
- `http://localhost:5000/api/profile/chandu_security`

## Run tests

```powershell
py -3.13 -m pytest tests
```

## Run Bandit

```powershell
py -3.13 -m pip install -r requirements-dev.txt
py -3.13 -m bandit -r app -f json -o docs\bandit-report.json
```

## Run Docker

```powershell
docker compose up --build
```

Docker sets `APP_HOST=0.0.0.0` so the container port can be reached from the host. Local Python runs bind to `127.0.0.1` by default.
