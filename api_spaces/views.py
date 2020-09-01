#models
from .models import Space
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
# from .permissions import IsAuthorOrReadOnly

#other stuff
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
    )
from .serializers import (
    SpaceListSerializer,
    SpaceCreateUpdateSerializer,
    SpaceDetailSerializer
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
from .pagination import SpacePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'spaces': reverse('api_spaces:list', request=request, format=format),
        'new_space': reverse('api_spaces:create', request=request, format=format),
    })

class SpaceListAPIView(ListAPIView):
    serializer_class = SpaceListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = SpacePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        spaces = Space.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                spaces = spaces.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not title == "":
                spaces = spaces.filter(summary__icontains=summary)

        return spaces.distinct()

class SpaceCreateAPIView(CreateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceRetrieveAPIView(RetrieveAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SpaceUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    permission_classes = [IsAuthenticated]

class SpaceDeleteAPIView(DestroyAPIView):
    queryset = Space.objects.all()
    serializer_class = SpaceDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
