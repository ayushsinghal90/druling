from file_upload.enum.FIleType import FileType


class BasePathService:
    FILE_PATH_MAP = {
        FileType.QR_MENU: lambda p: f"qr_menu/{p.get('branch_id')}",
    }

    def get_sub_path(self, file_type: FileType, params=None) -> str:
        if params is None:
            params = {}
        _, path_func = self.FILE_PATH_MAP.get(file_type)
        return path_func(params)
