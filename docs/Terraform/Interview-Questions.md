# Terraform & DevOps Interview Questions

## Detailed Terraform Concepts

## Related pages

- [Terraform overview](Readme.md)
- [Terraform cheat sheet](Terraform_cheat_sheet.md)
- [Question bank: Senior DevOps](../questions/Senior-DevOps.md)
- [Question bank: Terraform](../questions/terraform.md)

??? question "1. How does Terraform build the dependency graph internally?"
    Terraform creates a **Directed Acyclic Graph (DAG)** based on resource references. It executes resources in parallel where possible. Dependencies are derived from interpolation references and `depends_on`.
    
    !!! tip "Senior Tip"
        Mention parallelism & execution plan graph.

??? question "2. What happens if two engineers run terraform apply at the same time?"
    If a remote backend with locking (S3 + DynamoDB) is enabled, one will fail due to state lock. Without locking, there is a risk of state corruption.

??? question "3. How would you design Terraform for multi-region AWS DR setup?"
    Expected thinking:
    *   Separate state per region
    *   Region-specific providers
    *   RDS cross-region replica
    *   Route53 failover
    *   Replicated S3
    *   Tested restore process
    *   *They test disaster recovery maturity here.*

??? question "4. Explain how Kubernetes service discovery works."
    Kubernetes uses:
    *   DNS (CoreDNS)
    *   ClusterIP services
    *   kube-proxy (iptables/IPVS)
    *   Pods communicate using: `service-name.namespace.svc.cluster.local`

??? question "5. How does Kubernetes handle network routing internally?"
    Expected:
    *   `kube-proxy` manages iptables rules
    *   CNI plugin (Calico / AWS VPC CNI) handles pod networking
    *   Each pod gets its own IP
    *   *Bonus if you mention overlay vs VPC-native networking.*

??? question "6. What is etcd and why is it critical?"
    `etcd` is a distributed key-value store used by Kubernetes to store cluster state. If `etcd` is down, the cluster control plane fails.
    
    !!! info "Senior Insight"
        Backup strategy, Snapshot restore.

??? question "7. Cluster Autoscaler vs HPA — how do they work together?"
    HPA scales pods. If pods can’t schedule, Cluster Autoscaler scales nodes via Auto Scaling Group.
    
    !!! note
        Mention integration with AWS ASG in EKS.

??? question "8. How would you debug high memory usage in Kubernetes?"
    Answer structure:
    1.  Check metrics (Prometheus)
    2.  Check pod resource limits
    3.  Check memory leaks
    4.  Check OOMKilled events
    5.  Adjust requests/limits
    
    !!! danger "Don't just say..."
        Never say just “increase memory”.

??? question "9. Your EKS cluster suddenly stops scheduling pods. What could be wrong?"
    Expected:
    *   No available nodes
    *   Node taints
    *   Resource exhaustion
    *   PVC binding issue
    *   CNI failure
    *   *This tests deep K8s understanding.*

??? question "10. How do you secure Kubernetes at production level?"
    Mention:
    *   RBAC
    *   Network Policies
    *   Pod Security Standards
    *   Image scanning
    *   Secrets encryption
    *   IAM roles for service accounts (IRSA in EKS)

??? question "11. How do you upgrade EKS cluster with zero downtime?"
    Expected:
    1.  Upgrade control plane
    2.  Create new node group
    3.  Drain old nodes
    4.  Monitor
    5.  Remove old node group
    
    !!! warning
        Never directly upgrade existing nodes if possible.

---

## 25 Rapid-Fire DevOps Interview Questions

### 🟦 Terraform

??? question "1. What is Terraform state and why is it important?"
    Terraform state (`terraform.tfstate`) is a JSON file that maps real-world infrastructure to your configuration. It acts as a single source of truth, tracks metadata, and improves performance for large infrastructures.

??? question "2. Difference between `terraform plan` and `terraform apply`?"
    `terraform plan` reads the state and shows what changes will be made without modifying actual infrastructure. `terraform apply` executes the plan and provisions or modifies the real-world resources.

??? question "3. What is remote backend and why use it?"
    A remote backend (like S3, GCS, or Terraform Cloud) stores the state file remotely rather than locally. It allows team collaboration, enables state locking (preventing concurrent modifications), and keeps sensitive data secure.

??? question "4. How do you prevent accidental resource deletion in Terraform?"
    Use the `lifecycle { prevent_destroy = true }` meta-argument on critical resources, enable versioning on your remote backend, and restrict IAM permissions.

??? question "5. What is the difference between `count` and `for_each`?"
    `count` creates resources using a numerical index, which can cause massive recreation if an item in the middle is removed. `for_each` uses stable map keys or strings, making it much safer for dynamic infrastructure.

??? question "6. How do you manage multiple environments in Terraform?"
    By using separate directories for each environment (e.g., `dev/`, `prod/`) referencing shared modules, or by using Terraform Workspaces (though directories are preferred for strict production isolation).

??? question "7. What happens if state file is corrupted?"
    Terraform cannot accurately determine the current infrastructure state, potentially leading to duplicate resources or destructive changes. You must recover it from a backup (like S3 versioning) or manually reconstruct it via `terraform import`.

