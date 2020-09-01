from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import ContentType

class ContentTypeListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_contenttypes:read',
        lookup_field='pk'
        )
    class Meta:
        model = ContentType
        fields = [
            'url', 'id', 'title', 'slug', 'sequence', 'namespace', 'active', 'space_page_URL', 'directory_URL', 'icon_URL'
        ]

class ContentTypeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = [
            'id', 'title', 'sequence', 'namespace', 'active', 'space_page_URL', 'directory_URL', 'icon_URL'
        ]

class ContentTypeDetailSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = [
            'id', 'title', 'sequence', 'namespace', 'active', 'space_page_URL', 'directory_URL', 'icon_URL'
        ]
