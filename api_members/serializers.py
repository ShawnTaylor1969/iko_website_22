from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Member

class MemberListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_members:read',
        lookup_field='pk'
        )
    username = SerializerMethodField()
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    class Meta:
        model = Member
        fields = [
            'url', 'username', 'first_name', 'last_name', 'status',
                'is_soronian_sister', 'is_independent', 'is_site_visitor',
                'about_me', 'picture', 'pledge_class', 'graduation_year', 'birth_date', 'house_positions', \
                'profiled', 'profiled_dateTime', \
                'validated', 'validated_by', 'validated_dateTime', \
                'activated', 'activated_by', 'activated_dateTime', \
                'updated_dateTime', 'created_dateTime'
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

class MemberCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = [
                'is_soronian_sister', 'is_independent', 'is_site_visitor',
                'about_me', 'picture', 'pledge_class', 'graduation_year', 'birth_date'
        ]
class MemberDetailSerializer(ModelSerializer):
    username = SerializerMethodField()
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    class Meta:
        model = Member
        fields = [
            'username', 'first_name', 'last_name', 'status',
                'is_soronian_sister', 'is_independent', 'is_site_visitor',
                'about_me', 'picture', 'pledge_class', 'graduation_year', 'birth_date'
        ]

    def get_username(self, obj):
        return obj.user.username

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name
