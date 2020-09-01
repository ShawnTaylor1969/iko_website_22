#models
from django.contrib.auth.models import User
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
    UserListSerializer,
    UserCreateUpdateSerializer,
    UserDetailSerializer
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
from .pagination import UserPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api_users:list', request=request, format=format),
        'new_user': reverse('api_users:create', request=request, format=format),
    })

class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['username', 'first_name', 'last_name']
    pagination_class = UserPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        users = User.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            username = self.request.GET.get("username", "")
            if not username == "":
                users = users.filter(username__icontains=title)

            # publications = self.request.GET.get("publications", "")
            # if len(publications) > 0:
            #     str_pks = publications.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         publication = Publication.objects.get(pk=int(pk))
            #         pks.append(publication)
            #     users = users.filter(publication__in=pks)
            #
            # authors = self.request.GET.get("authors", "")
            # if len(authors) > 0:
            #     str_pks = authors.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         author = User.objects.get(pk=int(pk))
            #         pks.append(author)
            #     users = users.filter(author__in=pks)

            # publication_dateTime_start = self.request.GET.get("publication_dateTime_start", "")
            # if len(publication_dateTime_start) > 0:
            #     users = users.filter(publication_dateTime__gte=date(int(publication_dateTime_start[0:4]), int(publication_dateTime_start[5:7]), int(publication_dateTime_start[8:10])))
            #
            # publication_dateTime_end = self.request.GET.get("publication_dateTime_end", "")
            # if len(publication_dateTime_end) > 0:
            #     users = users.filter(publication_dateTime__gte=date(int(publication_dateTime_end[0:4]), int(publication_dateTime_end[5:7]), int(publication_dateTime_end[8:10])))

        return users.distinct()

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
