#

kubectl get - list resources
kubectl describe - show detailed information about a resource
kubectl logs - print the logs from a container in a pod
kubectl exec - execute a command on a container in a pod
You can use these commands to see when applications were deployed, what their current statuses are, where they are running and what their configurations are.

# Every Kubernetes Node runs at least:

Kubelet, a process responsible for communication between the Kubernetes control plane and the Node; it manages the Pods and the containers running on a machine.
A container runtime (like Docker) responsible for pulling the container image from a registry, unpacking the container, and running the application.


# To login into pod 
kubectl exec -ti $POD_NAME -- bash

# To scale a application 
kubectl scale deployments/kubernetes-bootcamp --replicas=4

# To get details of scaled pods
kubectl get pods -o wide