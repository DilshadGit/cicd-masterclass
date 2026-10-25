# 🎓 CI/CD Masterclass Quiz (24 Questions & Complete Answer Key)

1. **What is the difference between Continuous Delivery and Continuous Deployment?**
   - Answer: Continuous Delivery awaits human approval before production; Continuous Deployment releases automatically without manual gates.
2. **Where must GitHub Actions workflow YAML files reside?**
   - Answer: `.github/workflows/`
3. **Which event triggers a workflow on PR creation or updates?**
   - Answer: `on: pull_request`
4. **How do multiple jobs run by default?**
   - Answer: In parallel across separate runner virtual machines.
5. **Which directive establishes job execution dependencies?**
   - Answer: `needs: [jobA, jobB]`
6. **Which action standardly checks out repository source code?**
   - Answer: `actions/checkout@v4`
7. **How do you reference an encrypted repository secret?**
   - Answer: `${{ secrets.SECRET_NAME }}`
8. **Which exit status code denotes clean success to the CI runner?**
   - Answer: `0`
9. **Which conditional expression forces a cleanup step to run even after failures?**
   - Answer: `if: always()`
10. **What does 'continue-on-error: true' achieve?**
    - Answer: Prevents step failure from failing the overall job.
11. **Which feature runs tests across multiple Python versions simultaneously?**
    - Answer: `strategy: matrix`
12. **What is the benefit of 'actions/cache@v4'?**
    - Answer: Drastically decreases build duration by reusing dependency directories.
13. **Which action persists artifacts across jobs?**
    - Answer: `actions/upload-artifact@v4`
14. **What is concurrency cancel-in-progress used for?**
    - Answer: Cancels outdated builds when new commits are pushed to the same branch.
15. **What does Static Application Security Testing (SAST) do?**
    - Answer: Analyzes source code for CVEs and vulnerabilities without execution.
16. **Which action logs the runner into container registries (GHCR / Docker Hub)?**
    - Answer: `docker/login-action@v3`
17. **Why use multi-stage Docker builds in CI/CD?**
    - Answer: Yields minimal, secure runtime containers by discarding compilers and build tools.
18. **What is Blue/Green deployment?**
    - Answer: Running two identical environments and switching traffic instantly with zero downtime.
19. **What is Canary deployment?**
    - Answer: Gradually shifting a small percentage of live traffic to the new release to monitor telemetry.
20. **What is the core philosophy of GitOps?**
    - Answer: Git is the single source of truth for declaratively defined system state.
21. **What happens in Bash steps without 'set -e'?**
    - Answer: The shell continues executing following lines despite errors.
22. **Which event allows manual workflow triggers with inputs?**
    - Answer: `on: workflow_dispatch`
23. **What is the difference between readiness and liveness probes?**
    - Answer: Readiness determines when traffic can be routed; liveness restarts hung containers.
24. **Which workflow command masks sensitive strings from logs?**
    - Answer: `echo '::add-mask::secret'`
