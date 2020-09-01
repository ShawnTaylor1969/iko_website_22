from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import SpaceLink


class SpaceLinkListSerializer(ModelSerializer):
    spacelink_url = HyperlinkedIdentityField(
        view_name='api_spacelinks:read',
        lookup_field='pk'
        )
    space_title = SerializerMethodField()
    another_space_title = SerializerMethodField()
    program_title = SerializerMethodField()
    parent_title = SerializerMethodField()
    class Meta:
        model = SpaceLink
        fields = [
            'spacelink_url', 'id', 'space', 'space_title', 'root_link', 'parent', 'parent_title', 'title', 'slug', 'sequence', 'type', 'another_space', 'another_space_title', 'content_slug', 'program', 'program_title', 'url', 'icon_URL'
        ]

    def get_space_title(request, obj):
        return str(obj.space.title)

    def get_another_space_title(request, obj):
        if obj.another_space:
            return str(obj.another_space.title)
        else:
            return ""

    def get_program_title(request, obj):
        if obj.program:
            return str(obj.program.title)
        else:
            return ""

    def get_parent_title(request, obj):
        if obj.parent:
            return str(obj.parent.title)
        else:
            return ""

class SpaceLinkCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = SpaceLink
        fields = [
            'id', 'space', 'root_link', 'parent', 'title', 'sequence', 'type', 'another_space', 'content_slug', 'program', 'url', 'icon_URL'
        ]

class SpaceLinkDetailSerializer(ModelSerializer):
    space_title = SerializerMethodField()
    another_space_title = SerializerMethodField()
    program_title = SerializerMethodField()
    parent_title = SerializerMethodField()
    class Meta:
        model = SpaceLink
        fields = [
            'id', 'space', 'space_title', 'root_link', 'parent', 'parent_title', 'title', 'slug', 'sequence', 'type', 'another_space', 'another_space_title', 'content_slug', 'program', 'program_title', 'url', 'icon_URL'
        ]

    def get_space_title(request, obj):
        return str(obj.space.title)

    def get_another_space_title(request, obj):
        if obj.another_space:
            return str(obj.another_space.title)
        else:
            return ""

    def get_program_title(request, obj):
        if obj.program:
            return str(obj.program.title)
        else:
            return ""

    def get_parent_title(request, obj):
        if obj.parent:
            return str(obj.parent.title)
        else:
            return ""
