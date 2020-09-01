from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Program

class ProgramListSerializer(ModelSerializer):
    program_url = HyperlinkedIdentityField(
        view_name='api_programs:read',
        lookup_field='pk'
        )
    class Meta:
        model = Program
        fields = [
            'program_url', 'id', 'title', 'slug', 'summary', 'body', 'image', 'type', 'url', 'show_application_menu', 'show_space_menu', 'status'
        ]

class ProgramCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id', 'title', 'summary', 'body', 'image', 'type', 'url', 'show_application_menu', 'show_space_menu', 'status'
        ]
class ProgramDetailSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = [
            'id', 'title', 'slug', 'summary', 'body', 'image', 'type', 'url', 'show_application_menu', 'show_space_menu', 'status'
        ]
