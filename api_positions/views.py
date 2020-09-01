#models
from .models import Position
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
    PositionListSerializer,
    PositionCreateUpdateSerializer,
    PositionDetailSerializer
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
from .pagination import PositionPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'positions': reverse('api_positions:list', request=request, format=format),
        'new_position': reverse('api_positions:create', request=request, format=format),
    })

class PositionListAPIView(ListAPIView):
    serializer_class = PositionListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class = PositionPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        positions = Position.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                positions = positions.filter(title__icontains=title)

        return positions.distinct()

class PositionCreateAPIView(CreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class PositionRetrieveAPIView(RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PositionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class PositionDeleteAPIView(DestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
