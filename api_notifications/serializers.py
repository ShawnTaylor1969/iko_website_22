from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Notification

class NotificationListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_notifications:read',
        lookup_field='pk'
        )
    notify_user_name = SerializerMethodField()
    source_user_name = SerializerMethodField()
    class Meta:
        model = Notification
        fields = [
            'url', 'id', 'notify_user', 'notify_user_name', 'source_user', 'source_user_name', 'token', 'message', 'content_app_id', 'content_slug', 'cleared', 'cleared_dateTime', 'created_dateTime'
        ]

    def get_notify_user_name(request, obj):
        return str(obj.notify_user.first_name) + " " + str(obj.notify_user.last_name)

    def get_source_user_name(request, obj):
        return str(obj.source_user.first_name) + " " + str(obj.source_user.last_name)

class NotificationCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'notify_user', 'source_user', 'token', 'message', 'content_app_id', 'content_slug'
        ]
class NotificationDetailSerializer(ModelSerializer):
    notify_user_name = SerializerMethodField()
    source_user_name = SerializerMethodField()
    class Meta:
        model = Notification
        fields = [
            'id', 'notify_user', 'notify_user_name', 'source_user', 'source_user_name', 'token', 'message', 'content_app_id', 'content_slug', 'cleared', 'cleared_dateTime', 'created_dateTime'
        ]

    def get_notify_user_name(request, obj):
        return str(obj.notify_user.first_name) + " " + str(obj.notify_user.last_name)

    def get_source_user_name(request, obj):
        return str(obj.source_user.first_name) + " " + str(obj.source_user.last_name)
