import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('sagemaker', region_name="us-west-2")

    response = client.create_presigned_domain_url(
        DomainId='d-1234567890abcdef0',
        UserProfileName='John Doe',
        SessionExpirationDurationInSeconds=43200,
        ExpiresInSeconds=5
    )

    return {
        'statusCode': 302,
        'headers': {
            'Location': response['AuthorizedUrl']
        }
    }
