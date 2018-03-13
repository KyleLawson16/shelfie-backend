from ShelfieKey.serializers import AmazonS3Serializer
from ShelfieKey.models import AmazonS3

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters, generics, mixins
from knox.auth import TokenAuthentication

# Create your views here.
class AmazonS3ListAPIView(generics.ListAPIView):
    serializer_class = AmazonS3Serializer
    queryset = AmazonS3.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []

    def get_queryset(self):
        key = AmazonS3.objects.all()
        return key
