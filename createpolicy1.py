import boto3
import json
def create_iam_policy():
    # Create IAM client
    iam = boto3.client('iam')

    # Create a policy
    my_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "readonly:GetItem",
                    "readonly:Scan",
                ],
                "Resource": "*"
            }
        ]
    }
    result  = iam.create_policy(
        PolicyName='ReadOnly',
        PolicyDocument=json.dumps(my_policy)
    )
    print(result)

create_iam_policy()