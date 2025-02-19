import logging

from django.db import transaction

from commons.service.BaseService import BaseService
from ..models import OrderItem
from ..serializer import OrderItemSerializer

logger = logging.getLogger(__name__)


class OrderItemService(BaseService):
    def __init__(self):
        super().__init__(OrderItem)

    def bulk_create(self, order, order_items_data):
        with transaction.atomic():
            for order_item in order_items_data:
                order_item["order_id"] = order.id

            serializer = OrderItemSerializer(data=order_items_data, many=True)
            serializer.is_valid(raise_exception=True)

            order_item_instances = [
                OrderItem(**data) for data in serializer.validated_data
            ]
            order_items = OrderItem.objects.bulk_create(order_item_instances)

            return order_items

    def get_all(self, order):
        try:
            return OrderItem.objects.filter(order=order)
        except Exception as e:
            logger.error(f"Error fetching features: {e}")
            return []
