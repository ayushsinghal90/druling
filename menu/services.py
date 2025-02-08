import logging

from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db import transaction

from branch.services import BranchService
from commons.exceptions.BaseError import BaseError
from commons.service.BaseService import BaseService
from .models import QRMenu
from .serializer import QRMenuCreateSerializer
from menu_file.services import MenuFileService

logger = logging.getLogger(__name__)


class QRMenuService(BaseService):
    def __init__(self, branch_service=None, menu_file_service=None):
        super().__init__(QRMenu)
        self.branch_service = branch_service or BranchService()
        self.menu_file_service = menu_file_service or MenuFileService()

    def create(self, data):
        with transaction.atomic():
            try:
                branch_id = data.get("branch_id")
                theme = data.get("theme")
                files = data.get("files")
                qr_menu_serializer = QRMenuCreateSerializer(
                    data={"branch_id": branch_id, "theme": theme}
                )
                if qr_menu_serializer.is_valid(raise_exception=True):
                    with transaction.atomic():
                        qr_menu_instance = qr_menu_serializer.save()

                self.menu_file_service.create(qr_menu_instance, files)
                return qr_menu_instance

            except ValidationError as e:
                logger.warning(f"Validation error while creating QR menu: {str(e)}")
                raise

            except Exception:
                logger.error("Error while creating QR menu", exc_info=True)
                raise

    def get_by_branch_id(self, branch_id):
        try:
            return self.model.objects.get(branch_id=branch_id)
        except self.model.DoesNotExist:
            logger.error(
                f"{self.model.__name__} with branch id {branch_id} does not exist."
            )
            raise ObjectDoesNotExist(
                f"{self.model.__name__} with branch id {branch_id} does not exist."
            )

        except Exception as e:
            logger.error(
                f"An error occurred while fetching the {self.model.__name__}: {str(e)}",
                exc_info=True,
            )
            raise BaseError(
                f"Error while fetching the {self.model.__name__}", original_exception=e
            )

    def get_list(self, profile_id):
        try:
            return QRMenu.objects.filter(
                branch__relations__profile_id=profile_id
            ).distinct()
        except Exception as e:
            logger.error("Error while fetching restaurant", exc_info=True)
            raise BaseError("Error while fetching restaurant", original_exception=e)

    def activate_menu(self, id):
        try:
            with transaction.atomic():
                qr_menus = self.model.objects.filter(id=id, is_active=False)
                for qr_menu in qr_menus:
                    qr_menu.is_active = True
                    qr_menu.save()
                return qr_menu
        except Exception as e:
            logger.error("Error while activating menu", exc_info=True)
            raise BaseError("Error while activating menu", original_exception=e)
