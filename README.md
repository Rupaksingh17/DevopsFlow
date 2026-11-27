# DevOpsFlow – Automated CI/CD Pipeline

A portfolio-ready DevOps project that packages a Python/Flask service as a Docker image and automates quality checks, container builds, and release publishing with GitHub Actions.

**Tech stack:** Python, Flask, Docker, GitHub Actions, Bash, Pytest, Ruff  
**Repository name:** `devopsflow-automated-cicd-pipeline`

## What it demonstrates

- A small HTTP service with liveness (`/health`) and readiness (`/ready`) probes.
- Automated linting and unit tests on pushes and pull requests.
- A Docker image build that runs only after quality checks pass.
- Tagged releases published to GitHub Container Registry (GHCR).
- A minimal, non-root production container with health checking.
- Local operations through Docker Compose and Bash helpers.

## Pipeline

```text
Pull request / push to main
        │
        ├── Ruff lint ──┐
        └── Pytest ─────┴──> Docker build

Push version tag (for example v1.0.0)
        └──> Build and publish ghcr.io/<owner>/<repo>:v1.0.0 and :latest
```

## Run locally

### With Python

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m app
```

Open `http://localhost:5000/`, or check `http://localhost:5000/health` and `http://localhost:5000/ready`.

### With Docker Compose

```bash
docker compose up --build
```

Copy `.env.example` to `.env` to change the host port or local version. Stop with `docker compose down`. Bash users can also run `scripts/run-local.sh` and `scripts/stop-local.sh`.

## Run quality checks

```bash
python -m pip install -r requirements-dev.txt
ruff check .
pytest
```

Or use `make check` / `scripts/check.sh` where available.

## CI and release

1. Create a GitHub repository named `devopsflow-automated-cicd-pipeline` and push this project to its `main` branch.
2. Open a pull request or push to `main`. GitHub Actions runs lint, tests, then builds the image.
3. Create and push a semantic version tag to publish a release image:

   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

4. The CD workflow publishes `ghcr.io/<lowercase-owner>/devopsflow-automated-cicd-pipeline:v1.0.0` and `:latest`. The workflow uses the repository-provided `GITHUB_TOKEN`; ensure Actions can write packages in repository settings. Package visibility may need to be changed to public in GitHub Packages settings if you want others to pull it anonymously.

Pull and run the published image:

```bash
docker pull ghcr.io/<lowercase-owner>/devopsflow-automated-cicd-pipeline:v1.0.0
docker run --rm -p 5000:5000 ghcr.io/<lowercase-owner>/devopsflow-automated-cicd-pipeline:v1.0.0
```

## API

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Service metadata and endpoint list |
| `GET` | `/health` | Liveness probe |
| `GET` | `/ready` | Readiness probe |

Unknown routes return a JSON 404 response.

## Suggested next improvements

- Add coverage reporting and a minimum coverage threshold.
- Add dependency and container vulnerability scanning.
- Deploy the published image to a cloud platform with protected environments and approval gates.
- Add infrastructure as code (for example Terraform) and a staging-to-production promotion flow.

## Resume entry

**DevOpsFlow – Automated CI/CD Pipeline** | Python, Flask, Docker, GitHub Actions, Bash, Pytest  
Built a containerized Flask service and automated linting, tests, Docker image builds, and versioned GHCR releases using GitHub Actions; added health probes, Docker Compose local operations, and non-root container execution.
