import boto3

bucket_name = "dinesh-static-website-demo"

s3 = boto3.client("s3")

# Create Bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("Bucket Created")
