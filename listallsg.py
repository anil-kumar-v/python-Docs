import boto3

AWS_REGION = "ap-south-1"
EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION)
l1=[]
security_groups = EC2_RESOURCE.security_groups.all()

print('These are the below Security Groups in this region:')

for security_group in security_groups:
    print(f'{security_group.id}')
    l1.append(security_group.id)
    
print('The total no of Security Groups are :',len(l1))