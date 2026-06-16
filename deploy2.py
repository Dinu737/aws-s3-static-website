import boto3

bucket_name = "dinesh-static-website-demo"

s3 = boto3.client("s3")

# Upload file
s3.upload_file(
    r"C:\Users\ghule\OneDrive\Desktop\index33.html",
    bucket_name,
    "index.html"
)

print("File Uploaded")

# Enable Static Website Hosting
website_configuration = {
    "IndexDocument": {
        "Suffix": "index.html"
    }
}

s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration=website_configuration
)

print("Website Hosting Enabled")

