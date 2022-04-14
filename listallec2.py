import boto3

AWS_REGION = "ap-south-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
l1=[]
instances = EC2_RESOURCE.instances.all()

for instance in instances:
    print(f'EC2 instance {instance.id}"')
    print(f'Instance state: {instance.state["Name"]}')
    print(f'Instance type: "{instance.instance_type}')
    print(f'Piblic IPv4 address: {instance.public_ip_address}')
    print('-'*30)
    l1.append(instance.id)
    
print('The total no of ec2 are in ths region:',len(l1))