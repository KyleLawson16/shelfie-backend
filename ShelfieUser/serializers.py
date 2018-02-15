from rest_framework import serializers
from django.db.models import Q

from rest_framework.serializers import (
    CharField,
    EmailField
)
from rest_framework.authtoken.models import Token

from ShelfieUser.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    random_user_id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'random_user_id',
            'password',
            'confirm_password',
            'phone_number',
            'is_staff',
            'is_superuser'
        ]

    def create(self, validated_data):
        print validated_data
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError(
                {'password': ['this field should match confirm password']})

        try:
            phone_number = validated_data['phone_number']
        except:
            phone_number = ''
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=phone_number,
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],

        )
        user.set_password(validated_data['password'])

        user.save()

        return user

# Allows us to create a Detail View Url and attach it to the list view


class UserUrlField(serializers.HyperlinkedIdentityField):
    lookup_field = 'random_user_id'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = UserUrlField(view_name='ShelfieUser:UserDetailAPIView')
    username = serializers.CharField(read_only=True)


    class Meta:
        model = User
        fields = [
            'url',
            'random_user_id',
            'username',
            'email',
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'is_active',
            'is_staff',
            'is_superuser',
            'gender',
            'profile_picture',
        ]

# class UserLoginSerializer(serializers.ModelSerializer):
#     token = CharField(allow_blank=True, read_only=True)
#     username = CharField(required=False, allow_blank=True)
#     email = EmailField(label='Email Address', required=False, allow_blank=True)
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'token',
#
#         ]
#         extra_kwargs = {"password":
#                             {"write_only": True}
#                             }
#     def validate(self, data):
#         user_obj = None
#         email = data.get("email", None)
#         username = data.get("username", None)
#         password = data["password"]
#         if not email and not username:
#             raise ValidationError("A username or email is required to login")
#
#         user = User.objects.filter(
#             Q(email=email) |
#             Q(username=username)
#         ).distinct()
#         if user.exists() and user.count() == 1:
#             user_obj = user.first()
#         else:
#             raise ValidationError("The username or email entered is not valid")
#
#         if user_obj:
#             if not user_obj.check_password(password):
#                 raise ValidationError("Incorrect username or password")
#
#
#         data["token"] = "TOKEN"
#
#         return data
