from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import EventType

class EventTypeListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_eventtypes:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = EventType
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'slug', 'author', 'author_name', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_author_name(request, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)

class EventTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = EventType
        fields = [
            'id', 'space', 'title', 'author', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
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

class EventTypeDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = EventType
        fields = [
            'id', 'space', 'space_name', 'title', 'slug', 'author', 'author_name', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_author_name(self, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)
