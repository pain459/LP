# Install localstack $ pip install localstack

import boto3

# Configure Boto3 to use LocalStack
boto3.setup_default_session()
sts_client = boto3.client('sts', endpoint_url='http://localhost:4566', region_name='us-east-1')

response = sts_client.assume_role(
    RoleArn='arn:aws:iam::123456789012:role/example-role',
    RoleSessionName='example-session'
)

credentials = response['Credentials']
access_key = credentials['AccessKeyId']
secret_key = credentials['SecretAccessKey']
session_token = credentials['SessionToken']

s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    aws_session_token=session_token,
    endpoint_url='http://localhost:4566'
)

response = s3_client.list_buckets()
print('Buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')
