from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Photo

class PhotoListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_photos:read',
        lookup_field='pk'
        )
    album_title = SerializerMethodField()
    space_id = SerializerMethodField()
    space_name = SerializerMethodField()
    uploaded_by_name = SerializerMethodField()
    class Meta:
        model = Photo
        fields = [
            'url', 'id', 'album', 'album_title', 'space_id', 'space_name', 'title', 'slug', 'uploaded_by', 'uploaded_by_name', 'summary', 'picture', 'picture_height', 'picture_width', 'updated_dateTime', 'created_dateTime'
        ]

    def get_album_title(request, obj):
        return str(obj.album.title)

    def get_space_id(request, obj):
        return str(obj.album.space.id)

    def get_space_name(request, obj):
        return str(obj.album.space.title)

    def get_uploaded_by_name(request, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)

class PhotoCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            'id', 'album', 'title', 'uploaded_by', 'summary', 'picture'
        ]

    # def validate_parent_position(self, value):
    #     if value == self.instance:
    #         raise ValidationError("Parent position cannot be itself.")
    #     return value
    #
    # def validate(self, data):
    #     if data['is_top_five'] == False and data['parent_position'] == None:
    #         raise ValidationError("Parent position is required when the position is not Top Five.")
    #     return data

class PhotoDetailSerializer(ModelSerializer):
    album_title = SerializerMethodField()
    space_id = SerializerMethodField()
    space_name = SerializerMethodField()
    uploaded_by_name = SerializerMethodField()
    class Meta:
        model = Photo
        fields = [
            'id', 'album', 'album_title', 'space_id', 'space_name', 'title', 'slug', 'uploaded_by', 'uploaded_by_name', 'summary', 'picture', 'picture_height', 'picture_width', 'updated_dateTime', 'created_dateTime'
        ]

    def get_album_title(request, obj):
        return str(obj.album.title)

    def get_space_id(request, obj):
        return str(obj.album.space.id)

    def get_space_name(request, obj):
        return str(obj.album.space.title)

    def get_uploaded_by_name(request, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)
