#models
from .models import ContentType
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

#other stuff
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
    )
from .serializers import (
    ContentTypeListSerializer,
    ContentTypeCreateUpdateSerializer,
    ContentTypeDetailSerializer
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
from .pagination import ContentTypePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contenttypes': reverse('api_contenttypes:list', request=request, format=format),
        'new_contenttype': reverse('api_contenttypes:create', request=request, format=format),
    })

class ContentTypeListAPIView(ListAPIView):
    serializer_class = ContentTypeListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = ContentTypePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        contenttypes = ContentType.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                contenttypes = contenttypes.filter(title__icontains=title)

        return contenttypes.distinct()

class ContentTypeCreateAPIView(CreateAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ContentTypeRetrieveAPIView(RetrieveAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ContentTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ContentTypeDeleteAPIView(DestroyAPIView):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
