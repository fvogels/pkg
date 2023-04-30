import boto3
from botocore.config import Config
import os


class Backblaze:
    @staticmethod
    def from_environment_variables():
        endpoint_url = os.getenv('ENDPOINT_URL')
        key_id = os.getenv("KEY_ID")
        application_key = os.getenv('APPLICATION_KEY')
        return Backblaze(endpoint_url, key_id, application_key)

    def __init__(self, endpoint_url, key_id, application_key):
        self.__b2 = boto3.resource(
            service_name='s3',
            endpoint_url=endpoint_url,
            aws_access_key_id=key_id,
            aws_secret_access_key=application_key,
            config = Config(signature_version='s3v4')
        )

    def download_file(self, *, bucket, remote_name, local_path):
        self.__b2.Bucket(bucket).download_file(remote_name, local_path)

    def upload_file(self, *, bucket, local_path, remote_path):
        self.__b2.Bucket(bucket).upload_file(local_path, remote_path)
