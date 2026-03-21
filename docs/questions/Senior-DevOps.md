# Senior-Level DevOps Interview Questions

These questions are designed to test architecture thinking, failure handling, production maturity, deep Kubernetes + Terraform knowledge, and an SRE mindset. They separate experienced engineers from beginners.

---

## 🔥 11 Senior-Level Tricky DevOps Interview Questions

### 1️⃣ How does Terraform build the dependency graph internally?
Terraform creates a **Directed Acyclic Graph (DAG)** based on resource references. It executes resources in parallel where possible. Dependencies are derived from interpolation references and `depends_on`.
*   **Senior Tip:** Mention parallelism & execution plan graph.

### 2️⃣ What happens if two engineers run terraform apply at the same time?
If a remote backend with locking (S3 + DynamoDB) is enabled, one will fail due to state lock. Without locking, there is a risk of state corruption.

### 3️⃣ How would you design Terraform for multi-region AWS DR setup?
Expected thinking:
*   Separate state per region
*   Region-specific providers
*   RDS cross-region replica
*   Route53 failover
*   Replicated S3
*   Tested restore process
*   *This tests disaster recovery maturity.*

### 4️⃣ Explain how Kubernetes service discovery works.
Kubernetes uses:
*   **DNS (CoreDNS):** Provides name resolution for services.
*   **ClusterIP services:** Virtual IPs that represent a group of pods.
*   **kube-proxy (iptables/IPVS):** Manages the routing of traffic to the correct pod.
*   **Communication:** Pods communicate using `service-name.namespace.svc.cluster.local`.

### 5️⃣ How does Kubernetes handle network routing internally?
Expected:
*   `kube-proxy` manages iptables or IPVS rules to route traffic.
*   **CNI plugin** (e.g., Calico, AWS VPC CNI) handles pod-to-pod networking and IP assignment.
*   Each pod gets its own unique IP address.
*   *Bonus: Mention overlay vs. VPC-native networking.*

### 6️⃣ What is etcd and why is it critical?
`etcd` is a distributed key-value store used by Kubernetes to store the entire cluster state. If `etcd` is down, the cluster control plane fails, and no changes can be made to the cluster.
*   **Senior Tip:** Mention backup strategies and snapshot restore procedures.

### 7️⃣ Cluster Autoscaler vs HPA — how do they work together?
*   **HPA (Horizontal Pod Autoscaler):** Scales the number of pods based on resource usage.
*   **Cluster Autoscaler:** If pods cannot be scheduled due to lack of resources, it scales the number of nodes via the cloud provider's Auto Scaling Group (ASG).
*   *Mention integration with AWS ASG in EKS.*

### 8️⃣ How would you debug high memory usage in Kubernetes?
Answer structure:
1.  Check metrics (e.g., Prometheus/Grafana).
2.  Review pod resource limits and requests.
3.  Investigate application-level memory leaks.
4.  Analyze `OOMKilled` events in the cluster.
5.  Adjust requests/limits based on empirical data.
*   *Never say just “increase memory”.*

### 9️⃣ Your EKS cluster suddenly stops scheduling pods. What could be wrong?
Expected:
*   **No available nodes:** Reached max capacity of ASG.
*   **Node taints:** Pods don't have required tolerations.
*   **Resource exhaustion:** CPU/Memory fully allocated.
*   **PVC binding issue:** Storage not available in the node's AZ.
*   **CNI failure:** No IP addresses available for pods.

### 🔟 How do you secure Kubernetes at production level?
Mention:
*   **RBAC:** Least privilege access control.
*   **Network Policies:** Restrict traffic between pods.
*   **Pod Security Standards:** Prevent privileged containers.
*   **Image scanning:** Check for vulnerabilities in the pipeline.
*   **Secrets encryption:** Encrypting data in `etcd`.
*   **IRSA (IAM Roles for Service Accounts):** Securely assigning AWS permissions to pods.

### 1️⃣1️⃣ How do you upgrade EKS cluster with zero downtime?
Expected process:
1.  Upgrade the Control Plane first.
2.  Create a new node group with the newer version.
3.  **Drain** the old nodes (evict pods gracefully).
4.  Monitor application health during migration.
5.  Remove the old node group once all pods are migrated.
*   *Never perform an in-place upgrade of live nodes.*

---
#DevOps #Interview #QA
