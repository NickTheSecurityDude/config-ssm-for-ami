##############################################################
#
# ssm_stack.py
#
# Resources:
#
#
##############################################################

from aws_cdk import (
  aws_ssm as ssm,
  core
)

import boto3

class SSMStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    ssm_client = boto3.client('ssm')

    ami_id_param="/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
    response = ssm_client.get_parameter(
      Name=ami_id_param
    )
    ami_id=response['Parameter']['Value']

    ssm.StringParameter(self,"Linux Prod AMI ID",
      parameter_name="/linux/production/ami_id",
      string_value=ami_id
    )