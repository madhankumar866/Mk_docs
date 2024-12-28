### 1. Workload Objects
Workload objects define the applications and jobs running in the cluster.

- **Pod**: The smallest deployable unit in Kubernetes. A pod runs one or more containers.
- **ReplicaSet**: Ensures a specified number of pod replicas are running at any given time.
- **Deployment**: Manages ReplicaSets and provides declarative updates for pods and ReplicaSets.
- **StatefulSet**: Manages stateful applications with persistent storage and unique pod identities.
- **DaemonSet**: Ensures that a copy of a pod runs on all or specific nodes in the cluster.
- **Job**: Creates pods to perform a specific task and ensures they complete successfully.
- **CronJob**: Manages jobs that run on a schedule, similar to a cron task.

### 2. Service and Networking Objects
These objects define how applications communicate internally and externally.

- **Service****: Exposes an application running on a set of pods as a network service.
- **Ingress****: Manages external HTTP and HTTPS access to services within the cluster.
- **EndpointSlice**: Tracks IP addresses and ports of services, supporting scalability.
- **NetworkPolicy**: Defines rules for controlling network traffic to/from pods.


### 3. Configuration Objects
Configuration objects store and manage configuration data for applications.

- **ConfigMap**: Stores non-sensitive configuration data as key-value pairs.
- **Secret**: Stores sensitive information like passwords, tokens, and keys in an encrypted format.
- **Volume**: Provides storage to pods, supporting different storage backends.
- **PersistentVolume (PV)**: Represents a storage resource in the cluster.
- **PersistentVolumeClaim (PVC)**: Requests storage resources from PVs.

### 4. Cluster Management Objects
These objects control the behavior and configuration of the Kubernetes cluster.

- **Namespace**: Provides logical isolation of resources within a cluster.
- **Node**: Represents a worker machine in the cluster.
- **HorizontalPodAutoscaler (HPA)**: Automatically scales the number of pods in a deployment or replica set based on resource usage.
- **VerticalPodAutoscaler (VPA)**: Adjusts resource requests and limits for pods.
- **Role and RoleBinding**: Define permissions within a namespace.
- **ClusterRole and ClusterRoleBinding**: Define permissions across the entire cluster.

### 5. Observability and Debugging Objects
These objects facilitate monitoring, logging, and troubleshooting.

- **Event**: Records changes or errors in the cluster.
- **PodDisruptionBudget (PDB)**: Limits the number of pods that can be down during maintenance.
- **Probe (Readiness, Liveness, Startup)**: Defines health checks for containers.


Custom Resource Definitions (CRDs)
- **CRDs**: Extend Kubernetes by defining your own objects. For example, in Argo Workflows, objects like Workflow and WorkflowTemplate are CRDs.