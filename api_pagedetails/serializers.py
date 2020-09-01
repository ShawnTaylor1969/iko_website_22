from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import PageDetail

class PageDetailListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_pagedetails:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    class Meta:
        model = PageDetail
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'slug', 'body'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

class PageDetailCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = PageDetail
        fields = [
            'space', 'title', 'body'
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

class PageDetailDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    class Meta:
        model = PageDetail
        fields = [
            'id', 'space', 'space_name', 'title', 'body'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)
