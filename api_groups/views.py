#models
from .models import Group
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
    GroupListSerializer,
    GroupCreateUpdateSerializer,
    GroupDetailSerializer
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
from .pagination import GroupPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'groups': reverse('api_groups:list', request=request, format=format),
        'new_group': reverse('api_groups:create', request=request, format=format),
    })

class GroupListAPIView(ListAPIView):
    serializer_class = GroupListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title']
    pagination_class = GroupPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        groups = Group.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                groups = groups.filter(title__icontains=title)

        return groups.distinct()

class GroupCreateAPIView(CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GroupRetrieveAPIView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GroupUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class GroupDeleteAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
