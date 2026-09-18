# AWS SRE Resilience & Recovery POC

Runnable reference for DevRabbit’s LinkedIn-posted remote SRE Lead role. It makes an AWS/Kubernetes release decision only after checking PostgreSQL replica lag, backup verification, Kubernetes readiness, error budget, and change approval.

## How it works

The POC returns one of three outcomes:

- `stabilize-and-page` when reliability or recovery signals are unsafe;
- `await-change-approval` when production is healthy but the change is not approved;
- `proceed-approved-change` only when all controls are satisfied.

In production, CloudWatch/Prometheus and PostgreSQL telemetry feed the signals; Terraform/GitOps uses the decision to gate a deployment; the outcome links to an incident or change record.

```bash
python3 -m unittest discover -s tests -v
```

This POC does not claim access to DevRabbit or customer systems.

Candidate: https://www.linkedin.com/in/rahul-h-bhatia/ · https://rahulhbhatia.vercel.app
