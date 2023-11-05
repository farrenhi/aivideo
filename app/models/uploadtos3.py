import boto3
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
from models.model import *

# Initialize S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id = os.getenv('s3_access'),
    aws_secret_access_key = os.getenv('s3_secret'),
)

def upload_to_s3_and_get_cloudfront_link(local_file_path, filename, request_id):
    cloudfront_distribution_domain = os.getenv('cloudfront_distribution_domain')

    # Upload the file to S3
    s3.upload_file(local_file_path, 'login-aws-docker', filename)

    # Generate CloudFront link
    cloudfront_link = generate_cloudfront_link(cloudfront_distribution_domain, filename)
    videolink_to_sql(request_id, cloudfront_link) 
    
    return cloudfront_link

def generate_cloudfront_link(cloudfront_domain, filename):
    return f"https://{cloudfront_domain}/{filename}"


