import boto3
import json
def attach_user_policy(policy_arn, username):
    iam = boto3.client("iam")
    response = iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    print(response)

attach_user_policy(policy_arn="arn:aws:iam::aws:policy/ReadOnlyAccess",username="A1")
attach_user_policy(policy_arn="arn:aws:iam::aws:policy/ReadOnlyAccess",username="A2")
attach_user_policy(policy_arn="arn:aws:iam::aws:policy/ReadOnlyAccess",username="A3")
