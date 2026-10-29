# Apex Ops API — Junior DevOps Assessment

## Setup and Run Steps
```bash
# 1. Copy environment variables
cp .env.example .env

# 2. Build and run the application and database
docker compose up -d --build

# 3. Verify the application is running
curl http://localhost:8000/health
curl http://localhost:8000/ready
Running Tests
To run the automated checks (including the one intentional failure), use a Python virtual environment:

bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
pytest app/tests/ -v
Architecture and Process Diagram
text
[ GitHub Actions CI ] --> [ Docker Image ] --> [ Docker Compose ]
                                                    |
                                          +---------+---------+
                                          |                   |
                                    [ FastAPI App ] <---> [ PostgreSQL ]
                                      (non-root)          (named volume)
Security and Configuration Hygiene
Secrets handling: .env is gitignored; .env.example is committed. No hard-coded secrets.

Least privilege: Container runs as non-root user (appuser); DB user is scoped.

Dependency/Image scanning: Dockerfile scanned via Hadolint (see evidence/trivy.png).

Metrics and Alert Proposal
Structured logs: Implemented (JSON format).

Health checks: Implemented (/health for liveness, /ready for DB readiness).

Metrics/Alert Proposal: Prometheus scrapes /metrics. Proposed alerts: error_rate > 5% for 5 minutes, and readiness_fail for > 1 minute.

Cost-Aware Cloud Path
Single small VM (e.g., Fly.io/Railway free tier) with a managed Postgres free tier. Scale horizontally only when needed.