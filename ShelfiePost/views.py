import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfiePost.serializers import PostSerializer
from ShelfiePost.models import Post
from ShelfiePost.filters import PostFilter

from rest_framework import filters, generics, mixins
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication



class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []
    filter_class = PostFilter
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('user', 'game', 'challenge')

    def get_queryset(self):
        posts = Post.objects.all()
        return posts


class PostDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []

    def get_object(self, *args, **kwargs):
        random_post_id = self.kwargs.pop('random_post_id')
        post = get_object_or_404(Post, random_post_id=random_post_id)
        return post
