import django_filters

from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from ShelfiePost.serializers import PostSerializer, PostLikesSerializer
from ShelfiePost.models import Post
from ShelfiePost.filters import PostFilter
from ShelfieUser.models import User

from rest_framework import filters, generics, mixins
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from knox.auth import TokenAuthentication

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([])
def like_create_api(request, *args, **kwargs):
    post = get_object_or_404(Post, random_post_id=request.data['random_post_id'])
    post.likes.add(request.data['random_user_id'])
    serializer = PostLikesSerializer()

    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([])
def like_delete_api(request, *args, **kwargs):
    post = get_object_or_404(Post, random_post_id=request.data['random_post_id'])
    user = get_object_or_404(User, random_user_id=request.data['random_user_id'])
    post.likes.remove(user)
    serializer = PostLikesSerializer()

    return Response(serializer.data, status=HTTP_200_OK)

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
