from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Timeline

class TimelineListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_timelines:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    event_user_name = SerializerMethodField()

    class Meta:
        model = Timeline
        fields = [
            'url', 'id', 'event', 'event_user', 'event_user_name', 'space', 'space_name', 'title', 'message', 'content_app_id', 'content_slug', 'created_dateTime'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_event_user_name(self, obj):
        return str(obj.event_user_name.first_name) + " " + str(obj.event_user_name.last_name)

class TimelineCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Timeline
        fields = [
            'event', 'event_user', 'space', 'title', 'message', 'content_app_id', 'content_slug'
        ]

class TimelineDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    event_user_name = SerializerMethodField()
    class Meta:
        model = Timeline
        fields = [
            'id', 'event', 'event_user', 'event_user_name', 'space', 'space_name', 'title', 'message', 'content_app_id', 'content_slug', 'created_dateTime'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_event_user_name(self, obj):
        return str(obj.event_user_name.first_name) + " " + str(obj.event_user_name.last_name)
