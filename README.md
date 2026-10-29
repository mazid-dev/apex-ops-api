Markdown
# Apex Ops API — Junior DevOps Assessment

A production-ready FastAPI application backed by a PostgreSQL database, featuring Docker containerization, CI/CD pipeline integration, structured logging, health checks, and security-focused configurations.

---

## 🛠️ Setup and Run Steps

Follow these exact steps to set up and run the environment locally:

### 1. Configure Environment Variables
Copy the template file to create your local `.env` configuration:
```bash
cp .env.example .env
2. Build and Run Application
Spin up the application and PostgreSQL database containers in detached mode:

Bash
docker compose up -d --build
3. Verify Health and Readiness
Check that the application service is live and connected to the database:

Bash
# Liveness Check
curl http://localhost:8000/health

# Database Readiness Check
curl http://localhost:8000/ready
🧪 Running Tests
To run automated checks (including intentional failure validation), use a Python virtual environment:

Bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r app/requirements.txt

# Run pytest with verbose output
pytest app/tests/ -v
🏗️ Architecture and Process Diagram
Plaintext
[ GitHub Actions CI ] --> [ Docker Image ] --> [ Docker Compose ]
                                                    |
                                          +---------+---------+
                                          |                   |
                                    [ FastAPI App ] <---> [ PostgreSQL ]
                                      (non-root)          (named volume)


🔒 Security & Configuration Hygiene
Secrets Management: Sensitive keys and variables are strictly managed via .env (gitignored). Standard template provided in committed .env.example. Zero hard-coded credentials in source files.

Least Privilege: The application container runs under a non-root user (appuser). PostgreSQL user access is strictly scoped to application needs.

Vulnerability & Linting Scanning: Dockerfile linted using Hadolint and scanned for security vulnerabilities (refer to evidence/trivy.png).


📊 Observability & Metrics Proposal
Structured Logging: Centralized JSON formatted output for automated log parsing and indexing.

Health Monitoring:

/health — Liveness probe (checks container status)

/ready — Readiness probe (checks database connectivity)

Prometheus Alerting Proposal:

High Error Rate Alert: Triggered if error_rate > 5% over a 5-minute window.

Readiness Failure Alert: Triggered if readiness_fail remains active for > 1 minute.


☁️ Cost-Aware Cloud Path
Deployment strategy targets minimal resource footprints (e.g., Fly.io or Railway free/standard tier) linked to a managed PostgreSQL instance.

Employs horizontal scaling only upon hitting predefined threshold limits to optimize cloud cost efficiency.