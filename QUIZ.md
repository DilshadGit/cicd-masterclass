# 🎯 TeachCloud Current Active Assessment — CI/CD Pipelines

> **Current Active 7-Day Cycle**: Edition #42 (2026-10-15 → 2026-10-22 UTC)
> **Automatic Rotation Policy**: New random questions reload every 7 days.
> **Top-Reloading Architecture**: Newly generated questions are appended on the top with date tags. Older questions are permanently preserved below without duplicates.
> **Historical Storage Vault**: Archived weekly snapshots reside in [`docs/Quiz/Store/`](Store/).

---

## 🔄 Weekly Update: 2026-10-24 (Edition #43)
> **Active Dates**: 2026-10-22 to 2026-10-29 UTC
> **New Unique Questions Reloaded**: 5

### Question 1: What is the function of dynamic ephemeral environments in CI/CD (Preview Environments)?

- [x] **Spins up isolated temporary environments per pull request to validate feature changes before merging** *(Correct Answer)*
- [ ] Runs production workloads continuously
- [ ] Backs up production databases
- [ ] Deletes old git tags

> **💡 Engineering Context & Rationale**:
> <strong>Preview Environments</strong> provision short-lived instances for testing pull requests in isolation.

---

### Question 2: What is a Build Trigger in CI tools?

- [x] **An event (e.g. code push, PR open, scheduled cron) that automatically initiates pipeline execution** *(Correct Answer)*
- [ ] A physical button in the datacenter
- [ ] A compiler error message
- [ ] A database lock timeout

> **💡 Engineering Context & Rationale**:
> <strong>Build Triggers</strong> initiate automated pipeline workflows upon repository changes.

---

### Question 3: What is the role of automated Code Coverage thresholds in CI?

- [x] **Fails the build pipeline if unit test coverage drops below a specified percentage (e.g. 80%)** *(Correct Answer)*
- [ ] Measures network bandwidth speed
- [ ] Calculates line counts of HTML templates
- [ ] Enforces git commit message lengths

> **💡 Engineering Context & Rationale**:
> <strong>Code Coverage thresholds</strong> ensure developers write adequate unit tests for new code modifications.

---

### Question 4: What is Semantic Versioning (SemVer) standard format?

- [x] **`MAJOR.MINOR.PATCH` (e.g. `2.1.4`)** *(Correct Answer)*
- [ ] `YEAR.MONTH.DAY`
- [ ] `BUILD.REVISION.SUB`
- [ ] `ALPHA.BETA.GAMMA`

> **💡 Engineering Context & Rationale**:
> <strong>SemVer</strong> uses `MAJOR.MINOR.PATCH` where MAJOR denotes breaking changes, MINOR denotes features, and PATCH denotes fixes.

---

### Question 5: What is Dynamic Application Security Testing (DAST) in CI/CD pipelines?

- [x] **Evaluates running applications from the outside by simulating security attacks against exposed endpoints** *(Correct Answer)*
- [ ] Scans static source code files
- [ ] Scans Dockerfile layer syntax
- [ ] Tests database query speed

> **💡 Engineering Context & Rationale**:
> <strong>DAST tools</strong> test active running applications against security vulnerabilities (e.g. OWASP ZAP).

---
## 🔄 Weekly Update: 2026-10-20 (Edition #42)
> **Active Dates**: 2026-10-15 to 2026-10-22 UTC
> **Active Questions Count**: 16

### Question 1: What is Immutable Deployment Artifact principle?

- [x] **Building and packaging artifacts (e.g. Docker images) once in CI and deploying the exact same artifact across staging and production** *(Correct Answer)*
- [ ] Re-compiling source code directly on production servers
- [ ] Modifying binary files after deployment
- [ ] Deleting build artifacts immediately after creation

> **💡 Engineering Context & Rationale**:
> <strong>Immutable artifacts</strong> guarantee that the exact binary tested in staging is what runs in production.

---
### Question 2: What is the purpose of Slack or Teams webhook notifications in CI/CD pipelines?

- [x] **Alerts engineering teams instantly when build pipelines succeed or fail** *(Correct Answer)*
- [ ] Sends marketing emails to app users
- [ ] Deletes failed cloud deployments
- [ ] Logs into server SSH sessions

> **💡 Engineering Context & Rationale**:
> Webhook integrations broadcast pipeline build events directly into team chat channels.

---
### Question 3: How do Feature Flags (Feature Toggles) support Continuous Deployment?

- [x] **Allows releasing code to production with new features wrapped in disabled toggles, enabling dark launches and instant rollbacks** *(Correct Answer)*
- [ ] Bypasses unit test checks
- [ ] Encrypts user passwords
- [ ] Disables deployment logs

> **💡 Engineering Context & Rationale**:
> <strong>Feature Flags</strong> decouple code deployment from feature activation, allowing safe testing in production.

---
### Question 4: What does `terraform plan` perform inside a CI validation pipeline?

- [x] **Generates an execution plan showing proposed infrastructure additions, modifications, or deletions without applying changes** *(Correct Answer)*
- [ ] Applies changes to cloud infrastructure immediately
- [ ] Destroys existing cloud resources
- [ ] Downloads terraform provider plugins only

> **💡 Engineering Context & Rationale**:
> <code>terraform plan</code> allows code reviewers to verify proposed infrastructure changes before approval.

---
### Question 5: What is a Canary Deployment in CD automation?

- [x] **Rolls out updates incrementally to a small percentage of users first, monitoring error rates before expanding to 100% traffic** *(Correct Answer)*
- [ ] Deploys updates to staging environments only
- [ ] Replaces all production servers at once
- [ ] Switches DNS records instantly

