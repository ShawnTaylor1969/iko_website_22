from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Space

class SpaceListSerializer(ModelSerializer):
    space_url = HyperlinkedIdentityField(
        view_name='api_spaces:read',
        lookup_field='pk'
        )
    class Meta:
        model = Space
        fields = [
            'space_url', 'id', 'title', 'slug', 'summary', 'body', 'image', 'type', 'layout', 'url', 'show_application_menu', 'show_space_menu', 'content_types', 'status', \
             'admin_method', 'admin_role', 'admin_user', \
             'public_access', 'private_access', 'restricted_access', 'restricted_to_roles', \
             'user_space', 'system_space', 'created_dateTime'
        ]

class SpaceCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Space
        fields = [
            'id', 'title', 'summary', 'body', 'image', 'type', 'layout', 'url', 'show_application_menu', 'show_space_menu', 'content_types', 'status', \
             'admin_method', 'admin_role', 'admin_user', \
             'public_access', 'private_access', 'restricted_access', 'restricted_to_roles'
        ]

class SpaceDetailSerializer(ModelSerializer):
    class Meta:
        model = Space
        fields = [
            'id', 'title', 'summary', 'body', 'image', 'type', 'layout', 'url', 'show_application_menu', 'show_space_menu', 'content_types', 'status', \
             'admin_method', 'admin_role', 'admin_user', \
             'public_access', 'private_access', 'restricted_access', 'restricted_to_roles',
             'user_space', 'system_space', 'created_dateTime'
        ]
