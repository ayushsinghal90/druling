#!/usr/bin/env bash

set -euo pipefail

# enable debug
# set -x

echo "configuring AWS resources"
echo "=========================="
LOCALSTACK_HOST=localhost
AWS_REGION=ap-south-1

create_s3_bucket() {
    local S3_BUCKET_NAME=$1
    awslocal --endpoint-url=http://${LOCALSTACK_HOST}:4566 s3api create-bucket --bucket ${S3_BUCKET_NAME} --region ${AWS_REGION} --create-bucket-configuration LocationConstraint=${AWS_REGION}
}

create_s3_bucket "druling-menus-temp"
create_s3_bucket "druling-menus"
