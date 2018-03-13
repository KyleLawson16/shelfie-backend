from rest_framework import serializers

from ShelfieKey.models import AmazonS3


class AmazonS3Serializer(serializers.ModelSerializer):
    class Meta:
        model = AmazonS3
        fields = [
            'bucket',
            'region',
            'access_key',
            'secret_access_key',
        ]
