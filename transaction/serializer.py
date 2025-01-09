from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import Transaction


class TransactionCreateSerializer(BaseModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "amount",
            "profile_id",
            "discount",
            "taxes",
            "total_amount",
            "status",
            "method",
            "completed_at",
            "reference_number",
        ]
