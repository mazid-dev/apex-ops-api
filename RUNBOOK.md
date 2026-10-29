# RUNBOOK — Apex Ops API

## 1. Deploy
- cp .env.example .env   (edit local values only)
- TAG=v1.0.0 docker compose up -d --build
- curl http://localhost:8000/health   # {"status":"ok"}
- curl http://localhost:8000/ready    # {"status":"ready"}

## 2. Rollback
- TAG=v0.9.0 docker compose up -d
- curl http://localhost:8000/health
- Save output to evidence/rollback.log

## 3. Incident Response
1. Detect: readiness 503 or alert
2. Triage: docker compose ps; docker compose logs api
3. Mitigate: rollback to last good tag (section 2)
4. Communicate: log incident in evidence/
5. Postmortem: update DECISION_MEMO.md

## 4. Troubleshooting
- API not ready -> docker compose logs db (is DB up?)
- Port in use -> change ports in compose
- Build fails -> check Dockerfile base pin
- Secret missing -> verify .env exists (never commit)