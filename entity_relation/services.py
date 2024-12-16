import logging

from commons.service.BaseService import BaseService
from .models import EntityRelation
from .serializer import EntityRelationSerializer

logger = logging.getLogger(__name__)


class EntityRelationService(BaseService):
    def __init__(self):
        super().__init__(EntityRelation)

    def create_relation(self, branch_id, profile_id):
        data = {"branch_id": branch_id, "profile_id": profile_id, "role": "owner"}
        entity_relation_serializer = EntityRelationSerializer(data=data)

        if entity_relation_serializer.is_valid(raise_exception=True):
            return entity_relation_serializer.save()
