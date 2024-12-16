import logging

from .serializer import EntityRelationSerializer

logger = logging.getLogger(__name__)


class EntityRelationService:
    def create_relation(self, branch_id, profile_id):
        data = {"branch_id": branch_id, "profile_id": profile_id, "role": "owner"}
        entity_relation_serializer = EntityRelationSerializer(data=data)

        if entity_relation_serializer.is_valid(raise_exception=True):
            return entity_relation_serializer.save()
