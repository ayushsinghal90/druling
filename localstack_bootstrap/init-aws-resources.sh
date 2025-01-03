#!/usr/bin/env bash

set -euo pipefail

# enable debug
# set -x

echo "configuring AWS resources"
echo "=========================="
LOCALSTACK_HOST=localhost
AWS_REGION=ap-south-1

# Function to check if LocalStack is running
wait_for_localstack() {
    echo "Waiting for LocalStack to be ready..."
    until curl -s "http://${LOCALSTACK_HOST}:4566" > /dev/null; do
        echo -n "."
        sleep 2
    done
    echo "LocalStack is ready!"
}

create_s3_bucket() {
    local S3_BUCKET_NAME=$1
    awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 s3api create-bucket --bucket ${S3_BUCKET_NAME} --region ${AWS_REGION} --create-bucket-configuration LocationConstraint=${AWS_REGION}

    # Apply CORS configuration to the bucket
    aws --endpoint-url=http://localhost:4566 s3api put-bucket-cors \
      --bucket druling-menus \
      --cors-configuration '{
        "CORSRules": [
          {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
            "AllowedOrigins": ["*"],
            "ExposeHeaders": [],
            "MaxAgeSeconds": 3000
          }
        ]
      }'
}

# Wait for LocalStack to be ready
wait_for_localstack

# Create S3 buckets
create_s3_bucket "druling-menus"
create_s3_bucket "druling-restaurants"