import uuid

from file_upload.s3.s3_read import get_normal_url
from file_upload.s3.s3_upload import get_upload_signed_url

QR_MENU_PATH = "qr_menus"
MENU_BUCKET = "druling-menus"


def get_upload_url_and_file_key(branch_id, file_key):
    new_file_key = f"{uuid.uuid4()}-{file_key}"
    new_file_path = f"{get_sub_path(branch_id)}/{new_file_key}"
    signed_url = get_upload_signed_url(MENU_BUCKET, new_file_path)
    return {
        "upload_url": signed_url,
        "new_file_key": new_file_key,
        "file_key": file_key,
    }


def get_sub_path(branch_id):
    return f"{QR_MENU_PATH}/{branch_id}/"


def get_url(branch_id, file_key):
    return get_normal_url(MENU_BUCKET, f"{get_sub_path(branch_id)}/{file_key}")
