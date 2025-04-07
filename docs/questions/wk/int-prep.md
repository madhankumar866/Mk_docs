## 🧠 Technical Questions:

### ArgoCD / Argo Workflows

### How do you manage application deployment lifecycles with ArgoCD?
```
In my current role, I use ArgoCD to manage Kubernetes application deployments via GitOps. Each service has its own Helm chart or Kustomize configuration stored in a Git repository. ArgoCD continuously monitors these repos, and syncs changes to the respective clusters.

I follow a model where we have separate branches or folders for each environment (dev, prep, prod). Sync policies vary — auto-sync for lower environments and manual sync with approvals for prod. I’ve also configured health checks and notifications via Webhooks to WebEx for deployment events.
```
### Can you explain how ArgoCD syncs with Git and handles drift detection?
```
ArgoCD continuously compares the desired state defined in Git with the actual state in the Kubernetes cluster. If there's a drift — for example, someone manually modifies a deployment — ArgoCD marks the app as "OutOfSync".

Depending on the sync policy, it can auto-sync to correct the drift or wait for manual approval. I’ve configured notifications so our team gets Slack/WebEx alerts on such drift events. This has helped us reduce configuration inconsistencies across environments.


```
### What's your experience with Argo Workflows for complex multi-step pipelines?

### Kubernetes & GitOps

### How do you troubleshoot failed Pods or unresponsive Services?
```
In my current role, I use ArgoCD to manage Kubernetes application deployments via GitOps. Each service has its own Helm chart or Kustomize configuration stored in a Git repository. ArgoCD continuously monitors these repos, and syncs changes to the respective clusters.

I follow a model where we have separate branches or folders for each environment (dev, prep, prod). Sync policies vary — auto-sync for lower environments and manual sync with approvals for prod. I’ve also configured health checks and notifications via Webhooks to WebEx for deployment events.
```

### Describe your experience using Helm/Kustomize with GitOps.

### How would you design a multi-env GitOps setup (dev/staging/prod)?

### CI/CD & Automation

### Walk me through a pipeline you built — tools used, triggers, deployment stages.

### How do you ensure zero-downtime deployments?

### Observability

### What monitoring/alerting stack have you used (Prometheus, Grafana, etc.)?

### How do you visualize Kubernetes metrics?

### 6. How do you monitor deployments and application health?
```
I use a combination of Prometheus for metrics, Grafana for dashboards, and ArgoCD’s UI for deployment health. We’ve defined SLOs around deployment success rate and MTTR.

I also use readiness and liveness probes to catch failures early. On the observability side, we feed logs to Elasticsearch and alerts to Opsgenie, which we triage in WebEx using a custom bot.
```


## Behavioral Questions: ???

### Tell me about a time you had to troubleshoot a critical production deployment.

```

## IMP ASK Suraj About the tool he deployed
Once during a prod release, ArgoCD failed to sync due to a Helm chart change that introduced a breaking field in values.yaml. The rollout failed midway, and part of the app became unavailable.

I quickly disabled auto-sync in ArgoCD, rolled back to the previous version using kubectl rollout undo, and restored the working config from Git.

Post-mortem revealed a missing schema validation. I added helm lint and schema checks to our CI pipeline to catch such issues early. This also led us to implement ArgoCD's validation hooks before promoting to prod.
```

### Describe how you collaborated with developers or SREs to improve deployment workflows.

### Have you ever migrated a team from traditional CI/CD to GitOps? 