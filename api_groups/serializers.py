from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Group

class GroupListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_groups:read',
        lookup_field='pk'
        )
    class Meta:
        model = Group
        fields = [
            'url', 'id', 'title', 'slug', 'positions'
        ]

class GroupCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'title', 'positions'
        ]
class GroupDetailSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'title', 'positions'
        ]
