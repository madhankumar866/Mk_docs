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

## key components of an ArgoCD Application resource?

ApplicationSet in ArgoCD?
health checks in ArgoCD?
purpose of the argocd-cm ConfigMap?
handle secrets in ArgoCD?




## Description
```
In this you will be central to our efforts in moving Workday deployment to a git-ops driven Argo Workflow / Argo CD based tooling. You will be responsible for designing, implementing, and supporting our deployment tooling, using tools like ArgoCD, Argo Workflows, Grafana and many others. You will work closely with SRE, Operations, and service teams to ensure smooth and reliable deployments of our applications

Responsibilities:

Design, develop, and maintain GitOps driven deployment tooling using ArgoCD and Argo Workflows.

Find opportunities to automate operations in Workdays public cloud (AWS/GCP) Kubernetes environments, including resource definitions and configurations.

Automate the build, test, and deployment processes for our teams software artifacts.

Collaborate with service teams to integrate their applications into the GitOps workflow.

Triage and resolve deployment issues, ensuring high availability and reliability of our environments.

Monitor and optimize the performance of our deployment tooling.

Implement and maintain security methodologies within the deployment tooling.

Improve the operational posture of our SRE and operations teams through use of enhanced observability available through CNCF tooling.

Document and maintain our deployment processes and procedures.

Stay up-to-date with the latest technologies and trends in GitOps and Kubernetes.

Participate in code reviews and contribute to the improvement of our development practices.

About You

Required Skills and Experience:

BSc, MSc or equivalent experience in Computer Science or related field and 4+ years industry experience

Proven experience with GitOps or equivalent experience.

Strong understanding of Kubernetes and its core concepts (Pods, Deployments, Services, etc.).

Hands-on experience with ArgoCD and Argo Workflows.

Proficiency in using Git and Git workflows.

Experience with CI/CD tools and methodologies.

Familiarity with containerization technologies (Docker).

Experience with scripting languages (e.g., Ruby, Groovy, Python).

Strong problem-solving skills.

Excellent communication and collaboration skills.

Preferred Skills and Experience:

Knowledge of monitoring and logging tools (e.g., Prometheus, Grafana, ELK stack).

Experience with cloud platforms (e.g., AWS, GCP, Azure).

Understanding of security methodologies in a cloud-native environment.
```

write a argocd yaml,
```
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/your-org/your-repo.git
    targetRevision: HEAD
    path: path/to/your/app
  destination:
    server: https://kubernetes.default.svc
    namespace: your-app-namespace
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true

## Key parts:
repoURL: Git repo containing your Kubernetes manifests or Helm chart.

path: The folder inside the repo where your app is defined.

destination: Where to deploy the app.

syncPolicy: Automates syncing and healing if something drifts..

🧠 2. Use a mnemonic
Try this simple flow:
"Meta-Spec Source to Destination with Sync."
Say it like a checklist during the interview.

## SIMPLE VERSION

apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: demo
spec:
  source:
    repoURL: <git-url>
    path: <path>
    targetRevision: HEAD
  destination:
    server: https://kubernetes.default.svc
    namespace: demo
  syncPolicy:
    automated: {}


```

 app,manifest
workflow yaml dag
docker file
python for loops,if else,
kuberenetes basic, resources def and configuration
linux
grafana
sanity checks
aws & 


Argo
[ write an argocd ]


