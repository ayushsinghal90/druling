from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..serializer import OrderItemSerializer

from ..services import OrderItemService


class OrderItemView(ViewSet):
    def __init__(self, order_item_service=None, **kwargs):
        super().__init__(**kwargs)
        self.order_item_service = order_item_service or OrderItemService()

    @api_handler()
    def update_status(self, request):
        seat = self.order_item_service.update_status(request.data)
        return ResponseFactory.created(OrderItemSerializer(seat).data)
