import boto3

def upload_to_s3(file_name, bucket_name, object_name=None):
    """Uploads a file to an AWS S3 bucket."""
    s3 = boto3.client("s3")
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"Uploaded {file_name} to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    upload_to_s3("data/transactions.csv", "your-bucket-name")
