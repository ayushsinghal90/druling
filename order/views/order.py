from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..serializer import OrderSerializer

from ..services import OrderService


class OrderView(ViewSet):
    def __init__(self, order_service=None, **kwargs):
        super().__init__(**kwargs)
        self.order_service = order_service or OrderService()

    @api_handler()
    def create(self, request):
        order = self.order_service.create(request.data)
        return ResponseFactory.created(OrderSerializer(order).data)

    @api_handler()
    def update_status(self, request):
        order = self.order_service.update_status(request.data)
        return ResponseFactory.created(OrderSerializer(order).data)
