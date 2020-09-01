#models
from .models import Article
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .permissions import IsAuthorOrReadOnly

#other stuff
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
    )
from .serializers import (
    ArticleListSerializer,
    ArticleCreateUpdateSerializer,
    ArticleDetailSerializer
    )

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
    )

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView
    )
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.reverse import reverse

from django.db.models import Q, Count
from .pagination import ArticlePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'articles': reverse('api_articles:list', request=request, format=format),
        'new_article': reverse('api_articles:create', request=request, format=format),
    })

class ArticleListAPIView(ListAPIView):
    serializer_class = ArticleListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = ArticlePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        articles = Article.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                articles = articles.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not title == "":
                articles = articles.filter(summary__icontains=summary)

            publications = self.request.GET.get("publications", "")
            if len(publications) > 0:
                str_pks = publications.split(",")
                pks = []
                for pk in str_pks:
                    publication = Publication.objects.get(pk=int(pk))
                    pks.append(publication)
                articles = articles.filter(publication__in=pks)

            authors = self.request.GET.get("authors", "")
            if len(authors) > 0:
                str_pks = authors.split(",")
                pks = []
                for pk in str_pks:
                    author = User.objects.get(pk=int(pk))
                    pks.append(author)
                articles = articles.filter(author__in=pks)

            publication_dateTime_start = self.request.GET.get("publication_dateTime_start", "")
            if len(publication_dateTime_start) > 0:
                articles = articles.filter(publication_dateTime__gte=date(int(publication_dateTime_start[0:4]), int(publication_dateTime_start[5:7]), int(publication_dateTime_start[8:10])))

            publication_dateTime_end = self.request.GET.get("publication_dateTime_end", "")
            if len(publication_dateTime_end) > 0:
                articles = articles.filter(publication_dateTime__gte=date(int(publication_dateTime_end[0:4]), int(publication_dateTime_end[5:7]), int(publication_dateTime_end[8:10])))

        return articles.distinct()

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ArticleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class ArticleDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