### 🟦 Kubernetes

??? question "8. Difference between Deployment and StatefulSet?"
    A Deployment is for stateless applications where pods are identical and interchangeable. A StatefulSet is for stateful applications, providing stable, unique network identifiers and persistent storage for each pod.

??? question "9. What is HPA and how does it work?"
    Horizontal Pod Autoscaler (HPA) automatically scales the number of pods in a Deployment or StatefulSet based on observed CPU/memory utilization or custom metrics.

??? question "10. What is the difference between ClusterIP, NodePort, and LoadBalancer?"
    ClusterIP exposes the service internally within the cluster. NodePort exposes it on a static port on each Node's IP. LoadBalancer provisions an external cloud provider load balancer to route traffic to the service.

??? question "11. What causes `CrashLoopBackOff`?"
    A pod repeatedly failing to start and crashing immediately. Common causes: application code errors, missing dependencies/configurations, OOMKilled (Out of Memory), or failing liveness probes.

??? question "12. What are liveness and readiness probes?"
    Liveness probes check if an application is running (restarts the pod if it fails). Readiness probes check if the application is ready to receive traffic (removes the pod from service endpoints if it fails).

??? question "13. What happens when a node fails?"
    Kubernetes detects the node is unreachable, marks it as `NotReady`, and after a timeout (default 5 mins), reschedules its pods to other healthy nodes in the cluster.

??? question "14. How does Kubernetes scheduler decide pod placement?"
    It uses a two-step process: Filtering (finding nodes that meet resource requests, taints/tolerations, node selectors) and Scoring (ranking the filtered nodes based on optimal resource utilization and affinity/anti-affinity rules).

??? question "15. What is the difference between ConfigMap and Secret?"
    Both store configuration data, but ConfigMaps are for non-sensitive data (plain text), while Secrets are for sensitive data (base-64 encoded and can be encrypted at rest in etcd).

### 🟦 AWS / Cloud (EKS-focused)

??? question "16. What is the difference between Auto Scaling Group and HPA?"
    Auto Scaling Group (ASG) scales the actual underlying EC2 instances (nodes) in AWS. HPA (Horizontal Pod Autoscaler) scales the Kubernetes Pods running inside those nodes.

??? question "17. What happens if an EC2 instance in an Auto Scaling Group fails?"
    The ASG health checks detect the failure, terminate the unhealthy instance, and automatically launch a replacement instance to maintain the desired capacity.

??? question "18. How do you make an application highly available in AWS?"
    Deploy resources across multiple Availability Zones (AZs), use Auto Scaling Groups, place an Application Load Balancer in front, and use managed multi-AZ databases (like RDS Multi-AZ).

??? question "19. What is the difference between ALB and NLB?"
    ALB (Application Load Balancer) operates at Layer 7 (HTTP/HTTPS), supporting advanced routing and TLS termination. NLB (Network Load Balancer) operates at Layer 4 (TCP/UDP) and is optimized for ultra-high performance and low latency.

??? question "20. How do you secure S3 bucket?"
    Block all public access, enforce IAM policies and bucket policies, enable KMS encryption at rest, enforce SSL in transit (via policy conditions), enable versioning, and turn on MFA delete.

### 🟦 CI/CD

??? question "21. What is Blue-Green deployment?"
    A strategy where two identical environments exist (Blue is live, Green is new). Traffic is switched entirely from Blue to Green at the load balancer level, allowing instant rollback if issues occur.

??? question "22. What is Canary deployment?"
    Releasing a new version to a small subset of users (e.g., 5% traffic) to test stability before gradually rolling it out to the rest of the user base.

??? question "23. How do you rollback a failed deployment?"
    In Kubernetes, run `kubectl rollout undo deployment/<name>`. In standard CI/CD, re-trigger the pipeline for the previous stable Git commit or swap load balancer targets back to the old environment.

??? question "24. How do you secure CI/CD pipeline?"
    Use isolated/ephemeral runners, implement secret management (e.g., HashiCorp Vault, AWS Secrets Manager), scan code/images for vulnerabilities (SAST/DAST), enforce least privilege IAM roles, and require manual approvals for production deployments.

### 🟦 Monitoring & Troubleshooting

??? question "25. Production is slow — what is your troubleshooting approach?"
    1. Check monitoring dashboards (Prometheus/Grafana) to identify anomalies.
    2. Review logs (ELK/CloudWatch) for errors.
    3. Analyze resource metrics (CPU, Memory, Network bottlenecks, DB connections).
    4. Identify any recent deployments or configuration changes.
    5. If a recent change caused it, rollback to restore stability while investigating.

---

## Terraform Deep Dive (Q&A)

??? question "1. What happens if two engineers run terraform apply at the same time on the same remote backend?"
    If the backend supports state locking, the second apply will fail with a lock error. Terraform prevents concurrent modification of the state file because state is the single source of truth. Without locking, you risk:
    *   State corruption
    *   Duplicate resource creation
    *   Lost updates
    *   **With S3 + DynamoDB**, one engineer acquires the lock; the other gets: `Error acquiring the state lock`.
    
    !!! tip "Best practice"
        Always use remote backend with locking enabled; Never disable locking in production.

