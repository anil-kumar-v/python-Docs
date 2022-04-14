import boto3
a=boto3.client("AWS")
response= boto3.client.describe_regions()
print("These are the regions in AWS ",response)