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

# Function to check if bucket exists
bucket_exists() {
    local S3_BUCKET_NAME=$1
    if awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 s3api head-bucket --bucket ${S3_BUCKET_NAME} 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

create_s3_bucket() {
    local S3_BUCKET_NAME=$1

    if bucket_exists ${S3_BUCKET_NAME}; then
        echo "Bucket ${S3_BUCKET_NAME} already exists"
    else
        echo "Creating bucket ${S3_BUCKET_NAME}"
        awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 s3api create-bucket \
            --bucket ${S3_BUCKET_NAME} \
            --region ${AWS_REGION} \
            --create-bucket-configuration LocationConstraint=${AWS_REGION}

        # Apply CORS configuration to the bucket
        aws --endpoint-url=http://localhost:4566 s3api put-bucket-cors \
            --bucket ${S3_BUCKET_NAME} \
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

        echo "Successfully created bucket ${S3_BUCKET_NAME} with CORS configuration"
    fi
}

# Function to verify email identity in SES
verify_email_identity() {
    local EMAIL=$1
    echo "Verifying email identity: ${EMAIL}"
    awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 ses verify-email-identity \
        --email-address ${EMAIL}
    echo "Email verification initiated for ${EMAIL}"
}

# Function to create an email template
create_email_template() {
    local TEMPLATE_NAME=$1
    local SUBJECT=$2
    local HTML_CONTENT=$3

    echo "Creating email template: ${TEMPLATE_NAME}"
    awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 ses create-template \
        --template '{
            "TemplateName": "'"${TEMPLATE_NAME}"'",
            "SubjectPart": "'"${SUBJECT}"'",
            "HtmlPart": "'"${HTML_CONTENT}"'"
        }'
    echo "Successfully created email template: ${TEMPLATE_NAME}"
}

# Wait for LocalStack to be ready
wait_for_localstack

# Create S3 buckets
create_s3_bucket "druling"
create_s3_bucket "druling-menus"
create_s3_bucket "druling-restaurants"

# Set up SES configurations
# Verify email addresses
verify_email_identity "no-reply@druling.com"
verify_email_identity "support@druling.com"

# Create email templates
create_email_template "WelcomeTemplate" \
    "Welcome to Druling!" \
    "<h1>Welcome to Druling!</h1><p>Thank you for joining our platform.</p>"

echo "AWS resource configuration completed successfully!"