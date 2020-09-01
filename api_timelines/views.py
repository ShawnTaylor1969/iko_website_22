#models
from .models import Timeline
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
    TimelineListSerializer,
    TimelineCreateUpdateSerializer,
    TimelineDetailSerializer
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
from .pagination import TimelinePageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'timelines': reverse('api_timelines:list', request=request, format=format),
        'new_timeline': reverse('api_timelines:create', request=request, format=format),
    })

class TimelineListAPIView(ListAPIView):
    serializer_class = TimelineListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'message']
    pagination_class = TimelinePageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        timelines = Timeline.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                timelines = timelines.filter(title__icontains=title)

            message = self.request.GET.get("message", "")
            if not message == "":
                timelines = timelines.filter(message__icontains=message)

        return timelines.distinct()

class TimelineCreateAPIView(CreateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TimelineRetrieveAPIView(RetrieveAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class TimelineUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class TimelineDeleteAPIView(DestroyAPIView):
    queryset = Timeline.objects.all()
    serializer_class = TimelineDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
