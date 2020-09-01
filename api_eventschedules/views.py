#models
from .models import EventSchedule
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
    EventScheduleListSerializer,
    EventScheduleCreateUpdateSerializer,
    EventScheduleDetailSerializer
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
from .pagination import EventSchedulePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'eventschedules': reverse('api_eventschedules:list', request=request, format=format),
        'new_eventschedule': reverse('api_eventschedules:create', request=request, format=format),
    })

class EventScheduleListAPIView(ListAPIView):
    serializer_class = EventScheduleListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    pagination_class = EventSchedulePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        eventschedules = EventSchedule.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                eventschedules = eventschedules.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not title == "":
                eventschedules = eventschedules.filter(summary__icontains=summary)

        return eventschedules.distinct()

class EventScheduleCreateAPIView(CreateAPIView):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventScheduleRetrieveAPIView(RetrieveAPIView):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class EventScheduleUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class EventScheduleDeleteAPIView(DestroyAPIView):
    queryset = EventSchedule.objects.all()
    serializer_class = EventScheduleDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
