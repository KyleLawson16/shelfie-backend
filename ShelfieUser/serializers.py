from rest_framework import serializers

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
    url = UserUrlField(view_name='UserDetailAPIView')
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
        ]
