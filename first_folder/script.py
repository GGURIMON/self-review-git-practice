import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Boto3 세션을 명시적으로 설정
session = boto3.Session()

# S3 클라이언트 생성
s3 = session.client('s3')

bucket_name = 's3bucket-ggurimon'

try:
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        print(f"Bucket: {bucket_name} contains the following objects:")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f"Bucket: {bucket_name} is empty or does not exist.")

except NoCredentialsError:
    print("No credentials provided.")
except PartialCredentialsError:
    print("Incomplete credentials provided.")
except Exception as e:
    print(f"An error occurred: {e}")
