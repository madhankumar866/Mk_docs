  
### Get the secret for admin
  k get secret argocd-initial-admin-secret -n argocd -o yaml
### Decode it 
  echo NVVTSUlSVUJtV0JiZ015eg== | base64 --decode
  k get svc -n argocd
### Login into argocd using cli
  argocd login localhost:8080
  argocd app list
  argocd login --help


## Service port forward
  kubectl port-forward svc/argocd-server -n argocd 8080:443
### List the port and kill it.  
  lsof -i:8080
  kill -9 98320
