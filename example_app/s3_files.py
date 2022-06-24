from boto3 import Session
from typing import Any, Dict

from django.conf import settings

def get_object_key_from_url(url: str) -> str:
    '''
    Returns the object key for the given url
    '''
    endpoint = settings.AWS_S3_ENDPOINT_URL
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    return url.split(f'{endpoint}/{bucket_name}/')[1]


def get_presigned_url(object_key: str) -> str:
    '''
    Returns a presigned URL for the given object key
    '''
    session = Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )
    s3client = session.client('s3')
    url = s3client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
            'Key': object_key,
        },
        ExpiresIn=settings.AWS_PRESIGNED_URL_EXPIRATION_TIME_MINUTES,
    )
    return url


def get_presigned_url_to_upload_file(object_key: str) -> Dict[str, Any]:
    '''
    Returns a dict with the necessary data to upload a file for the given key
    '''
    session = Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME,
    )
    s3client = session.client('s3')

    url = s3client.generate_presigned_post(
        Bucket=settings.AWS_STORAGE_BUCKET_NAME,
        Key=object_key,
        Fields={
            'acl': 'private',
        },
        Conditions=[
            {'acl': 'private'},
        ],
        ExpiresIn=settings.AWS_PRESIGNED_URL_EXPIRATION_TIME_MINUTES,
    )

    return url
