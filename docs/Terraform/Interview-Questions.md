# Terraform & DevOps Interview Questions

## Detailed Terraform Concepts

### 1. How does Terraform build the dependency graph internally?
Terraform creates a **Directed Acyclic Graph (DAG)** based on resource references. It executes resources in parallel where possible. Dependencies are derived from interpolation references and `depends_on`.
*   **Senior Tip:** Mention parallelism & execution plan graph.

### 2. What happens if two engineers run terraform apply at the same time?
If a remote backend with locking (S3 + DynamoDB) is enabled, one will fail due to state lock. Without locking, there is a risk of state corruption.

### 3. How would you design Terraform for multi-region AWS DR setup?
Expected thinking:
*   Separate state per region
*   Region-specific providers
*   RDS cross-region replica
*   Route53 failover
*   Replicated S3
*   Tested restore process
*   *They test disaster recovery maturity here.*

### 4. Explain how Kubernetes service discovery works.
Kubernetes uses:
*   DNS (CoreDNS)
*   ClusterIP services
*   kube-proxy (iptables/IPVS)
*   Pods communicate using: `service-name.namespace.svc.cluster.local`

### 5. How does Kubernetes handle network routing internally?
Expected:
*   `kube-proxy` manages iptables rules
*   CNI plugin (Calico / AWS VPC CNI) handles pod networking
*   Each pod gets its own IP
*   *Bonus if you mention overlay vs VPC-native networking.*

### 6. What is etcd and why is it critical?
`etcd` is a distributed key-value store used by Kubernetes to store cluster state. If `etcd` is down, the cluster control plane fails.
*   **Senior engineers mention:** Backup strategy, Snapshot restore.

### 7. Cluster Autoscaler vs HPA — how do they work together?
HPA scales pods. If pods can’t schedule, Cluster Autoscaler scales nodes via Auto Scaling Group.
*   **Mention:** Integration with AWS ASG in EKS.

### 8. How would you debug high memory usage in Kubernetes?
Answer structure:
1.  Check metrics (Prometheus)
2.  Check pod resource limits
3.  Check memory leaks
4.  Check OOMKilled events
5.  Adjust requests/limits
*   *Never say just “increase memory”.*

### 9. Your EKS cluster suddenly stops scheduling pods. What could be wrong?
Expected:
*   No available nodes
*   Node taints
*   Resource exhaustion
*   PVC binding issue
*   CNI failure
*   *This tests deep K8s understanding.*

### 10. How do you secure Kubernetes at production level?
Mention:
*   RBAC
*   Network Policies
*   Pod Security Standards
*   Image scanning
*   Secrets encryption
*   IAM roles for service accounts (IRSA in EKS)

### 11. How do you upgrade EKS cluster with zero downtime?
Expected:
1.  Upgrade control plane
2.  Create new node group
3.  Drain old nodes
4.  Monitor
5.  Remove old node group
*   *Never directly upgrade.*

---

## 25 Rapid-Fire DevOps Interview Questions

### 🟦 Terraform
1.  What is Terraform state and why is it important?
2.  Difference between `terraform plan` and `terraform apply`?
3.  What is remote backend and why use it?
4.  How do you prevent accidental resource deletion in Terraform?
5.  What is the difference between `count` and `for_each`?
6.  How do you manage multiple environments in Terraform?
7.  What happens if state file is corrupted?

### 🟦 Kubernetes
8.  Difference between Deployment and StatefulSet?
9.  What is HPA and how does it work?
10. What is the difference between ClusterIP, NodePort, and LoadBalancer?
11. What causes `CrashLoopBackOff`?
12. What are liveness and readiness probes?
13. What happens when a node fails?
14. How does Kubernetes scheduler decide pod placement?
15. What is the difference between ConfigMap and Secret?

### 🟦 AWS / Cloud (EKS-focused)
16. What is the difference between Auto Scaling Group and HPA?
17. What happens if an EC2 instance in an Auto Scaling Group fails?
18. How do you make an application highly available in AWS?
19. What is the difference between ALB and NLB?
20. How do you secure S3 bucket?

### 🟦 CI/CD
21. What is Blue-Green deployment?
22. What is Canary deployment?
23. How do you rollback a failed deployment?
24. How do you secure CI/CD pipeline?

### 🟦 Monitoring & Troubleshooting
25. Production is slow — what is your troubleshooting approach?

---

## Terraform Deep Dive (Q&A)

### 1. What happens if two engineers run terraform apply at the same time on the same remote backend?
If the backend supports state locking, the second apply will fail with a lock error. Terraform prevents concurrent modification of the state file because state is the single source of truth. Without locking, you risk:
*   State corruption
*   Duplicate resource creation
*   Lost updates
*   **With S3 + DynamoDB**, one engineer acquires the lock; the other gets: `Error acquiring the state lock`.
*   **Best practice:** Always use remote backend with locking enabled; Never disable locking in production.

