from rest_framework import serializers

from branch.requests.serlializers import BranchSerializer
from branch_location.requests.serlializers import BranchLocationSerializer
from contact.requests.serlializers import ContactSerializer


class BranchEditSerializer(serializers.Serializer):
    branch = BranchSerializer()
    location = BranchLocationSerializer(required=False)
    contact = ContactSerializer()
