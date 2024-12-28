# Kube basics

 ## Service Account In Kubernetes
 'https://medium.com/the-programmer/working-with-service-account-in-kubernetes-df129cb4d1cc'
 https://www.cncf.io/blog/2019/05/10/kubernetes-core-concepts/

 Service Account: It is used to authenticate machine level processes to get access to our Kubernetes cluster. The API server is responsible for such authentication to the processes running in the pod.



 For Example:
    An application like Prometheus accessing the cluster to monitor it is a type of service account

    So,

    A service account is an identity that is attached to the processes running within a pod.



When you create a pod, if you do not specify a service account, it is automatically assigned the default service account in the same namespace.


Case 1:

     My Web Page which has a list of items to be displayed, this data needs to be fetched from an API server hosted in the Kubernetes cluster as shown above in the figure. To do so, we need to a service account that will be enabled by cluster API servers to authenticate and access the data from the cluster servers.

    

![Image title](https://miro.medium.com/max/640/1*sZlfKN3mTd2YxubbSaR24w.webp){ loading=lazy }


# helm chart
the package manager for Kubernetes
Helm allows you to add variables and use functions inside your template files. This makes it perfect for scalable applications that'll eventually need to have their parameters changed.


# Three Big Concepts
A Chart is a Helm package. It contains all of the resource definitions necessary to run an application, tool, or service inside of a Kubernetes cluster. Think of it like the Kubernetes equivalent of a Homebrew formula, an Apt dpkg, or a Yum RPM file.

A Repository is the place where charts can be collected and shared. It's like Perl's CPAN archive or the Fedora Package Database, but for Kubernetes packages.

A Release is an instance of a chart running in a Kubernetes cluster. One chart can often be installed many times into the same cluster. And each time it is installed, a new release is created. Consider a MySQL chart. If you want two databases running in your cluster, you can install that chart twice. Each one will have its own release, which will in turn have its own release name.

With these concepts in mind, we can now explain Helm like this:

Helm installs charts into Kubernetes, creating a new release for each installation. And to find new charts, you can search Helm chart repositories.



# 'helm install': Installing a Package
To install a new package, use the helm install command. At its simplest, it takes two arguments: A release name that you pick, and the name of the chart you want to install.



# resource limit
https://sysdig.com/blog/kubernetes-limits-requests/