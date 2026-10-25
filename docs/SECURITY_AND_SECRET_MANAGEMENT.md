# CI/CD Security Hardening & Secret Management

A comprehensive guide to locking down CI/CD pipelines against supply chain attacks, token theft, and vulnerability leakage.

---

## 1. Principles of Least Privilege for GITHUB_TOKEN
Always disable default read-write permissions at the workflow level:
```yaml
permissions:
  contents: read
  packages: write
  pull-requests: read
```

## 2. Supply Chain Security (SLSA & Pinning Actions)
Never reference mutable tags like `@v3` in production workflows. Pin to immutable Git commit SHAs:
```yaml
- uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
- uses: actions/setup-python@0a5c61591373683505ea898e09a3ea4f39ef2b9c # v5.0.0
```

## 3. Automated Vulnerability Scanning
Integrate container vulnerability scanning via Aqua Security Trivy:
```yaml
- name: Scan Docker Image for High/Critical CVEs
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'teachcloud/api:${{ github.sha }}'
    format: 'table'
    exit-code: '1'
    ignore-unfixed: true
    vuln-type: 'os,library'
    severity: 'CRITICAL,HIGH'
```
