#TODO   VPC Peering
        

#TODO   Helm Chart
        Download helm chart
        remove other edge&firefox&node's from helm chart

        check this repo for scaling pods {
            https://github.com/SeleniumHQ/docker-selenium/issues/1688
            https://github.com/prashanth-volvocars/docker-selenium/blob/auto-scaling/charts/selenium-grid/values.yaml
            }

#TODO   kube  ok
        
#TODO        
# Keda 
## selenium autoscaler 
        install https://keda.sh/ plugin  in kube
        helm repo add kedacore https://kedacore.github.io/charts
        kubectl create namespace keda
        helm install keda kedacore/keda --namespace keda
        helm install -f values.yaml docker-selenium


#NOTES
        try graphql  or /status

#Autoscaling
        pods are scale-in and scale-out by keda,
        nodes are scaled out and scaled-in by autoscaling group by aws
        By how individual grid isolated components scale's by default it have only 1 replica enabled in helm
        Increase resource size for pod's

