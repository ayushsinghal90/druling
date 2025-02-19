from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..serializer import ItemSerializer

from ..services.item import ItemService


class ItemView(ViewSet):
    def __init__(self, item_service=None, **kwargs):
        super().__init__(**kwargs)
        self.item_service = item_service or ItemService()

    @api_handler()
    def create(self, request):
        item = self.item_service.create(request.data)
        return ResponseFactory.created(ItemSerializer(item).data)
