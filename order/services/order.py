import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from .order_item import OrderItemService
from ..models import Order
from ..serializer import OrderSerializer

logger = logging.getLogger(__name__)


class OrderService(BaseService):
    def __init__(self, order_item_service=None):
        super().__init__(Order)
        self.order_item_service = order_item_service or OrderItemService()

    def create(self, order_data):
        with transaction.atomic():
            items = order_data.pop("items")
            serializer = OrderSerializer(data=order_data)
            serializer.is_valid(raise_exception=True)
            order = serializer.save()

            self.order_item_service.bulk_create(order, items)
            return order

    def update_status(self, order_data):
        with transaction.atomic():
            order_ids, status = order_data.get("order_ids"), order_data.get("status")
            try:
                orders = Order.objects.filter(id__in=order_ids)
                orders.update(status=status)
                return orders
            except Exception as e:
                logger.error(f"Error updating status: {e}")
                return []

    def get_all(self, branch):
        try:
            return Order.objects.filter(branch=branch)
        except Exception as e:
            logger.error(f"Error fetching features: {e}")
            return []
