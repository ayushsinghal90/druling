from dataclasses import dataclass

from file_upload.enum.Buckets import BucketType
from file_upload.enum.FileType import FileType
from file_upload.requests import QRMenuUploadSerializer
from typing import List, Type, Callable, Optional


@dataclass
class FileTypeConfig:
    bucket: str
    valid_extensions: List[str]
    path: Callable[[dict], str]
    serializer: Optional[Type]


S3_FILE_TYPE_CONFIG = {
    FileType.QR_MENU: FileTypeConfig(
        bucket=BucketType.MENU.value,
        valid_extensions=["jpg", "jpeg", "png"],
        path=lambda p: f"qr_menus/{p.get('branch_id')}",
        serializer=QRMenuUploadSerializer,
    ),
    FileType.RESTAURANT_LOGO: FileTypeConfig(
        bucket=BucketType.RESTAURANT.value,
        valid_extensions=["jpg", "jpeg", "png"],
        path=lambda p: "restaurant_logos",
        serializer=None,
    ),
    FileType.BRANCH_LOGO: FileTypeConfig(
        bucket=BucketType.RESTAURANT.value,
        valid_extensions=["jpg", "jpeg", "png"],
        path=lambda p: "branch_logos",
        serializer=None,
    ),
    FileType.USER_PROFILE: FileTypeConfig(
        bucket=BucketType.DRULING.value,
        valid_extensions=["jpg", "jpeg", "png"],
        path=lambda p: "user_profile",
        serializer=None,
    ),
}
