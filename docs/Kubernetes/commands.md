
# connect to existing Cluster

### To update existing kubectl cluster To local kubeconfig For Connecting
```bash
  aws eks update-kubeconfig --name <cluster-name> --profile 
  ```
  ```bash
  aws eks update-kubeconfig --name seeding --profile seeding --region us-east-1
```

### To Get Service
```bash
  kubectl get svc
```
```bash
  eksctl create cluster --name selenium --region ap-south-1
  ```
  ```bash
  eksctl create cluster "selenium" --zones us-east-1a,us-east-1b,us-east-1c,us-east-1d,us-east-1f
  ```
  ```bash
  eksctl register cluster --name selenium --provider other --region us-east-1
  ```
```bash
  aws eks update-kubeconfig --region us-east-1 --name selenium
```

### To delete existing kubectl config
```bash
  rm ~/.kube/config

  helm install selenium-grid docker-selenium/selenium-grid
  kubectl get all -n selenium-grid
  kubectl get services
```
### To connect to internal network using busybox
```bash
  kubectl run -i --tty busybox --image=busybox --restart=Never -- sh
```
### For centos pod
```bash
  kubectl run -i --tty centos --image=centos --restart=Never -- sh
```


### To get all resource details
```bash
  kubectl get all
```
### To delete the deployment
```bash
  kubectl delete deployments -l app=selenium-edge-node
```
### To Describe Events In Running Pods
```bash
  kubectl describe pods -l app=selenium-chrome-node | grep Events -A4
```

### To Force Delete A Pod
```bash
  kubectl delete pod selenium-chrome-node --grace-period=0 --force
  kubectl delete pod selenium-edge-node --grace-period=0 --force
  kubectl delete pod selenium-firefox-node --grace-period=0 --force
  kubectl delete pod selenium-hub-c6c94c6c4-h558k --grace-period=0 --force
```
### To get status of kube system
```bash
  kubectl get pods -n=kube-system | grep coredns
```

### To scale pod replicaset
```bash
  kubectl scale --replicas=5 replicaset/selenium-chrome-node-7bf4f8dc77
  kubectl scale deployment.apps/selenium-node-chrome-node --replicas=1
```
### scale deployment
```bash
  kubectl scale deployment/selenium-chrome-node --replicas=2
```
### To get the value replicaset
```bash
  kubectl get rs selenium-chrome-node-5f44bffc9b -o jsonpath="{.status.replicas} {.status.availableReplicas}"
```

### To get replica status
```bash
  kubectl get rs
```
### Run the following command to forward a local port to the service:
```bash
  kubectl port-forward service/selenium-hub 4444:4444
```

### To get running resource to yaml
```bash
  crd = CustomResourceDefinition 
  rs  = replicaset
  kubectl get crd <CRD-NAME> -o yaml
```
### If CRD unable to Delete remove the crd using kubectl edit

  link-to-delete-crd[https://learn.microsoft.com/en-us/answers/questions/602466/custom-crds-not-getting-deleted-in-aks-cluster-how]
```bash
  kubectl edit crd crd-name   #  Remove finalizers from it and save
```


# eks cluster with command 
#### working with fargate,image is downloading & running
```bash
 eksctl create cluster --name seeding --region us-east-1 --version 1.26 --fargate --profile
```
 seeding
   Next:
      allow 80 port in security group for loadbalancer access


### To get metric server
```bash
  kubectl get --raw "/apis/external.metrics.k8s.io/v1beta1"
```
### To Find which Namespce if metric in
```bash
  kubectl get scaledobject selenium-chrome-scaledobject -n default -o jsonpath={.status.externalMetricNames}
```
###  describe scaledobject
```bash
  kubectl describe scaledobject
```
### To create node group
```bash
  eksctl create nodegroup --cluster=seeding \
  --name=node2 \
  --node-type=c5.2xlarge \
  --nodes=3 \
  --nodes-min=3 \
  --nodes-max=3 \
  --node-volume-size=20 \
  --ssh-access \
  --ssh-public-key=6548652153 \
  --managed \
  --region ap-south-1 
  ```


### To delete node group
```bash
  eksctl delete nodegroup --cluster=seeding --region ap-south-1
  eksctl delete --cluster=seeding --region ap-south-1
```
###  To Proxypass service
```bash
  kubectl --namespace monitoring port-forward svc/prometheus-k8s 9090

  kubectl kubernetes port-forward service/kubernetes 9090
```

### To connect to ssh to pod
```bash
  kubectl exec --stdin --tty busybox -- /bin/bash
  kubectl exec --it  busybox -n namespace -- /bin/bash
```
# Field selector 
### To delete all pods 
### Getting Specific Evicted is not working
```bash
kubectl delete pods --field-selector status.phase=Failed
```


```bash
kubectl logs -n {namespace}  (podname) --tail=100
```

### If above not working using --previous=false

```bash
kubectl logs -p dbc-ddl-service-ddc4cf6f9-6dqx8 -n {namespace} --previous=false --tail=50
```

```bash
kubectl logs -p (podname)  --since=30m --timestamps	
```

```bash
k get events -n {namespace} --field-selector involvedobject.name={pod_name} --sort-by='.metadata.creationTimestamp'
```


```bash
k describe pod {pod_name} -n {namespace}
```

###  Get the count of the pods
```bash
kubectl get pods -n {namespace} | grep "dbc-ddl-service" | wc -l
```
### scale replica
```bash
kubectl scale  deployment mysql --replicas=3
```

### Delete pods where status is Evicted
```bash
kubectl delete pod $(kubectl get pods  --field-selector=status.phase=Failed -o jsonpath='{.items[?(@.status.reason=="Evicted")].metadata.name}')
```

### rollout deployment
```bash
kubectl rollout restart deployment {podname} -n lifion
```
### get_the status of container_restart count
```bash
kubectl get pods --sort-by='.status.containerStatuses[0].restartCount'
```