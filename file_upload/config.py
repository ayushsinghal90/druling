from dataclasses import dataclass

from file_upload.enum.Buckets import BucketType
from file_upload.enum.FIleType import FileType
from file_upload.requests import QRMenuUploadSerializer
from typing import List, Type, Callable


@dataclass
class FileTypeConfig:
    bucket: str
    valid_extensions: List[str]
    path: Callable[[dict], str]
    serializer: Type


S3_FILE_TYPE_CONFIG = {
    FileType.QR_MENU: FileTypeConfig(
        bucket=BucketType.MENU.value,
        valid_extensions=["jpg", "jpeg", "png"],
        path=lambda p: f"qr_menu/{p.get('branch_id')}",
        serializer=QRMenuUploadSerializer,
    )
}
