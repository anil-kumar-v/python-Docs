import boto3
def add_user_to_group(username, group_name):
    iam = boto3.client('iam') # IAM low level client object
    response = iam.add_user_to_group(
        UserName=username,
        GroupName=group_name
    )
    print(response)
add_user_to_group(username="A1", group_name="Dushmans")
add_user_to_group(username="A2", group_name="Dushmans")