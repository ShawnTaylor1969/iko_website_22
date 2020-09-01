#models
from .models import Event
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
    EventListSerializer,
    EventCreateUpdateSerializer,
    EventDetailSerializer
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
from .pagination import EventPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'events': reverse('api_events:list', request=request, format=format),
        'new_event': reverse('api_events:create', request=request, format=format),
    })

class EventListAPIView(ListAPIView):
    serializer_class = EventListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    pagination_class = EventPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        events = Event.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                events = events.filter(title__icontains=title)

            body = self.request.GET.get("body", "")
            if not body == "":
                events = events.filter(body__icontains=body)

        return events.distinct()

class EventCreateAPIView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class EventRetrieveAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class EventUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class EventDeleteAPIView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
