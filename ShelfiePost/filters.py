import django_filters
from ShelfiePost.models import Post
from ShelfiePost.serializers import PostSerializer
from rest_framework import generics

class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['game']
