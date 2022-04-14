#import the library and config module.
import boto3 
from botocore.config import Config
region = "ap-south-1"
#declare the config.
config = Config( 
             region_name = "ap-south-1",
             signature_version = 'v4',
             retries = {
                 'max_attempts': 10,
                 'mode': 'standard'
             }
         )
#initialize boto3 client for ec2 with the config object.
ec2 = boto3.client('ec2', config = config)
instances = ['i-0464dc5fd236d07b6'] # or ["<instance-id-1>","<instance-id-2>",...,"<instance-id-n>"]
#start the instance
#ec2.start_instances(InstanceIds=instances)
#stop the instance
#ec2.stop_instances(InstanceIds=instances)
#reboot the instance
ec2.reboot_instances(InstanceIds=instances)