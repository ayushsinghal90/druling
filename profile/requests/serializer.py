from rest_framework import serializers

from contact.requests.serlializers import ContactSerializer


class ProfileSerializer(serializers.Serializer):
    last_name = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    contact_info = ContactSerializer()
    img_url = serializers.URLField(max_length=200, required=False)
