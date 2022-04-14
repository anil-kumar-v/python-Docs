import boto3
import json
def list_policies():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_policies')
    for response in paginator.paginate(Scope="Local"):
        for policy in response["Policies"]:
            print(f"Policy Name: {policy['PolicyName']} ARN: {policy['Arn']}")

list_policies()