import django_filters
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters, generics, mixins
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from ShelfieUser.forms import MemberFormPersonal, MemberProfilePhotoForm
from ShelfieUser.models import User
from ShelfieUser.permissions import IsOwnerOrSuperUser, IsSuperUser
from ShelfieUser.serializers import UserCreateSerializer, UserSerializer

from knox.views import LoginView as KnoxLoginView
from ShelfieUser.authentication import ExampleAuthentication
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth import authenticate


# Quick login redirect view, it can be used to add in new login add ons
# for the login attempts


@login_required
def login_redirect(request):
    return redirect('/app')


# Allows members to edit personal profile information
@login_required
def edit_profile_information(request):
    user = request.user
    form = MemberFormPersonal(request.POST or None,
                              request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully updated profile! ')
            return redirect("CleancultUser:edit_profile_information")
    profile_active = True
    context = {
        'profile_active': profile_active,
        'form': form
    }
    return render(request, 'app/user/profile/edit_profile_information.html', context)


# Allows members to edit profile photo
@login_required
def edit_profile_photo(request):
    user = request.user
    print user.profile_image
    form = MemberProfilePhotoForm(
        request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Successfully updated profile photo! ')
            return redirect("CleancultUser:edit_profile_information")
    profile_active = True
    context = {
        'profile_active': profile_active,
        'form': form
    }
    return render(request, 'account/change_profile_photo.html', context)


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
    permission_classes = [IsAuthenticated,]

    # Works off of the mixins.UpdateModelMixin
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Works off of the mixins.DestroyModelMixin
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        random_user_id = self.kwargs.pop('random_user_id')
        user = get_object_or_404(User, random_user_id=random_user_id)
        tokens = AuthToken.objects.filter(user=user)
        # If the use is not a super user ...
        if not self.request.user.is_superuser:
            # ... and the user they are looking at is not themselves then they are block
            for token in tokens:
                print token
                # if not (token == self.request.token):
                #     raise PermissionDenied(
                #         'Sorry, you do not have permissions to view this entry')
        return user


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class LoggedInUserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrSuperUser, IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user


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
