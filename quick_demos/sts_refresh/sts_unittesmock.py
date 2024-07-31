from unittest.mock import patch, MagicMock
import boto3

@patch('boto3.client')
def test_sts_assume_role(mock_boto_client):
    mock_sts = MagicMock()
    mock_boto_client.return_value = mock_sts

    mock_sts.assume_role.return_value = {
        'Credentials': {
            'AccessKeyId': 'FAKE_ACCESS_KEY',
            'SecretAccessKey': 'FAKE_SECRET_KEY',
            'SessionToken': 'FAKE_SESSION_TOKEN',
            'Expiration': '2023-01-01T00:00:00Z'
        }
    }

    sts_client = boto3.client('sts')
    response = sts_client.assume_role(
        RoleArn='arn:aws:iam::123456789012:role/example-role',
        RoleSessionName='example-session'
    )

    credentials = response['Credentials']
    access_key = credentials['AccessKeyId']
    secret_key = credentials['SecretAccessKey']
    session_token = credentials['SessionToken']

    print('Temporary Credentials:')
    print(f'Access Key: {access_key}')
    print(f'Secret Key: {secret_key}')
    print(f'Session Token: {session_token}')

test_sts_assume_role()
