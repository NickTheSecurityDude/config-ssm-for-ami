##############################################################
#
# config_stack.py
#
# Resources:
#
#
##############################################################

from aws_cdk import (
  aws_config as config,
  core
)

import boto3

class ConfigStack(core.Stack):

  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    ssm_client = boto3.client('ssm')

    ami_id_param="/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
    response = ssm_client.get_parameter(
      Name=ami_id_param
    )
    ami_id=response['Parameter']['Value']

    config.ManagedRule(self,"Config AMI Rule",
      identifier="APPROVED_AMIS_BY_ID",
      input_parameters={'amiIds':ami_id},
      rule_scope=config.RuleScope.from_tag(
        key='ami_id_parameter',
        value='/linux/production/ami_id'
      )

    )
    