> **💡 Engineering Context & Rationale**:
> <strong>Canary deployments</strong> minimize blast radius by exposing new releases to a fraction of live traffic.

---
### Question 6: What is Concurrency Control in CI/CD pipeline execution?

- [x] **Prevents concurrent workflow runs on the same branch or environment from stepping on each other by canceling redundant queued builds** *(Correct Answer)*
- [ ] Runs jobs in parallel across 100 nodes
- [ ] Limits maximum user logins
- [ ] Throttles HTTP request rates

> **💡 Engineering Context & Rationale**:
> <strong>Concurrency control</strong> cancels outdated pull request pipeline builds when new commits are pushed.

---
### Question 7: What is Static Application Security Testing (SAST) in CI pipelines?

- [x] **Analyzes application source code for security vulnerabilities without executing the code** *(Correct Answer)*
- [ ] Scans active web servers by sending HTTP attacks
- [ ] Tests database connection latency
- [ ] Verifies SSL certificate expiration dates

> **💡 Engineering Context & Rationale**:
> <strong>SAST tools</strong> (e.g. SonarQube, Bandit) scan source code for known vulnerability patterns prior to compilation.

---
### Question 8: What is Container Vulnerability Scanning in CI pipelines (e.g. Trivy, Clair)?

- [x] **Scans container base images and OS packages for known Common Vulnerabilities and Exposures (CVEs)** *(Correct Answer)*
- [ ] Checks container CPU speeds
- [ ] Formats Dockerfile code
- [ ] Monitors container network traffic

> **💡 Engineering Context & Rationale**:
> <strong>Container scanners</strong> detect CVEs in container base images before pushing to registries.

---
### Question 9: In GitHub Actions, what directory stores workflow definition files?

- [x] **`.github/workflows/`** *(Correct Answer)*
- [ ] `.ci/pipelines/`
- [ ] `/bin/actions/`
- [ ] `.git/hooks/`

> **💡 Engineering Context & Rationale**:
> GitHub Actions workflow YAML manifests are stored in <strong>.github/workflows/</strong>.

---
### Question 10: What is Linting in CI code quality checks?

- [x] **Analyzing source code to flag programming errors, bugs, stylistic errors, and anti-patterns** *(Correct Answer)*
- [ ] Compiling code to C binaries
- [ ] Running integration test suites
- [ ] Encrypting git repositories

> **💡 Engineering Context & Rationale**:
> <strong>Linters</strong> (e.g. Flake8, ESLint) enforce code style and catch static syntax bugs early.

---
### Question 11: What is an Approval Gate in Continuous Delivery?

- [x] **A manual checkpoint requiring explicit sign-off from authorized personnel before triggering production deployment** *(Correct Answer)*
- [ ] A security firewall hardware appliance
- [ ] An automated unit test suite
- [ ] A DNS routing rule

> **💡 Engineering Context & Rationale**:
> <strong>Approval Gates</strong> require manual user verification before proceeding to production releases.

---
### Question 12: What is the primary difference between Continuous Delivery and Continuous Deployment?

- [x] **Continuous Delivery automates build/test steps requiring manual approval to release to production; Continuous Deployment automates release to production automatically without manual intervention** *(Correct Answer)*
- [ ] Continuous Delivery is for open-source; Continuous Deployment is for enterprises
- [ ] Continuous Deployment requires zero testing
- [ ] They are exact aliases

> **💡 Engineering Context & Rationale**:
> <strong>Continuous Delivery</strong> keeps main branch always ready for production deployment via manual trigger; <strong>Continuous Deployment</strong> pushes all passing commits directly to production.

---
### Question 13: What is a Pipeline Artifact in CI/CD automation?

- [x] **Files or compiled binaries generated by a workflow step (e.g. build binaries, test coverage reports) preserved for downstream steps or deployment** *(Correct Answer)*
- [ ] Unused git branches
- [ ] Old log files on build nodes
- [ ] Security vulnerabilities detected by scanners

> **💡 Engineering Context & Rationale**:
> <strong>Pipeline Artifacts</strong> persist build outputs (e.g., compiled code binaries or test reports) across workflow jobs.

---
### Question 14: Why is secret masking critical in CI/CD runner logs?

- [x] **Prevents encrypted secrets (e.g. API tokens, database passwords) from leaking in plain text in public build console outputs** *(Correct Answer)*
- [ ] Accelerates pipeline execution speed
- [ ] Reduces runner RAM consumption
- [ ] Encrypts git commit hashes

> **💡 Engineering Context & Rationale**:
> <strong>Secret masking</strong> sanitizes build logs, replacing confidential string variables with `***`.

---
### Question 15: What is the purpose of Matrix Builds in CI pipelines?

- [x] **Runs job steps concurrently across multiple operating systems, Python versions, or hardware combinations** *(Correct Answer)*
- [ ] Compiles database matrices into JSON
- [ ] Executes 3D graphics benchmarks
- [ ] Merges Git pull requests automatically

> **💡 Engineering Context & Rationale**:
> <strong>Matrix builds</strong> allow testing code across combinations of runtime versions (e.g. Python 3.9, 3.10, 3.11 on Ubuntu and macOS).

---
### Question 16: How do Self-Hosted Runners differ from Cloud-Hosted Runners in GitHub Actions?

- [x] **Self-hosted runners are dedicated servers managed by the user; cloud-hosted runners are ephemeral VMs provisioned automatically by GitHub** *(Correct Answer)*
- [ ] Self-hosted runners do not support Docker
- [ ] Cloud-hosted runners are free for unlimited private usage
- [ ] They execute different YAML syntax

> **💡 Engineering Context & Rationale**:
> <strong>Self-hosted runners</strong> run on custom infrastructure, offering access to internal networks and custom hardware.

---
