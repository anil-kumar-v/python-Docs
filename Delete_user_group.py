"Before we can delete an IAM user, we need to detach any IAM policies attached to the user as well as remove the user from any groups they are in."

import boto3
def delete_user(username):
    # Create IAM client
    iam = boto3.client('iam')

    # Delete a user
    response = iam.delete_user(
        UserName=username
    )
    print(response)

delete_user(username="ekanath")