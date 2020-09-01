#models
from .models import Notification
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
    NotificationListSerializer,
    NotificationCreateUpdateSerializer,
    NotificationDetailSerializer
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
from .pagination import NotificationPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'notifications': reverse('api_notifications:list', request=request, format=format),
        'new_notification': reverse('api_notifications:create', request=request, format=format),
    })

class NotificationListAPIView(ListAPIView):
    serializer_class = NotificationListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['message', 'content']
    pagination_class = NotificationPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        notifications = Notification.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            message = self.request.GET.get("message", "")
            if not message == "":
                notifications = notifications.filter(message__icontains=title)

            content = self.request.GET.get("content", "")
            if not content == "":
                notifications = notifications.filter(content__icontains=summary)

        return notifications.distinct()

class NotificationCreateAPIView(CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class NotificationRetrieveAPIView(RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class NotificationUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class NotificationDeleteAPIView(DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
