import django_filters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters, generics, mixins
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ShelfieUser.forms import MemberFormPersonal, MemberProfilePhotoForm
from ShelfieUser.models import User
from ShelfieUser.permissions import IsOwnerOrSuperUser, IsSuperUser
from ShelfieUser.serializers import UserCreateSerializer, UserSerializer, UserFollowSerializer

from knox.views import LoginView as KnoxLoginView
from ShelfieUser.authentication import ExampleAuthentication, CreateUserAuthentication
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth import authenticate


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('username', 'first_name', 'last_name',
                     'email', 'random_user_id')

    def get_queryset(self):
        user = self.request.user
        # If ther requesting user is not a super user ... then they can only
        # see their own information
        if user.is_superuser:
            # site_users = cache.get('site_users')
            site_users = None
            if not site_users:
                site_users = User.objects.all().order_by('-date_joined')
                cache.set('site_users', site_users, 600)
                print 'Not Retrieved From Cache, but set it'
            else:
                print 'Retrieved From Cache'

            return site_users
        else:
            return User.objects.filter(username=user.username)


class UserDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication,]
    permission_classes = []

    # Works off of the mixins.UpdateModelMixin
    def put(self, request, *args, **kwargs):
        random_user_id = self.kwargs.pop('random_user_id')
        user = get_object_or_404(User, random_user_id=random_user_id)
        if len(request.data) == 2:
            user.profile_picture = request.data['profile_picture']
            user.save()
            return Response(HTTP_200_OK)

        else:
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.username = request.data['username']
            user.phone_number = request.data['phone_number']
            user.email = request.data['email']
            user.save()
            return Response(HTTP_200_OK)


    # Works off of the mixins.DestroyModelMixin
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        random_user_id = self.kwargs.pop('random_user_id')
        user = get_object_or_404(User, random_user_id=random_user_id)
        tokens = AuthToken.objects.filter(user=user)
        return user


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []


class LoggedInUserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrSuperUser, IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user


@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([])
def follow_create_api(request, *args, **kwargs):
    active_user = get_object_or_404(User, random_user_id=request.data['random_user_id'])
    followed_user = get_object_or_404(User, random_user_id=request.data['followed_user_id'])
    active_user.following.add(followed_user) # add new user to list of active user's following
    followed_user.followers.add(active_user) # add active_user to new user's list of followers
    serializer = UserFollowSerializer()

    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([])
def follow_delete_api(request, *args, **kwargs):
    active_user = get_object_or_404(User, random_user_id=request.data['random_user_id'])
    followed_user = get_object_or_404(User, random_user_id=request.data['followed_user_id'])
    active_user.following.remove(followed_user) # delete new user from list of active user's following
    followed_user.followers.remove(active_user) # delete active_user from new user's list of followers
    serializer = UserFollowSerializer()

    return Response(serializer.data, status=HTTP_200_OK)


@api_view(['POST'])
def validate_user_data(request):
    values = request.data['values']
    username = None
    email = None
    error = False
    error_response = {}
    print values
    try:
        username = values['username']
        username = username.lower()
    except:
        pass
    try:
        email = values['email']
        email = email.lower()
    except:
        pass
    if username:
        if User.objects.all().filter(username=username).exists():
            error = True
            error_response[
                'username'] = 'The Username (' + username + ') Is Already In Use'
    if email:
        print email
        if User.objects.all().filter(email=email).exists():
            error = True
            error_response[
                'email'] = 'The Email (' + email + ') Is Already In Use'
    if error:
        raise ValidationError(error_response)
    else:
        return Response({"message": "Success"})
