import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# S3 클라이언트 생성
s3 = boto3.client('s3')

# 나열할 S3 버킷의 이름
bucket_name = 'your-bucket-name'

try:
    # S3 버킷의 객체 목록을 가져오기
    response = s3.list_objects_v2(Bucket=bucket_name)

    # S3 버킷에 객체가 있는지 확인
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
