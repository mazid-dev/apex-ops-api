# Apex Ops API — Junior DevOps Assessment

A production-ready FastAPI application backed by PostgreSQL, featuring Docker containerization, CI/CD integration, structured logging, health checks, and security-focused configurations.

## 🛠️ Setup and Run

### 1. Configure Environment Variables

Create your local environment configuration:

```bash
cp .env.example .env
```

### 2. Build and Start Services

Build the application image and start the application and PostgreSQL containers:

```bash
docker compose up -d --build
```

### 3. Verify Health and Readiness

Check application liveness:

```bash
curl http://localhost:8000/health
```

Check database connectivity:

```bash
curl http://localhost:8000/ready
```

## 🧪 Running Tests

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r app/requirements.txt
```

Run the test suite:

```bash
pytest app/tests/ -v
```

## 🏗️ Architecture

```text
              GitHub Actions CI
                      |
                      v
                Docker Image
                      |
                      v
                Docker Compose
                      |
             +--------+--------+
             |                 |
             v                 v
       FastAPI App <------> PostgreSQL
       (Non-root User)      (Named Volume)
```

## 🔒 Security and Configuration

- **Secrets Management:** Sensitive configuration is stored in a local `.env` file excluded from version control. An `.env.example` template provides the required configuration structure.
- **Least Privilege:** The application container runs as a non-root `appuser`, reducing unnecessary privileges.
- **Database Security:** PostgreSQL access is configured for application-specific requirements.
- **Security Scanning:** Dockerfile linting is performed with Hadolint, and vulnerability scanning evidence is provided in `evidence/trivy.png`.

## 📊 Observability and Monitoring

- **Structured Logging:** JSON-formatted logs support centralized collection, parsing, and analysis.
- **Liveness Probe:** `/health` verifies application health.
- **Readiness Probe:** `/ready` verifies database connectivity.
- **Prometheus Alerting Proposals:**
  - **High Error Rate:** Trigger an alert when the error rate exceeds 5% over a five-minute window.
  - **Readiness Failure:** Trigger an alert when readiness checks fail continuously for more than one minute.

## ☁️ Cost-Aware Cloud Deployment

The deployment strategy prioritizes minimal resource consumption through platforms such as Fly.io or Railway, combined with managed PostgreSQL where appropriate.

Horizontal scaling can be introduced when predefined resource utilization or performance thresholds are reached, helping balance application reliability and cloud costs.
