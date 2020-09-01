from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Event

class EventListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_events:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'url', 'id', 'space', 'space_name', 'calendar', 'calendar_title', 'title', 'slug', 'organizer', 'organizer_name', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'location', 'show_as_busy'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_organizer_name(request, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)

class EventCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 'space', 'calendar', 'title', 'slug', 'organizer', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'location', 'show_as_busy'
        ]

class EventDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'id', 'space', 'space_name', 'calendar', 'calendar_title', 'title', 'slug', 'organizer', 'organizer_name', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'location', 'show_as_busy'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_organizer_name(self, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)
