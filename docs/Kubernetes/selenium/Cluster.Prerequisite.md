
# Keda Autoscaler 
    It is Important In-order to scale pods based on number of request present in selenium-grid queue.

####
        install https://keda.sh/ plugin  in kube
        helm repo add kedacore https://kedacore.github.io/charts
        kubectl create namespace keda   # [ Create only if Needed]
        helm install keda kedacore/keda --namespace keda  # [ Dont use Namspace     if selenium is running in default workspace]
        helm install -f values.yaml docker-selenium


#  Installing the Kubernetes Metrics Server

    https://docs.aws.amazon.com/eks/latest/userguide/metrics-server.html

    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml 
    
    kubectl get deployment metrics-server -n kube-system