### 2. How does Terraform state locking work internally with S3 and DynamoDB?
S3 stores the state file. DynamoDB provides the lock mechanism.
Internally:
*   When apply starts, Terraform writes a lock entry to DynamoDB.
*   The table has a primary key: `LockID`.
*   If lock exists → operation fails.
*   When apply finishes → lock entry is deleted.
*   **DynamoDB ensures:** Atomic writes, strong consistency, TTL for stale locks (if configured).
*   *S3 alone does NOT support locking — DynamoDB is mandatory for safe concurrency.*

### 3. Risks of manually editing .tfstate and recovery?
**Risks:** Resource address mismatch, orphaned resources, duplicate infra creation, complete corruption.
State file is JSON but must never be manually edited unless emergency recovery.
**Recovery:**
1.  Restore from backend versioning (S3 versioning recommended).
2.  Use `terraform state pull`.
3.  Fix locally.
4.  Push back using `terraform state push`.
*   **Better approach:** Use `terraform state mv`, `terraform state rm`, or `terraform import`.

### 4. Designing Terraform architecture for multiple environments
**Option 1: Folder per environment**
```
envs/
  dev/
  qa/
  prod/
modules/
```
**Option 2 (Better): Single codebase + workspaces (for small setups)**
**Enterprise Best Practice:**
*   Separate state per environment.
*   Separate AWS accounts per environment.
*   Shared reusable modules.
*   CI/CD controlled apply.
*   No manual local apply for prod.
*   **Golden rule:** Isolation + modularity + version control.

### 5. What is Terraform drift?
Drift occurs when **Actual infrastructure ≠ Terraform state**.
*   Example: Someone manually deletes an EC2 instance.
*   **Detection:** `terraform plan` will show changes needed to reconcile.
*   **Prevention:** IAM policy to block manual console changes, use drift detection in CI pipelines, enable CloudTrail monitoring.
*   *Never allow manual infra changes in production.*

### 6. Difference between count and for_each?
*   **count:** Index-based (`count = 3`). Resources indexed numerically. Problem: If one resource is removed, all indexes shift → destroys and recreates infra.
*   **for_each:** Key-based (`for_each = toset(["a","b","c"])`). Stable mapping using keys.
*   **Why count is dangerous:** Index shifting can destroy production databases accidentally.
*   **Production rule:** Use `for_each` for dynamic infra.

### 7. Migrating state from local to remote without downtime
1.  Configure `backend` block.
2.  Run `terraform init`.
3.  Terraform will ask to migrate state. Confirm migration.
*   *No infra changes occur — only state moves.*
*   **Ensure:** No concurrent operations, backup state before migration.

### 8. Refactoring Terraform without destroying infra
Use:
*   `terraform state mv`
*   `terraform state rm`
*   `moved` blocks (Terraform 1.1+)
Example moving resource into module: `terraform state mv aws_instance.web module.compute.aws_instance.web`
*   **Refactor rule:** State first, then code. Never rename resources blindly.

### 9. Lifecycle meta-arguments
Inside resource:
```hcl
lifecycle {
  create_before_destroy = true
  prevent_destroy = true
  ignore_changes = [...]
}
```
*   **create_before_destroy:** Used for Load balancers, Databases, Zero-downtime updates.
*   **prevent_destroy:** Used for Production DB, Critical storage buckets. Prevents accidental deletion.

### 10. Securely managing secrets in Terraform
Never hardcode secrets.
**Best practices:**
*   Use AWS Secrets Manager, SSM Parameter Store, or Vault.
*   Pass via environment variables.
*   Mark variables as `sensitive = true`.
*   **State risk:** Secrets can end up in state file. Solution: Encrypt S3 bucket, restrict IAM, enable KMS encryption.

### 11. How Terraform handles dependency graphs
Terraform builds a **Directed Acyclic Graph (DAG)**. Dependencies are inferred from resource references and `depends_on`.
*   **Execution order:** Parallel where possible, sequential where required. This ensures optimal performance and correct ordering.

### 12. Difference between refresh, plan, apply
*   **refresh:** Updates state to match real infra (deprecated as standalone in newer versions).
*   **plan:** Reads state, compares with configuration, shows execution plan. Does NOT modify infra.
*   **apply:** Executes plan, updates infra, updates state.
*   *Plan is safe. Apply is destructive.*

### 13. Designing reusable enterprise modules
**Principles:**
*   Single responsibility per module.
*   Clear input/output variables.
*   Versioned via Git tags (Semantic versioning).
*   No hardcoded values.
*   Well documented.
**Enterprise pattern:** `source = "git::ssh://repo//vpc?ref=v1.2.0"`
*   *Never use unversioned modules in production.*

### 14. Zero-downtime updates with Terraform
**Techniques:**
*   `create_before_destroy`
*   Blue-Green deployments
*   Load balancer switch
*   Rolling ASG updates
*   Separate target groups
*   *Never modify in-place for critical infra unless safe.*

### 15. Handling partial creation failure
If apply fails midway: Terraform state contains partially created resources.
1.  Run `terraform plan`.
2.  Identify created resources.
3.  Fix root cause.
4.  Run `terraform apply` again.
*   If state inconsistent: Use `terraform state rm` or import resource. Never manually delete infra before checking state.
