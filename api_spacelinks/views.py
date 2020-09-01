#models
from .models import SpaceLink
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
    SpaceLinkListSerializer,
    SpaceLinkCreateUpdateSerializer,
    SpaceLinkDetailSerializer
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
from .pagination import SpaceLinkPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'spacelinks': reverse('api_spacelinks:list', request=request, format=format),
        'new_spacelinks': reverse('api_spacelinks:create', request=request, format=format),
    })

class SpaceLinkListAPIView(ListAPIView):
    serializer_class = SpaceLinkListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = SpaceLinkPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        spacelinks = SpaceLink.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                spacelinks = spacelinks.filter(title__icontains=title)

        return spacelinks.distinct()

class SpaceLinkCreateAPIView(CreateAPIView):
    queryset = SpaceLink.objects.all()
    serializer_class = SpaceLinkCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceLinkRetrieveAPIView(RetrieveAPIView):
    queryset = SpaceLink.objects.all()
    serializer_class = SpaceLinkDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceLinkUpdateAPIView(RetrieveUpdateAPIView):
    queryset = SpaceLink.objects.all()
    serializer_class = SpaceLinkCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceLinkDeleteAPIView(DestroyAPIView):
    queryset = SpaceLink.objects.all()
    serializer_class = SpaceLinkDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
