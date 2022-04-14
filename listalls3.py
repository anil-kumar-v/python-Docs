import boto3

AWS_REGION = "ap-south-1"

client = boto3.client("s3", region_name=AWS_REGION)
l1=[]
response = client.list_buckets()

print("These are the below s3 buckets in this region:")
for bucket in response['Buckets']:
    print(f"--> {bucket['Name']}")
    l1.append(bucket['Name'])

print("The total no of s3 buckets are:",len(l1))