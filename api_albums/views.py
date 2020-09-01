#models
from .models import Album
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
#from .permissions import IsAuthorOrReadOnly

#other stuff
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
    )
from .serializers import (
    AlbumListSerializer,
    AlbumCreateUpdateSerializer,
    AlbumDetailSerializer
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
from .pagination import AlbumPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'albums': reverse('api_albums:list', request=request, format=format),
        'new_album': reverse('api_albums:create', request=request, format=format),
    })

class AlbumListAPIView(ListAPIView):
    serializer_class = AlbumListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary']
    pagination_class = AlbumPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        albums = Album.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                albums = albums.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not summary == "":
                albums = albums.filter(summary__icontains=summary)

        return albums.distinct()

class AlbumCreateAPIView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AlbumRetrieveAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AlbumUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    
class AlbumDeleteAPIView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
