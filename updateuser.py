import boto3
import sys
def update_user(old_user_name , new_user_name):
    iam = boto3.client('iam')
    # Update a user name
    response = iam.update_user(
        UserName=old_user_name,
        NewUserName=new_user_name
    )
    print(response)
update_user("Anil","Kumar")