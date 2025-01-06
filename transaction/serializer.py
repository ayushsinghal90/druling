from commons.serializer.BaseModelSerializer import BaseModelSerializer

from .models import Transaction


class TransactionSerializer(BaseModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "amount", "profile"]
