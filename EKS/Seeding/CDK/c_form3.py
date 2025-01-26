from aws_cdk import (
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam,
    core as cdk
)

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        self.create_eks_cluster()

    def create_eks_cluster(self):
        vpc = self.create_vpc()
        eks_role = self.create_eks_service_role()

        cluster = eks.CfnCluster(
            self,
            "EKSCluster",
            name="seeding",
            role_arn=eks_role.attr_arn,
            version="1.26",
            resources_vpc_config={
                "security_group_ids": ["sg-044a1e970c2d60905"],
                "subnet_ids": [subnet.ref for subnet in vpc.private_subnets]
            },
            kubernetes_network_config={
                "service_ipv4_cidr": "10.100.0.0/16"
            }
        )

        self.create_eks_nodegroup("se-1", cluster, vpc.private_subnets, "t3.xlarge", "1.25")
        self.create_eks_nodegroup("Prometheus", cluster, vpc.private_subnets, "t3.medium", "1.26")
        self.create_eks_nodegroup("se-hub2", cluster, vpc.private_subnets, "t3.xlarge", "1.26")

        self.create_eks_addon("kube-proxy", "v1.25.6-eksbuild.1", cluster)
        self.create_eks_addon("vpc-cni", "v1.12.2-eksbuild.1", cluster)
        self.create_eks_addon("aws-ebs-csi-driver", "v1.17.0-eksbuild.1", cluster, iamrole4.attr_arn)
        self.create_eks_addon("coredns", "v1.9.3-eksbuild.2", cluster)
        self.create_eks_addon("kubecost_kubecost", "v1.102.2-eksbuild.0", cluster)

    def create_vpc(self):
        return ec2.Vpc(
            self,
            "EKSVpc",
            cidr="192.168.0.0/16",
            max_azs=2,
            nat_gateways=1,
            enable_dns_support=True,
            enable_dns_hostnames=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public",
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name="Private",
                    cidr_mask=24
                )
            ]
        )

    def create_eks_service_role(self):
        return iam.CfnRole(
            self,
            "EKSServiceRole",
            path="/",
            role_name="EKSServiceRole",
            assume_role_policy_document={
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {"Service": "eks.amazonaws.com"},
                        "Action": "sts:AssumeRole"
                    }
                ]
            }
        )

    def create_eks_nodegroup(self, name, cluster, subnets, instance_type, version):
        eks.CfnNodegroup(
            self,
            f"EKSNodegroup{name}",
            nodegroup_name=name,
            cluster_name=cluster.name,
            version=version,
            scaling_config={
                "min_size": 1,
                "max_size": 1,
                "desired_size": 1
            },
            instance_types=[instance_type],
            subnets=[subnet.ref for subnet in subnets],
            ami_type="AL2_x86_64",
            disk_size=50,
            capacity_type="ON_DEMAND"
        )

    def create_eks_addon(self, name, version, cluster, role_arn=None):
        eks.CfnAddon(
            self,
            f"EKSAddon{name}",
            addon_name=name,
            addon_version=version,
            cluster_name=cluster.name,
            service_account_role_arn=role_arn
        )

app = cdk.App()
MyStack(app, "my-stack-name", env={'region': 'us-east-1'})
app.synth()
