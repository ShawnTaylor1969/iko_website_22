#models
from .models import Member
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
    MemberListSerializer,
    MemberCreateUpdateSerializer,
    MemberDetailSerializer
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
from .pagination import MemberPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'members': reverse('api_members:list', request=request, format=format),
        'new_member': reverse('api_members:create', request=request, format=format),
    })

class MemberListAPIView(ListAPIView):
    serializer_class = MemberListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'about_me']
    pagination_class = MemberPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        members = Member.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            first_name = self.request.GET.get("first_name", "")
            if not first_name == "":
                members = members.filter(first_name__icontains=first_name)

            # publications = self.request.GET.get("publications", "")
            # if len(publications) > 0:
            #     str_pks = publications.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         publication = Publication.objects.get(pk=int(pk))
            #         pks.append(publication)
            #     members = members.filter(publication__in=pks)
            #
            # authors = self.request.GET.get("authors", "")
            # if len(authors) > 0:
            #     str_pks = authors.split(",")
            #     pks = []
            #     for pk in str_pks:
            #         author = User.objects.get(pk=int(pk))
            #         pks.append(author)
            #     members = members.filter(author__in=pks)

            # publication_dateTime_start = self.request.GET.get("publication_dateTime_start", "")
            # if len(publication_dateTime_start) > 0:
            #     members = members.filter(publication_dateTime__gte=date(int(publication_dateTime_start[0:4]), int(publication_dateTime_start[5:7]), int(publication_dateTime_start[8:10])))
            #
            # publication_dateTime_end = self.request.GET.get("publication_dateTime_end", "")
            # if len(publication_dateTime_end) > 0:
            #     members = members.filter(publication_dateTime__gte=date(int(publication_dateTime_end[0:4]), int(publication_dateTime_end[5:7]), int(publication_dateTime_end[8:10])))

        return members.distinct()

class MemberCreateAPIView(CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class MemberRetrieveAPIView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class MemberUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class MemberDeleteAPIView(DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
