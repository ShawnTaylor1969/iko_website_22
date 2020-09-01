from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import EventSchedule

class EventScheduleListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_eventschedules:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = EventSchedule
        fields = [
            'url', 'id', 'space', 'space_name', 'calendar', 'calendar_title', 'title', 'slug', 'organizer', 'organizer_name', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                'repeat_on_Mon', 'repeat_on_Tue','repeat_on_Wed','repeat_on_Thu','repeat_on_Fri','repeat_on_Sat','repeat_on_Sun', \
                'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', \
                'end_series', 'series_occurrences', 'location', 'show_as_busy'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_organizer_name(request, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)

class EventScheduleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = EventSchedule
        fields = [
            'space', 'space_name', 'calendar', 'calendar_title', 'title', 'slug', 'organizer', 'organizer_name', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                'repeat_on_Mon', 'repeat_on_Tue','repeat_on_Wed','repeat_on_Thu','repeat_on_Fri','repeat_on_Sat','repeat_on_Sun', \
                'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', \
                'end_series', 'series_occurrences', 'location', 'show_as_busy'
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

class EventScheduleDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    organizer_name = SerializerMethodField()
    class Meta:
        model = EventSchedule
        fields = [
            'id', 'space', 'space_name', 'calendar', 'calendar_title', 'title', 'slug', 'organizer', 'organizer_name', 'body', 'picture', 'picture_height', 'picture_width', 'event_type', \
                'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                'repeat_on_Mon', 'repeat_on_Tue','repeat_on_Wed','repeat_on_Thu','repeat_on_Fri','repeat_on_Sat','repeat_on_Sun', \
                'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', \
                'end_series', 'series_occurrences', 'location', 'show_as_busy'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_organizer_name(self, obj):
        return str(obj.organizer.first_name) + " " + str(obj.organizer.last_name)
