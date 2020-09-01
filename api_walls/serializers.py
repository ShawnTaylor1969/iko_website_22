from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Wall

class WallListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_walls:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    created_by_name = SerializerMethodField()
    class Meta:
        model = Wall
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'created_by', 'created_by_name', 'message', 'content_app_id', 'content_pk', 'picture', 'created_dateTime', 'likes', 'dislikes'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_created_by_name(request, obj):
        return str(obj.created_by.first_name) + " " + str(obj.created_by.last_name)

class WallCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Wall
        fields = [
            'space', 'title', 'message', 'picture'
        ]

class WallDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    created_by_name = SerializerMethodField()
    class Meta:
        model = Wall
        fields = [
            'id', 'space', 'space_name', 'title', 'created_by', 'created_by_name', 'message', 'content_app_id', 'content_pk', 'picture', 'created_dateTime', 'likes', 'dislikes'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_created_by_name(self, obj):
        return str(obj.created_by.first_name) + " " + str(obj.created_by.last_name)
