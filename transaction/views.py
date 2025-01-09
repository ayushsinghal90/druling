from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from transaction.requests import TransactionSerializer
from transaction.services import TransactionService


class TransactionView(ViewSet):
    def __init__(self, transaction_service=None, **kwargs):
        super().__init__(**kwargs)
        self.transaction_service = transaction_service or TransactionService()

    @api_handler(serializer=TransactionSerializer)
    def initiate(self, request):
        profile_id = request.user.profile.id
        payment_initiated = self.transaction_service.initiate_payment(
            request.data, profile_id
        )
        return ResponseFactory.created(payment_initiated)
