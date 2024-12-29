from rest_framework import serializers


class SocialContactSerializer(serializers.Serializer):
    facebook = serializers.URLField()
    youtube = serializers.URLField()
    instagram = serializers.URLField()
    website = serializers.URLField()
    x_link = serializers.URLField()
    linkedin = serializers.URLField()
