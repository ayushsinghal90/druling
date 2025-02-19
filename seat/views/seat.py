from rest_framework.viewsets import ViewSet

from commons.api.responses import ResponseFactory
from commons.middleware.api_handler import api_handler
from ..serializer import SeatSerializer

from ..services import SeatService


class SeatView(ViewSet):
    def __init__(self, seat_service=None, **kwargs):
        super().__init__(**kwargs)
        self.seat_service = seat_service or SeatService()

    @api_handler()
    def create(self, request):
        seat = self.seat_service.create(request.data)
        return ResponseFactory.created(SeatSerializer(seat).data)
