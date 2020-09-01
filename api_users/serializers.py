from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from django.contrib.auth.models import User

class UserListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_users:read',
        lookup_field='pk'
        )
    class Meta:
        model = User
        fields = [
            'url', 'username', 'first_name', 'last_name'
        ]

class UserCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', "password"
        ]
        extra_kwargs = {"password": {"write_only": True}}
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name'
    ]
