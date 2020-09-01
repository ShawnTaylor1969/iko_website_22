from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Calendar

class CalendarListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_albums:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = Calendar
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'organizer', 'organizer_name', 'summary', 'picture', 'picture_height', 'picture_width'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_organizer_name(request, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)

class CalendarCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Calendar
        fields = [
            'id', 'space', 'title', 'organizer', 'summary', 'picture'
        ]

class CalendarDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = Calendar
        fields = [
            'id', 'space', 'space_name', 'title', 'organizer', 'organizer_name', 'summary', 'picture', 'picture_height', 'picture_width'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_organizer_name(self, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)
