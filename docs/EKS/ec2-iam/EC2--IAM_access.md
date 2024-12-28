

# Cross Account Access Policy.

## IN MASTER ACCOUNT A

    Add Required Policies to Roles

    Inline Policy   

    === "Role Name: Mk-ec2"
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "sts:AssumeRole",
                    "Resource": "arn:aws:iam::331911183167:role/Mk-ec2-policy"
                }
            ]
        }
        ```

    Trusted entities

    === "Trusted entities"
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        ```        


## IN SLAVE ACCOUNT B


    Add Required Policies to Roles

    Trusted entities

    === "Trusted entities"
        ```
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::362778997593:role/Mk-ec2"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }    
        ```        

## To Add It in aws config file location

    Add content in .aws/config  if fole is not Present create it.
    
    === "Trusted entities"
        ```
        [profile seeding]
        role_arn = arn:aws:iam::331911183167:role/Mk-ec2-policy
        credential_source = Ec2InstanceMetadata
        ```
## Run Commands to update Profile creditionals to ec2

    aws sts get-caller-identity --profile seeding



## To Allow EKS access to this Profile 

    ![Eks cluster using iam Referenced url](https://antonputra.com/kubernetes/add-iam-user-and-iam-role-to-eks/#add-iam-user-to-eks-cluster)

    If You create a Cluster using IAM User You Don't Need to do this,
    If You have accessing using Role without user, use this Below Method.

    === ""
        ``` bash
        aws eks update-kubeconfig --region us-east-1 --name seeding --profile seeding        

        kubectl edit -n kube-system configmap/aws-auth

        ...
        mapUsers: |
            - rolearn: arn:aws:iam::331911183167:role/Mk-ec2-policy
            username: Mk-ec2-policy
            groups:
            - system:masters
        ...

        ```
        apiVersion: v1
        data:
        mapRoles: |
          - groups:
            - system:bootstrappers
            - system:nodes
            rolearn: arn:aws:iam::331911183167:role/AmazonEKSNodeRole
            username: system:node:{{EC2PrivateDNSName}}
          - groups:
            - system:bootstrappers
            - system:nodes
            - system:node-proxier
            rolearn: arn:aws:iam::331911183167:role/AmazonEKSFargatePodExecutionRole
            username: system:node:{{SessionName}}
          - rolearn: arn:aws:iam::331911183167:role/Mk-ec2-policy
            username: Mk-ec2-policy
            groups:
            - system:masters

        ```


        aws eks update-kubeconfig \
        --region us-east-1 \
        --name seeding \
        --profile seeding
        ```