#models
from .models import Calendar
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
    CalendarListSerializer,
    CalendarCreateUpdateSerializer,
    CalendarDetailSerializer
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
from .pagination import CalendarPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'calendars': reverse('api_calendars:list', request=request, format=format),
        'new_calendar': reverse('api_calendars:create', request=request, format=format),
    })

class CalendarListAPIView(ListAPIView):
    serializer_class = CalendarListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary']
    pagination_class = CalendarPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        calendars = Calendar.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                calendars = calendars.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not summary == "":
                calendars = calendars.filter(summary__icontains=summary)

        return calendars.distinct()

class CalendarCreateAPIView(CreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class CalendarRetrieveAPIView(RetrieveAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CalendarUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class CalendarDeleteAPIView(DestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
