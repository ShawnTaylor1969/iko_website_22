from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from .models import Article

class ArticleListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api_articles:read',
        lookup_field='pk'
        )
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'url', 'id', 'space', 'space_name', 'title', 'slug', 'author', 'author_name', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
        ]

    def get_space_name(request, obj):
        return str(obj.space.title)

    def get_author_name(request, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)

class ArticleCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id', 'space', 'title', 'author', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
        ]
        
class ArticleDetailSerializer(ModelSerializer):
    space_name = SerializerMethodField()
    author_name = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'id', 'space', 'space_name', 'title', 'slug', 'author', 'author_name', 'summary', 'body', 'image', 'image_size', 'related_content', 'status', 'featured', 'featured_start_dateTime', 'featured_end_dateTime', 'required_reading', 'publication_dateTime', 'expiration_dateTime', 'read_dateTime', 'updated_dateTime', 'created_dateTime'
        ]

    def get_space_name(self, obj):
        return str(obj.space.title)

    def get_author_name(self, obj):
        return str(obj.author.first_name) + " " + str(obj.author.last_name)
