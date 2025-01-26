from aws_cdk import (
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam,
    core as cdk
)

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ekscluster = eks.CfnCluster(
            self,
            "EKSCluster",
            name="seeding",
            role_arn=iamrole8.attr_arn,
            version="1.26",
            resources_vpc_config={
                "security_group_ids": [
                    "sg-044a1e970c2d60905"
                ],
                "subnet_ids": [
                    ec2subnet4.ref,
                    ec2subnet3.ref,
                    ec2subnet.ref,
                    ec2subnet2.ref
                ]
            },
            kubernetes_network_config={
                "service_ipv4_cidr": "10.100.0.0/16"
            }
        )

        eksnodegroup = eks.CfnNodegroup(
            self,
            "EKSNodegroup",
            nodegroup_name="se-1",
            cluster_name="seeding",
            version="1.25",
            release_version="1.25.11-20230711",
            scaling_config={
                "min_size": 1,
                "max_size": 1,
                "desired_size": 1
            },
            instance_types=[
                "t3.xlarge"
            ],
            subnets=[
                ec2subnet.ref,
                ec2subnet2.ref,
                ec2subnet3.ref,
                ec2subnet4.ref
            ],
            remote_access={
                "ec2_ssh_key": "784264783",
                "source_security_groups": [
                    "sg-005e0e4d4e9762b20"
                ]
            },
            ami_type="AL2_x86_64",
            node_role=iamrole3.attr_arn,
            labels={
                
            },
            disk_size=50,
            tags={
                "app": "seeding",
                "grid": "hub"
            },
            capacity_type="ON_DEMAND"
        )

        eksnodegroup2 = eks.CfnNodegroup(
            self,
            "EKSNodegroup2",
            nodegroup_name="Prometheus",
            cluster_name="seeding",
            version="1.26",
            release_version="1.26.6-20230711",
            scaling_config={
                "min_size": 1,
                "max_size": 1,
                "desired_size": 1
            },
            instance_types=[
                "t3.medium"
            ],
            subnets=[
                ec2subnet.ref,
                ec2subnet2.ref,
                ec2subnet3.ref,
                ec2subnet4.ref
            ],
            ami_type="AL2_x86_64",
            node_role=iamrole3.attr_arn,
            labels={
                "app": "prometheus-server"
            },
            disk_size=50,
            tags={
                
            },
            capacity_type="ON_DEMAND"
        )

        eksnodegroup3 = eks.CfnNodegroup(
            self,
            "EKSNodegroup3",
            nodegroup_name="se-hub2",
            cluster_name="seeding",
            version="1.26",
            release_version="1.26.6-20230711",
            scaling_config={
                "min_size": 2,
                "max_size": 2,
                "desired_size": 2
            },
            instance_types=[
                "t3.xlarge"
            ],
            subnets=[
                ec2subnet.ref,
                ec2subnet2.ref,
                ec2subnet3.ref,
                ec2subnet4.ref
            ],
            ami_type="AL2_x86_64",
            node_role=iamrole3.attr_arn,
            labels={
                
            },
            disk_size=50,
            tags={
                
            },
            capacity_type="ON_DEMAND"
        )

        eksaddon = eks.CfnAddon(
            self,
            "EKSAddon",
            addon_name="kube-proxy",
            addon_version="v1.25.6-eksbuild.1",
            cluster_name="seeding"
        )

        eksaddon2 = eks.CfnAddon(
            self,
            "EKSAddon2",
            addon_name="vpc-cni",
            addon_version="v1.12.2-eksbuild.1",
            cluster_name="seeding"
        )

        eksaddon3 = eks.CfnAddon(
            self,
            "EKSAddon3",
            addon_name="aws-ebs-csi-driver",
            addon_version="v1.17.0-eksbuild.1",
            cluster_name="seeding",
            service_account_role_arn=iamrole4.attr_arn
        )

        eksaddon4 = eks.CfnAddon(
            self,
            "EKSAddon4",
            addon_name="coredns",
            addon_version="v1.9.3-eksbuild.2",
            cluster_name="seeding"
        )

        eksaddon5 = eks.CfnAddon(
            self,
            "EKSAddon5",
            addon_name="kubecost_kubecost",
            addon_version="v1.102.2-eksbuild.0",
            cluster_name="seeding"
        )

        ec2vpc = ec2.CfnVPC(
            self,
            "EC2VPC",
            cidr_block="192.168.0.0/16",
            enable_dns_support=True,
            enable_dns_hostnames=True,
            instance_tenancy="default",
            tags=[
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/VPC"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                }
            ]
        )

        ec2subnet = ec2.CfnSubnet(
            self,
            "EC2Subnet",
            availability_zone=ec2subnet4.attr_availability_zone,
            cidr_block="192.168.64.0/19",
            vpc_id=ec2vpc.ref,
            map_public_ip_on_launch=False,
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "kubernetes.io/role/internal-elb",
                    "value": "1"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/SubnetPrivateUSEAST1A"
                }
            ]
        )

        ec2subnet2 = ec2.CfnSubnet(
            self,
            "EC2Subnet2",
            availability_zone=ec2subnet3.attr_availability_zone,
            cidr_block="192.168.96.0/19",
            vpc_id=ec2vpc.ref,
            map_public_ip_on_launch=False,
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "kubernetes.io/role/internal-elb",
                    "value": "1"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/SubnetPrivateUSEAST1C"
                }
            ]
        )

        ec2subnet3 = ec2.CfnSubnet(
            self,
            "EC2Subnet3",
            availability_zone="us-east-1c",
            cidr_block="192.168.32.0/19",
            vpc_id=ec2vpc.ref,
            map_public_ip_on_launch=True,
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "kubernetes.io/role/elb",
                    "value": "1"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/SubnetPublicUSEAST1C"
                }
            ]
        )

        ec2subnet4 = ec2.CfnSubnet(
            self,
            "EC2Subnet4",
            availability_zone="us-east-1a",
            cidr_block="192.168.0.0/19",
            vpc_id=ec2vpc.ref,
            map_public_ip_on_launch=True,
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "kubernetes.io/role/elb",
                    "value": "1"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/SubnetPublicUSEAST1A"
                }
            ]
        )

        ec2internetgateway = ec2.CfnInternetGateway(
            self,
            "EC2InternetGateway",
            tags=[
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/InternetGateway"
                }
            ]
        )

        ec2route = ec2.CfnRoute(
            self,
            "EC2Route",
            destination_cidr_block="0.0.0.0/0",
            gateway_id=ec2internetgateway.ref,
            route_table_id="rtb-0a2a39826d650a051"
        )

        ec2route2 = ec2.CfnRoute(
            self,
            "EC2Route2",
            destination_cidr_block="0.0.0.0/0",
            nat_gateway_id="nat-0d30361f4737bca6b",
            route_table_id="rtb-00a768445b228e0b5"
        )

        iamservicelinkedrole = iam.CfnServiceLinkedRole(
            self,
            "IAMServiceLinkedRole",
            a_w_s_service_name="eks.amazonaws.com",
            description="Allows Amazon EKS to call AWS services on your behalf."
        )

        iamservicelinkedrole2 = iam.CfnServiceLinkedRole(
            self,
            "IAMServiceLinkedRole2",
            a_w_s_service_name="eks-fargate.amazonaws.com",
            description="This policy grants necessary permissions to Amazon EKS to run fargate tasks"
        )

        iamservicelinkedrole3 = iam.CfnServiceLinkedRole(
            self,
            "IAMServiceLinkedRole3",
            a_w_s_service_name="eks-nodegroup.amazonaws.com",
            description="This policy allows Amazon EKS to create and manage Nodegroups"
        )

        iamservicelinkedrole4 = iam.CfnServiceLinkedRole(
            self,
            "IAMServiceLinkedRole4",
            a_w_s_service_name="autoscaling.amazonaws.com",
            description="Default Service-Linked Role enables access to AWS Services and Resources used or managed by Auto Scaling"
        )

        iamrole = iam.CfnRole(
            self,
            "IAMRole",
            path="/",
            role_name="AmazonEKSLoadBalancerControllerRole",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Federated\":\"arn:aws:iam::331911183167:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642\"},\"Action\":\"sts:AssumeRoleWithWebIdentity\",\"Condition\":{\"StringEquals\":{\"oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642:aud\":\"sts.amazonaws.com\",\"oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642:sub\":\"system:serviceaccount:kube-system:aws-load-balancer-controller\"}}}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::331911183167:policy/AWSLoadBalancerControllerIAMPolicy"
            ],
            description="",
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/iamserviceaccount-name",
                    "value": "kube-system/aws-load-balancer-controller"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.150.0-dev"
                }
            ]
        )

        iamrole2 = iam.CfnRole(
            self,
            "IAMRole2",
            path="/",
            role_name="AmazonEKSFargatePodExecutionRole",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"eks-fargate-pods.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
                "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy"
            ],
            description="Fragate eks Allows access to other AWS service resources that are required to run Amazon EKS pods on AWS Fargate."
        )

        iamrole3 = iam.CfnRole(
            self,
            "IAMRole3",
            path="/",
            role_name="AmazonEKSNodeRole",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"ec2.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
                "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
                "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
                "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
            ],
            description="selenium  Allows EC2 instances to call AWS services on your behalf."
        )

        iamrole4 = iam.CfnRole(
            self,
            "IAMRole4",
            path="/",
            role_name="AmazonEKS_EBS_CSI_Driver",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Federated\":\"arn:aws:iam::331911183167:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642\"},\"Action\":\"sts:AssumeRoleWithWebIdentity\",\"Condition\":{\"StringEquals\":{\"oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642:aud\":\"sts.amazonaws.com\",\"oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642:sub\":\"system:serviceaccount:kube-system:ebs-csi-controller-sa\"}}}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
            ],
            description=""
        )

        iamrole5 = iam.CfnRole(
            self,
            "IAMRole5",
            path="/",
            role_name="eksctl-seed-cluster-FargatePodExecutionRole-14HFYWHZ436L",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"eks-fargate-pods.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            description="",
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seed"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seed"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seed-cluster/FargatePodExecutionRole"
                }
            ]
        )

        iamrole6 = iam.CfnRole(
            self,
            "IAMRole6",
            path="/",
            role_name="eksctl-seeding-cluster-FargatePodExecutionRole-1C9PZUE018248",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"eks-fargate-pods.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/AmazonEKSFargatePodExecutionRolePolicy"
            ],
            description="",
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/FargatePodExecutionRole"
                }
            ]
        )

        iamrole7 = iam.CfnRole(
            self,
            "IAMRole7",
            path="/",
            role_name="eksClusterRole",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"eks.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/AdministratorAccess",
                "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
                "arn:aws:iam::aws:policy/job-function/NetworkAdministrator",
                "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
            ],
            description="seeding Allows access to other AWS service resources that are required to operate clusters managed by EKS."
        )

        iamrole8 = iam.CfnRole(
            self,
            "IAMRole8",
            path="/",
            role_name="eksctl-seeding-cluster-ServiceRole-1JCJBVAEJHHNK",
            assume_role_policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"eks.amazonaws.com\"},\"Action\":\"sts:AssumeRole\"}]}",
            max_session_duration=3600,
            managed_policy_arns=[
                "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess",
                "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
                "arn:aws:iam::aws:policy/AmazonElasticContainerRegistryPublicFullAccess",
                "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
            ],
            description="",
            tags=[
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "eksctl.cluster.k8s.io/v1alpha1/cluster-name",
                    "value": "seeding"
                },
                {
                    "key": "alpha.eksctl.io/cluster-oidc-enabled",
                    "value": "false"
                },
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.133.0"
                },
                {
                    "key": "Name",
                    "value": "eksctl-seeding-cluster/ServiceRole"
                }
            ]
        )

        iampolicy = iam.CfnPolicy(
            self,
            "IAMPolicy",
            policy_document='''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ecr:*",
            "Resource": "*"
        }
    ]
}

''',
            roles=[
                iamrole2.ref
            ],
            policy_name="fargate-ecr-image-access"
        )

        iampolicy2 = iam.CfnPolicy(
            self,
            "IAMPolicy2",
            policy_document='''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
''',
            roles=[
                iamrole7.ref
            ],
            policy_name="eksctl-seed-cluster-PolicyCloudWatchMetrics"
        )

        iampolicy3 = iam.CfnPolicy(
            self,
            "IAMPolicy3",
            policy_document='''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeAddresses",
                "ec2:DescribeInternetGateways"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
''',
            roles=[
                iamrole7.ref
            ],
            policy_name="eksctl-seed-cluster-PolicyELBPermissions"
        )

        iampolicy4 = iam.CfnPolicy(
            self,
            "IAMPolicy4",
            policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Action\":[\"cloudwatch:PutMetricData\"],\"Resource\":\"*\",\"Effect\":\"Allow\"}]}",
            roles=[
                iamrole8.ref
            ],
            policy_name="eksctl-seeding-cluster-PolicyCloudWatchMetrics"
        )

        iampolicy5 = iam.CfnPolicy(
            self,
            "IAMPolicy5",
            policy_document="{\"Version\":\"2012-10-17\",\"Statement\":[{\"Action\":[\"ec2:DescribeAccountAttributes\",\"ec2:DescribeAddresses\",\"ec2:DescribeInternetGateways\"],\"Resource\":\"*\",\"Effect\":\"Allow\"}]}",
            roles=[
                iamrole8.ref
            ],
            policy_name="eksctl-seeding-cluster-PolicyELBPermissions"
        )

        iamoidcprovider = iam.CfnOIDCProvider(
            self,
            "IAMOIDCProvider",
            url="oidc.eks.us-east-1.amazonaws.com/id/4F04C6B4BC8878C105E17AD58ACEF642",
            client_id_list=[
                "sts.amazonaws.com"
            ],
            thumbprint_list=[
                "9e99a48a9960b14926bb7f3b02e22da2b0ab7280"
            ],
            tags=[
                {
                    "key": "alpha.eksctl.io/eksctl-version",
                    "value": "0.149.0-dev"
                },
                {
                    "key": "alpha.eksctl.io/cluster-name",
                    "value": "seeding"
                }
            ]
        )


app = cdk.App()
MyStack(app, "my-stack-name", env={'region': 'us-east-1'})
app.synth()
