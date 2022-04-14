import boto3
import json
def detach_user_policy(username, policy_arn):
    iam = boto3.resource("iam")
    attached_policy = iam.Policy(policy_arn)
    response = attached_policy.detach_user(
        UserName=username
    )
    print(response)
detach_user_policy(username="TrustedAdvisor", policy_arn="arn:aws:iam::151439720941:user/TrustedAdvisor")
#detach_user_policy(username="A2", policy_arn="arn:aws:iam::151439720941:policy/cactus")