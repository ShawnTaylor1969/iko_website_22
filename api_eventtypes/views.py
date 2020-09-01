#models
from .models import EventType
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
    EventTypeListSerializer,
    EventTypeCreateUpdateSerializer,
    EventTypeDetailSerializer
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
from .pagination import EventTypePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'eventtypes': reverse('api_eventtypes:list', request=request, format=format),
        'new_eventtype': reverse('api_eventtypes:create', request=request, format=format),
    })

class EventTypeListAPIView(ListAPIView):
    serializer_class = EventTypeListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = EventTypePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        eventtypes = EventType.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                eventtypes = eventtypes.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not title == "":
                eventtypes = eventtypes.filter(summary__icontains=summary)

            # publications = self.request.GET.get("publications", "")
            # if len(publications) > 0:
            #     str_pks = publications.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         publication = Publication.objects.get(pk=int(pk))
            #         pks.append(publication)
            #     eventtypes = eventtypes.filter(publication__in=pks)
            #
            # authors = self.request.GET.get("authors", "")
            # if len(authors) > 0:
            #     str_pks = authors.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         author = User.objects.get(pk=int(pk))
            #         pks.append(author)
            #     eventtypes = eventtypes.filter(author__in=pks)

            # publication_dateTime_start = self.request.GET.get("publication_dateTime_start", "")
            # if len(publication_dateTime_start) > 0:
            #     eventtypes = eventtypes.filter(publication_dateTime__gte=date(int(publication_dateTime_start[0:4]), int(publication_dateTime_start[5:7]), int(publication_dateTime_start[8:10])))
            #
            # publication_dateTime_end = self.request.GET.get("publication_dateTime_end", "")
            # if len(publication_dateTime_end) > 0:
            #     eventtypes = eventtypes.filter(publication_dateTime__gte=date(int(publication_dateTime_end[0:4]), int(publication_dateTime_end[5:7]), int(publication_dateTime_end[8:10])))

        return eventtypes.distinct()

class EventTypeCreateAPIView(CreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class EventTypeRetrieveAPIView(RetrieveAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class EventTypeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class EventTypeDeleteAPIView(DestroyAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
