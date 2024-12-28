## Kubernetes-questions

1. Create a yaml file for pod in cluster

2. Kubernetes objects
```
Workload objects define the applications and jobs running in the cluster.

Pod: The smallest deployable unit in Kubernetes. A pod runs one or more containers.
ReplicaSet: Ensures a specified number of pod replicas are running at any given time.
Deployment: Manages ReplicaSets and provides declarative updates for pods and ReplicaSets.
StatefulSet: Manages stateful applications with persistent storage and unique pod identities.
DaemonSet: Ensures that a copy of a pod runs on all or specific nodes in the cluster.
Job: Creates pods to perform a specific task and ensures they complete successfully.
CronJob: Manages jobs that run on a schedule, similar to a cron task.
```

3. Few Kubernetes commands:

4. Sceanrio based question
Namespace call tata, there are many service under namespace. Some services failed no pro active alerts 
Get list of pods that are not in running state, and in-incomplete pods

```
kubectl get pods -n tata --field-selector=status.phase!=Running

```

5. Faulty node one our cluster service hosting in the cluster not responding auto to not fault, I have ip of the node, we wan’t to find the services running in node
```
kubectl get pods -o wide --all-namespaces | grep <node-ip>

##Find Services Linked to Those Pods##

kubectl get svc --all-namespaces | grep <pod-name>
```

6. List pods with nodes running
```
kubectl get pods -o wide
    Alternaive
kubectl get pods -o custom-columns="NAME:.metadata.name,NODE:.spec.nodeName"
```


1) Command to list pods running in which node and which availability zone: 
```
 kubectl get pods -o custom-columns="POD:metadata.name,NODE:spec.nodeName" | tail -n +2 | while read pod node; do
 echo -n "$pod $node "
 kubectl get node "$node" -o jsonpath="{.metadata.labels.topology\.kubernetes\.io/zone}"
 echo ""
 done
```

2) List of nodes and how many pods running on them:
```
kubectl get po -o json --all-namespaces | \
 jq '.items | group_by(.spec.nodeName) | map({"nodeName": .[0].spec.nodeName, "count": length}) | sort_by(.count)'
```
3) List pods using most of RAM and CPU:
For CPU:
```
kubectl top pods -A | sort --reverse --key 3 --numeric
```
For RAM:
```
kubectl top pods -A | sort --reverse --key 4 --numeric
```

4) Getting pods that are continuously restarting (sorting them):
```
kubectl get pods --all-namespaces -o json | jq -r '.items | sort_by(.status.containerStatuses[0].restartCount) | reverse[] | [.metadata.namespace, .metadata.name, .status.containerStatuses[0].restartCount] | @tsv' | column -t
```
5) Quickly check the pod limits:
```
kubectl get pods -o=custom-columns='NAME:spec.containers[*].name,MEMREQ:spec.containers[*].resources.requests.memory,MEMLIM:spec.containers[*].resources.limits.memory,CPUREQ:spec.containers[*].resources.requests.cpu,CPULIM:spec.containers[*].resources.limits.cpu'
```
6) Get all private IPs of nodes:
```
kubectl get nodes -o json | \
 jq -r '.items[].status.addresses[]? | select (.type == "InternalIP") | .address' | \
 paste -sd "\n" -
```
7) Checking logs: Read logs with human readable timestamp:
```
kubectl logs -f my-pod --timestamps
```
8. Logs of the pods, last 100 lines —tail
 
```
kubectl logs -f my-pod --tail=100
```
9) Check for events across all namespaces and filter for any errors,
```
kubectl get events --all-namespaces --field-selector type=Warning -o wide
or 
kubectl get events --all-namespaces --field-selector type!=Normal -o wide
```

--------
# Kubernetes Commands
--------
## 1. Cluster Information
- **View Cluster Information**:
  ```bash
  kubectl cluster-info
  ```
- **List All Nodes**:
  ```bash
  kubectl get nodes
  ```
- **Describe a Node**:
  ```bash
  kubectl describe node <node-name>
  ```

---

## 2. Pod Management
- **List All Pods**:
  ```bash
  kubectl get pods
  ```
- **List Pods in a Specific Namespace**:
  ```bash
  kubectl get pods -n <namespace>
  ```
- **View Pod Logs**:
  ```bash
  kubectl logs <pod-name>
  ```
- **View Logs for a Specific Container in a Pod**:
  ```bash
  kubectl logs <pod-name> -c <container-name>
  ```
- **Describe a Pod**:
  ```bash
  kubectl describe pod <pod-name>
  ```
- **Execute a Command in a Pod**:
  ```bash
  kubectl exec -it <pod-name> -- <command>
  ```
- **Delete a Pod**:
  ```bash
  kubectl delete pod <pod-name>
  ```

---

## 3. Deployment Management
- **List Deployments**:
  ```bash
  kubectl get deployments
  ```
- **Describe a Deployment**:
  ```bash
  kubectl describe deployment <deployment-name>
  ```
- **Scale a Deployment**:
  ```bash
  kubectl scale deployment <deployment-name> --replicas=<number>
  ```
- **Apply Changes from a YAML File**:
  ```bash
  kubectl apply -f <file.yaml>
  ```
- **Roll Back a Deployment**:
  ```bash
  kubectl rollout undo deployment <deployment-name>
  ```
- **View Deployment History**:
  ```bash
  kubectl rollout history deployment <deployment-name>
  ```

---

## 4. Service and Networking
- **List Services**:
  ```bash
  kubectl get svc
  ```
- **Describe a Service**:
  ```bash
  kubectl describe svc <service-name>
  ```
- **Port Forward a Service**:
  ```bash
  kubectl port-forward svc/<service-name> <local-port>:<service-port>
  ```

---

## 5. Namespace Management
- **List Namespaces**:
  ```bash
  kubectl get namespaces
  ```
- **Create a Namespace**:
  ```bash
  kubectl create namespace <namespace-name>
  ```
- **Delete a Namespace**:
  ```bash
  kubectl delete namespace <namespace-name>
  ```

---

## 6. Troubleshooting
- **List All Events**:
  ```bash
  kubectl get events
  ```
- **Check the Status of All Resources**:
  ```bash
  kubectl get all
  ```
- **Debug a Node**:
  ```bash
  kubectl describe node <node-name>
  ```
- **Debug a Pod**:
  ```bash
  kubectl describe pod <pod-name>
  ```

---

## 7. Resource Management
- **Get Resource Usage (using Metrics Server)**:
  ```bash
  kubectl top nodes
  kubectl top pods
  ```
- **Delete a Resource**:
  ```bash
  kubectl delete <resource-type> <resource-name>
  ```
- **Edit a Resource**:
  ```bash
  kubectl edit <resource-type> <resource-name>
  ```

---

## 8. Custom Resources and YAML Files
- **Validate a YAML File**:
  ```bash
  kubectl apply --dry-run=client -f <file.yaml>
  ```
- **Delete All Resources Defined in a File**:
  ```bash
  kubectl delete -f <file.yaml>
  ```
- **List Custom Resources (CRDs)**:
  ```bash
  kubectl get crd
  ```

---

## 9. Utility Commands
- **Switch Context**:
  ```bash
  kubectl config use-context <context-name>
  ```
- **View Current Context**:
  ```bash
  kubectl config current-context
  ```
- **List All Contexts**:
  ```bash
  kubectl config get-contexts
  ```


### kubernetes Objects

([Kubernetes object](Objects.md))