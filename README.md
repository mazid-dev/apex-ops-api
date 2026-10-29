# Apex Ops API — Junior DevOps Assessment

## Setup
1. cp .env.example .env
2. docker compose up -d --build
3. curl http://localhost:8000/health

## Run tests
pip install -r app/requirements.txt && pytest app/tests/ -v

## Architecture
[app:FastAPI] --> [db:Postgres]   (compose, named volume pgdata)
CI builds versioned image --> compose deploy --> rollback by tag

## Security
- Secrets: .env gitignored; .env.example committed; CI uses GitHub Secrets
- Least privilege: non-root `appuser`; DB user scoped
- Scanning: trivy image apex-ops-api:latest

## Metrics/Alert proposal
Prometheus scrapes /metrics; alerts: error_rate>5% (5m), readiness_fail>1m.

## Cost-aware cloud path
Single small VM + managed Postgres free tier (Fly.io/Railway); scale later.

## Assumptions & trade-offs
- Local-only, synthetic data, no paid cloud
- Single-node compose; not production HA
- Rollback = previous image tag re-deploy