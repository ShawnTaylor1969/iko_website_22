#models
from .models import Wall
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
    WallListSerializer,
    WallCreateUpdateSerializer,
    WallDetailSerializer
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
from .pagination import WallPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'walls': reverse('api_walls:list', request=request, format=format),
        'new_wall': reverse('api_walls:create', request=request, format=format),
    })

class WallListAPIView(ListAPIView):
    serializer_class = WallListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'message']
    pagination_class = WallPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        walls = Wall.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                walls = walls.filter(title__icontains=title)

            message = self.request.GET.get("message", "")
            if not message == "":
                walls = walls.filter(message__icontains=message)

            # publications = self.request.GET.get("publications", "")
            # if len(publications) > 0:
            #     str_pks = publications.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         publication = Publication.objects.get(pk=int(pk))
            #         pks.append(publication)
            #     walls = walls.filter(publication__in=pks)
            #
            # created_bys = self.request.GET.get("created_bys", "")
            # if len(created_bys) > 0:
            #     str_pks = created_bys.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         created_by = User.objects.get(pk=int(pk))
            #         pks.append(created_by)
            #     walls = walls.filter(created_by__in=pks)

            # publication_dateTime_start = self.request.GET.get("publication_dateTime_start", "")
            # if len(publication_dateTime_start) > 0:
            #     walls = walls.filter(publication_dateTime__gte=date(int(publication_dateTime_start[0:4]), int(publication_dateTime_start[5:7]), int(publication_dateTime_start[8:10])))
            #
            # publication_dateTime_end = self.request.GET.get("publication_dateTime_end", "")
            # if len(publication_dateTime_end) > 0:
            #     walls = walls.filter(publication_dateTime__gte=date(int(publication_dateTime_end[0:4]), int(publication_dateTime_end[5:7]), int(publication_dateTime_end[8:10])))

        return walls.distinct()

class WallCreateAPIView(CreateAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class WallRetrieveAPIView(RetrieveAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class WallUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class WallDeleteAPIView(DestroyAPIView):
    queryset = Wall.objects.all()
    serializer_class = WallDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
