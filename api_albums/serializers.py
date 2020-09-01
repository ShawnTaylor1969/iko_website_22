from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Album

class AlbumListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_albums:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = Album
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'author', 'author_name', 'summary', 'picture', 'picture_height', 'picture_width'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_author_name(request, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)

class AlbumCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id', 'space', 'title', 'author', 'summary', 'picture'
        ]

class AlbumDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = Album
        fields = [
            'id', 'space', 'space_name', 'title', 'author', 'author_name', 'summary', 'picture', 'picture_height', 'picture_width'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_author_name(self, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)
