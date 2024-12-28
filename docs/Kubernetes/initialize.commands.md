
Turn off swap complusory
kubeadm init --apiserver-advertise-address {public_ip_or_private_ip_for api server} --pod-network-cidr= {Docker_container_network_subnet}

Install network flannel
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
Change it in netowrk section for custom docker network subnet
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml


kubectl get nodes
kubectl get pods -n kube-system -o wide


# script -a log.txt   For session Logging