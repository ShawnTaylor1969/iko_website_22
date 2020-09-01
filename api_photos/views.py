#models
from .models import Photo
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
    PhotoListSerializer,
    PhotoCreateUpdateSerializer,
    PhotoDetailSerializer
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
from .pagination import PhotoPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'photos': reverse('api_photos:list', request=request, format=format),
        'new_photo': reverse('api_photos:create', request=request, format=format),
    })

class PhotoListAPIView(ListAPIView):
    serializer_class = PhotoListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary']
    pagination_class = PhotoPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        photos = Photo.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                photos = photos.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not summary == "":
                photos = photos.filter(summary__icontains=summary)

        return photos.distinct()

class PhotoCreateAPIView(CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

class PhotoRetrieveAPIView(RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PhotoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    
class PhotoDeleteAPIView(DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
