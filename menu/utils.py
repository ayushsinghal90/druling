import uuid

from commons.utils.s3.s3_upload import get_upload_signed_url


def get_upload_url_and_file_key(bucket, sub_path, file_key):
    new_file_key = f"/{sub_path}/{uuid.uuid4()}-{file_key}"
    signed_url = get_upload_signed_url(bucket, new_file_key)
    return {"upload_url": signed_url, "file_key": new_file_key}
