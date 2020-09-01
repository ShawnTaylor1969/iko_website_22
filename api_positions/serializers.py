from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
    )

from .models import Position

class PositionListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_positions:read',
        lookup_field='pk'
        )
    class Meta:
        model = Position
        fields = [
            'url', 'id', 'title', 'slug', 'is_top_five', 'parent_position'
        ]

class PositionCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'title', 'is_top_five', 'parent_position'
        ]

    def validate_parent_position(self, value):
        if value == self.instance:
            raise ValidationError("Parent position cannot be itself.")
        return value

    def validate(self, data):
        if data['is_top_five'] == False and data['parent_position'] == None:
            raise ValidationError("Parent position is required when the position is not Top Five.")
        return data

class PositionDetailSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'id', 'title', 'is_top_five', 'parent_position'
        ]
