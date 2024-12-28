from aws_cdk import (
    aws_eks as eks,
    core as cdk
)

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        region = self.region
        cluster_name = "seeding"
        node_role_arn = f"arn:aws:iam::{self.account}:role/AmazonEKSNodeRole"

        subnet_ids = [
            "subnet-074b20489ec871f49",
            "subnet-0857a5df8524ba123",
            "subnet-0377bf26f064cb8b4",
            "subnet-022080e2e17c47186"
        ]

        eks.CfnCluster(
            self,
            "EKSCluster",
            name=cluster_name,
            role_arn=f"arn:aws:iam::{self.account}:role/eksctl-{cluster_name}-ServiceRole-1JCJBVAEJHHNK",
            version="1.26",
            resources_vpc_config={
                "security_group_ids": ["sg-044a1e970c2d60905"],
                "subnet_ids": subnet_ids
            },
            kubernetes_network_config={"service_ipv4_cidr": "10.100.0.0/16"}
        )

        nodegroup_props = {
            "version": "1.26",
            "release_version": "1.26.6-20230711",
            "instance_types": ["t3.xlarge"],
            "subnets": subnet_ids,
            "ami_type": "AL2_x86_64",
            "node_role": node_role_arn,
            "disk_size": 50,
            "capacity_type": "ON_DEMAND"
        }

        eks.CfnNodegroup(self, "EKSNodegroup1", nodegroup_name="se-hub2", cluster_name=cluster_name, **nodegroup_props)

        nodegroup_props.update(
            {
                "nodegroup_name": "Prometheus",
                "min_size": 1,
                "max_size": 1,
                "desired_size": 1,
                "instance_types": ["t3.medium"],
                "labels": {"app": "prometheus-server"}
            }
        )
        eks.CfnNodegroup(self, "EKSNodegroup2", cluster_name=cluster_name, **nodegroup_props)

        nodegroup_props.update(
            {
                "nodegroup_name": "se-1",
                "version": "1.25",
                "release_version": "1.25.11-20230711",
                "min_size": 1,
                "max_size": 1,
                "desired_size": 1,
                "instance_types": ["t3.xlarge"],
                "remote_access": {"ec2_ssh_key": "784264783", "source_security_groups": ["sg-005e0e4d4e9762b20"]},
                "labels": {},
                "tags": {"app": "seeding", "grid": "hub"}
            }
        )
        eks.CfnNodegroup(self, "EKSNodegroup3", cluster_name=cluster_name, **nodegroup_props)

        eks.CfnAddon(self, "EKSAddon1", addon_name="coredns", addon_version="v1.9.3-eksbuild.2", cluster_name=cluster_name)
        eks.CfnAddon(self, "EKSAddon2", addon_name="vpc-cni", addon_version="v1.12.2-eksbuild.1", cluster_name=cluster_name)
        eks.CfnAddon(self, "EKSAddon3", addon_name="kubecost_kubecost", addon_version="v1.102.2-eksbuild.0", cluster_name=cluster_name)
        eks.CfnAddon(self, "EKSAddon4", addon_name="kube-proxy", addon_version="v1.25.6-eksbuild.1", cluster_name=cluster_name)
        eks.CfnAddon(self, "EKSAddon5", addon_name="aws-ebs-csi-driver", addon_version="v1.17.0-eksbuild.1", cluster_name=cluster_name, service_account_role_arn="arn:aws:iam::331911183167:role/AmazonEKS_EBS_CSI_Driver")

app = cdk.App()
MyStack(app, "my-stack-name", env={'region': 'us-east-1'})
app.synth()