??? question "2. How does Terraform state locking work internally with S3 and DynamoDB?"
    S3 stores the state file. DynamoDB provides the lock mechanism.
    Internally:
    *   When apply starts, Terraform writes a lock entry to DynamoDB.
    *   The table has a primary key: `LockID`.
    *   If lock exists → operation fails.
    *   When apply finishes → lock entry is deleted.
    *   **DynamoDB ensures:** Atomic writes, strong consistency, TTL for stale locks (if configured).
    
    !!! note
        S3 alone does NOT support locking — DynamoDB is mandatory for safe concurrency.

??? question "3. Risks of manually editing .tfstate and recovery?"
    **Risks:** Resource address mismatch, orphaned resources, duplicate infra creation, complete corruption.
    State file is JSON but must never be manually edited unless emergency recovery.
    **Recovery:**
    1.  Restore from backend versioning (S3 versioning recommended).
    2.  Use `terraform state pull`.
    3.  Fix locally.
    4.  Push back using `terraform state push`.
    
    !!! tip "Better approach"
        Use `terraform state mv`, `terraform state rm`, or `terraform import`.

??? question "4. Designing Terraform architecture for multiple environments"
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

??? question "5. What is Terraform drift?"
    Drift occurs when **Actual infrastructure ≠ Terraform state**.
    *   Example: Someone manually deletes an EC2 instance.
    *   **Detection:** `terraform plan` will show changes needed to reconcile.
    *   **Prevention:** IAM policy to block manual console changes, use drift detection in CI pipelines, enable CloudTrail monitoring.
    
    !!! warning
        Never allow manual infra changes in production.

??? question "6. Difference between count and for_each?"
    *   **count:** Index-based (`count = 3`). Resources indexed numerically. Problem: If one resource is removed, all indexes shift → destroys and recreates infra.
    *   **for_each:** Key-based (`for_each = toset(["a","b","c"])`). Stable mapping using keys.
    
    !!! danger "Why count is dangerous"
        Index shifting can destroy production databases accidentally.
    
    !!! tip "Production rule"
        Use `for_each` for dynamic infra.

??? question "7. Migrating state from local to remote without downtime?"
    1.  Configure `backend` block.
    2.  Run `terraform init`.
    3.  Terraform will ask to migrate state. Confirm migration.
    
    !!! info
        No infra changes occur — only state moves.
    
    !!! note
        **Ensure:** No concurrent operations, backup state before migration.

??? question "8. Refactoring Terraform without destroying infra?"
    Use:
    *   `terraform state mv`
    *   `terraform state rm`
    *   `moved` blocks (Terraform 1.1+)
    
    Example moving resource into module: `terraform state mv aws_instance.web module.compute.aws_instance.web`
    
    !!! tip "Refactor rule"
        State first, then code. Never rename resources blindly.

??? question "9. Lifecycle meta-arguments"
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

??? question "10. Securely managing secrets in Terraform?"
    Never hardcode secrets.
    **Best practices:**
    *   Use AWS Secrets Manager, SSM Parameter Store, or Vault.
    *   Pass via environment variables.
    *   Mark variables as `sensitive = true`.
    
    !!! danger "State risk"
        Secrets can end up in state file. Solution: Encrypt S3 bucket, restrict IAM, enable KMS encryption.

??? question "11. How Terraform handles dependency graphs?"
    Terraform builds a **Directed Acyclic Graph (DAG)**. Dependencies are inferred from resource references and `depends_on`.
    *   **Execution order:** Parallel where possible, sequential where required. This ensures optimal performance and correct ordering.

??? question "12. Difference between refresh, plan, apply"
    *   **refresh:** Updates state to match real infra (deprecated as standalone in newer versions).
    *   **plan:** Reads state, compares with configuration, shows execution plan. Does NOT modify infra.
    *   **apply:** Executes plan, updates infra, updates state.
    
    !!! note
        Plan is safe. Apply is destructive.

??? question "13. Designing reusable enterprise modules"
    **Principles:**
    *   Single responsibility per module.
    *   Clear input/output variables.
    *   Versioned via Git tags (Semantic versioning).
    *   No hardcoded values.
    *   Well documented.
    
    **Enterprise pattern:** `source = "git::ssh://repo//vpc?ref=v1.2.0"`
    
    !!! tip "Version everything"
        Never use unversioned modules in production.

??? question "14. Zero-downtime updates with Terraform"
    **Techniques:**
    *   `create_before_destroy`
    *   Blue-Green deployments
    *   Load balancer switch
    *   Rolling ASG updates
    *   Separate target groups
    
    !!! info
        Never modify in-place for critical infra unless safe.

??? question "15. Handling partial creation failure"
    If apply fails midway: Terraform state contains partially created resources.
    1.  Run `terraform plan`.
    2.  Identify created resources.
    3.  Fix root cause.
    4.  Run `terraform apply` again.
    
    !!! tip "State recovery"
        If state inconsistent: Use `terraform state rm` or import resource. Never manually delete infra before checking state.
