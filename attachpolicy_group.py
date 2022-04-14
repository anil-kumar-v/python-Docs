import boto3
import json
def attach_group_policy(policy_arn, group_name):
    iam = boto3.client("iam")
    response = iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    print(response)

attach_group_policy(policy_arn="arn:aws:iam::151439720941:policy/cactus", group_name="Dushmans")
attach_group_policy(policy_arn="arn:aws:iam::151439720941:policy/cactus", group_name="Believers")

