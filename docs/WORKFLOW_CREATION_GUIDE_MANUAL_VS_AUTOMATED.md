# Creating CI/CD Pipelines: Step-by-Step Developer Evolution vs. Automated Scaffolding

> **Author**: TeachCloud DevOps & Cloud Architecture Team  
> **Target Audience**: Software Engineers, DevOps Beginners, CI/CD Architects  
> **Interactive Simulator**: [`/cicd`](http://127.0.0.1:5000/cicd)  
> **Last Updated**: October 2026

---

## Table of Contents
1. [The Core Dilemma: Option A vs. Option B](#1-the-core-dilemma-option-a-vs-option-b)
2. [Why GitHub Actions Requires `.github/workflows/`](#2-why-github-actions-requires-githubworkflows)
3. [Approach A: The Human Engineer Way (Step-by-Step Progressive Evolution)](#3-approach-a-the-human-engineer-way-step-by-step-progressive-evolution)
   - [Phase 0: Initializing the Workflow Directory](#phase-0-initializing-the-workflow-directory)
   - [Level 0: First Ephemeral Runner Sanity Check](#level-0-first-ephemeral-runner-sanity-check)
   - [Level 1: Automated Quality Gates & Pytest](#level-1-automated-quality-gates--pytest)
   - [Level 2: Speed Optimization & Dependency Caching](#level-2-speed-optimization--dependency-caching)
   - [Level 3: Security Scans, SAST & Keyless OIDC](#level-3-security-scans-sast--keyless-oidc)
   - [Level 4: Multi-Stage Docker Builds & GHCR Publishing](#level-4-multi-stage-docker-builds--ghcr-publishing)
   - [Level 5: Zero-Downtime Blue/Green GitOps Rollouts](#level-5-zero-downtime-bluegreen-gitops-rollouts)
4. [Approach B: The Automated Scaffolding Way (1-Command Enterprise Generator)](#4-approach-b-the-automated-scaffolding-way-1-command-enterprise-generator)
   - [The 1-Command Terminal Scaffolder](#the-1-command-terminal-scaffolder)
   - [When Automation is Appropriate vs. Dangerous](#when-automation-is-appropriate-vs-dangerous)
5. [Comparative Analysis Matrix: Human Learning vs. AI Generation](#5-comparative-analysis-matrix-human-learning-vs-ai-generation)
6. [Common Pitfalls When Creating `.github` Workflows](#6-common-pitfalls-when-creating-github-workflows)
7. [Summary & Educational Recommendation](#7-summary--educational-recommendation)

---

## 1. The Core Dilemma: Option A vs. Option B

When engineers set out to build or learn CI/CD pipelines, they invariably face a choice:

```
┌──────────────────────────────────────────────┐
│                  Option A                    │
│        The Human Developer Journey           │
│  • Level-by-level progressive building       │
│  • Manually creating each file               │
│  • Understanding every trigger & exit code   │
│  • True muscle memory and confidence         │
└──────────────────────┬───────────────────────┘
                       │
             VS.       ▼
┌──────────────────────────────────────────────┐
│                  Option B                    │
│      The Automated AI / Script Scaffolder    │
│  • 1-command generator dumps all 6 files     │
│  • Instant enterprise directory tree         │
│  • Fast, but feels like an "AI black box"    │
│  • Hard to debug when something breaks       │
└──────────────────────────────────────────────┘
```

### Why Option A is Superior for Learning:
In real software development teams, **no company starts at Level 5 (GitOps Blue/Green Rollouts) on Day 1**. Every successful engineering team begins with **Level 0** (a simple sanity check), verifies that GitHub allocates a clean Linux runner, and then incrementally adds linting, testing, security, containerization, and deployment.

---

## 2. Why GitHub Actions Requires `.github/workflows/`

GitHub's automation engine is hardcoded to look for a specific directory structure at the root of your Git repository:

```text
my-project/
├── .github/
│   └── workflows/
│       ├── level0_first_ci.yml
│       ├── level1_quality_gates.yml
│       ├── level2_caching_artifacts.yml
│       ├── level3_security_oidc.yml
│       ├── level4_docker_ghcr.yml
│       └── level5_blue_green_gitops.yml
├── cloud_app/
├── tests/
├── requirements.txt
└── README.md
```

### Key Rules GitHub Enforces:
1. **The Leading Dot (`.`)**: In POSIX/Linux systems, names starting with a dot are hidden directories. GitHub reserves `.github` for repository configuration (workflows, issue templates, PR templates, code owners).
2. **The Exact Folder Name `workflows`**: Workflows must reside directly inside `.github/workflows/`. Subdirectories inside `workflows/` (e.g., `.github/workflows/ci/`) are **ignored** by GitHub Actions.
3. **File Extensions**: Files must end in either `.yml` or `.yaml`.
4. **Independent Execution**: Every `.yml` file inside `workflows/` is treated by GitHub as an independent pipeline and will show up with its own name in the **Actions** tab.

---

## 3. Approach A: The Human Engineer Way (Step-by-Step Progressive Evolution)

### Phase 0: Initializing the Workflow Directory
In your terminal at the root of your project:

```bash
# 1. Create the hidden directory structure (-p ensures parent directories are created)
mkdir -p .github/workflows

# 2. Verify the directory exists
ls -la .github/
# Output: drwxr-xr-x  3 user user  workflows
```

---

### Level 0: First Ephemeral Runner Sanity Check
**Goal**: Verify that GitHub Actions successfully provisions an Ubuntu VM, checks out your code, and prints runner diagnostics.

```bash
# 1. Create the Level 0 file
touch .github/workflows/level0_first_ci.yml
```

**Content for `.github/workflows/level0_first_ci.yml`:**
```yaml
name: "Level 0: First CI Sanity Check"

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  runner-diagnostic:
    runs-on: ubuntu-latest
    timeout-minutes: 5

    steps:
      - name: 1. Checkout Repository
        uses: actions/checkout@v4

      - name: 2. Inspect Ephemeral Environment
        run: |
          echo "=== RUNNER DIAGNOSTIC ==="
          echo "Hostname: $(hostname)"
          echo "Kernel:   $(uname -r)"
          echo "OS:       $(cat /etc/os-release | grep PRETTY_NAME)"
          echo "Python:   $(python3 --version)"
          echo "Git Ref:  ${{ github.ref }}"
          echo "Commit:   ${{ github.sha }}"
```

**Git Commit & Verification:**
```bash
git add .github/workflows/level0_first_ci.yml
git commit -m "ci: add Level 0 ephemeral runner sanity check"
git push origin main
```
*Go to GitHub.com → click **Actions** tab → watch the pipeline turn **Green ✅**!*

---

### Level 1: Automated Quality Gates & Pytest
**Goal**: Block broken code from merging. Run Black/Flake8 linters and execute Pytest with exit code evaluation.

```bash
# 1. Create Level 1 file
touch .github/workflows/level1_quality_gates.yml
```

**Content for `.github/workflows/level1_quality_gates.yml`:**
```yaml
name: "Level 1: Automated Quality Gates"

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  test-and-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.12
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Linting & Test Tools
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest pytest-cov
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Code Style Gate (Flake8)
        run: |
          # Stop build if syntax errors exist
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

      - name: Automated Unit Tests (Pytest)
        run: |
          pytest --tb=short -v
```

---

### Level 2: Speed Optimization & Dependency Caching
**Goal**: Cut pipeline build time from 3 minutes to 25 seconds using `actions/cache` and artifact archiving.

```bash
touch .github/workflows/level2_caching_artifacts.yml
```

**Key Directives Learned**:
- `uses: actions/cache@v4`: Hashes `requirements.txt` to restore pip wheels across runs.
- `uses: actions/upload-artifact@v4`: Saves `coverage.html` or JUnit XML reports for download.

---

### Level 3: Security Scans, SAST & Keyless OIDC
**Goal**: Zero hardcoded credentials. Connect to AWS/GCP using OpenID Connect (OIDC) and scan for CVEs with Trivy and Bandit.

```bash
touch .github/workflows/level3_security_oidc.yml
```

**Key Directives Learned**:
- `permissions: id-token: write`: Ephemeral cryptographic token for cloud authentication.
- `uses: aquasecurity/trivy-action`: Automated container and dependency vulnerability gate.

---

### Level 4: Multi-Stage Docker Builds & GHCR Publishing
**Goal**: Build an optimized container image, push to GitHub Container Registry (`ghcr.io`), and sign it cryptographically with Cosign.

```bash
touch .github/workflows/level4_docker_ghcr.yml
```

**Key Directives Learned**:
- `uses: docker/build-push-action@v5` with Buildx cache.
- `uses: sigstore/cosign-installer`: Supply chain security verification.

---

### Level 5: Zero-Downtime Blue/Green GitOps Rollouts
**Goal**: Deploy new code to an isolated "Green" environment, perform automated HTTP health probes, and shift live production traffic with zero downtime.

```bash
touch .github/workflows/level5_blue_green_gitops.yml
```

**Key Directives Learned**:
- `environment: production`: Enforces manual approval protection rules.
- Automated rollback on exit code `!= 0`.

---

## 4. Approach B: The Automated Scaffolding Way (1-Command Enterprise Generator)

In enterprise teams, when a platform engineer creates a new repository template or provisions 20 microservices, they don't manually type `touch` 6 times. They use a **generator script**.

### The 1-Command Terminal Scaffolder
Developers can run this single bash snippet from the root of their repository to scaffold all 6 levels instantly:

```bash
mkdir -p .github/workflows && \
touch .github/workflows/level0_first_ci.yml \
      .github/workflows/level1_quality_gates.yml \
      .github/workflows/level2_caching_artifacts.yml \
      .github/workflows/level3_security_oidc.yml \
      .github/workflows/level4_docker_ghcr.yml \
      .github/workflows/level5_blue_green_gitops.yml && \
echo "✅ CI/CD Workflow Suite scaffolded successfully in .github/workflows/"
```

### When Automation is Appropriate vs. Dangerous:

| Context | Recommended Approach | Reason |
|:---|:---:|:---|
| **Learning CI/CD Concepts** | **Option A (Step-by-Step)** | You understand what every block of YAML does before moving to the next level. |
| **Debugging Broken Pipelines** | **Option A (Step-by-Step)** | You can isolate which specific step or exit code failed. |
| **Setting up 10th Microservice** | **Option B (Automated Script)** | You already master the syntax; automation saves repetitive time. |
| **Enterprise Template Repos** | **Option B (Automated Script)** | Standardizes compliance policies across an organization. |

---

## 5. Comparative Analysis Matrix: Human Learning vs. AI Generation

| Feature | Option A: Step-by-Step (Human Engineer) | Option B: 1-Click / AI Generator |
|:---|:---|:---|
| **Pace** | Incremental (Level 0 → Level 5) | Instant (All 6 files at once) |
| **Mental Model** | Builds rock-solid understanding of runner lifecycle | Can feel like an opaque "black box" |
| **Error Recovery** | Easy: only 1 file changed, error is obvious | Hard: 6 files running simultaneously, hard to pinpoint blame |
| **Confidence** | High: you saw every green checkmark yourself | Medium: you hope the generated YAML syntax is valid |
| **Real-World Fidelity** | 100% matches how real software projects evolve | Matches enterprise platform team automation |

---

## 6. Common Pitfalls When Creating `.github` Workflows

1. **Creating `.github` in a Subfolder**:
   - ❌ `src/.github/workflows/`
   - ✅ `.github/workflows/` (MUST be at repository root).
2. **Missing the Suffix `s` in `workflows`**:
   - ❌ `.github/workflow/` (Ignored by GitHub!).
   - ✅ `.github/workflows/`.
3. **Empty Folder Not Tracked by Git**:
   - Git does not commit empty folders. If you run `mkdir -p .github/workflows` without creating a `.yml` file inside, `git status` will show nothing to commit.
   - Always create at least one file (e.g. `level0_first_ci.yml` or a `.gitkeep`) before committing.
4. **Tab Characters inside YAML**:
   - Never press `Tab`. Use 2 spaces per indentation level.

---

## 7. Summary & Educational Recommendation

- **For the TeachCloud CI/CD Tutorials**:
  We prioritize **Option A**. The tutorial guides learners to initialize `.github/workflows/` and add **Level 0 first**. Once learners see the live runner execute and verify exit codes, they unlock subsequent levels with genuine understanding.
- **For Advanced Reference**:
  Option B remains documented here in the docs so that learners transitioning to senior DevOps or Platform Engineering roles can leverage automated scaffolding when architecting enterprise repositories.

---
*TeachCloud DevOps Track • Learn CI/CD by Building Real Pipelines.*
