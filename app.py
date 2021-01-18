#!/usr/bin/env python3

from aws_cdk import core

import boto3
import sys

client = boto3.client('sts')

region=client.meta.region_name

#if region != 'us-east-1':
#  print("This app may only be run from us-east-1")
#  sys.exit()

account_id = client.get_caller_identity()["Account"]

my_env = {'region': region, 'account': account_id}

from stacks.ssm_stack import SSMStack
from stacks.config_stack import ConfigStack

proj_name="ssm-config"

app = core.App()

ssm_stack=SSMStack(app, proj_name+"-ssm",env=my_env)
config_stack=ConfigStack(app,proj_name+"-config")

app.synth()
