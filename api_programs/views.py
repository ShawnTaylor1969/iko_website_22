#models
from .models import Program
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
    ProgramListSerializer,
    ProgramCreateUpdateSerializer,
    ProgramDetailSerializer
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
from .pagination import ProgramPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'programs': reverse('api_programs:list', request=request, format=format),
        'new_program': reverse('api_programs:create', request=request, format=format),
    })

class ProgramListAPIView(ListAPIView):
    serializer_class = ProgramListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'summary', 'body']
    pagination_class = ProgramPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        programs = Program.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                programs = programs.filter(title__icontains=title)

            summary = self.request.GET.get("summary", "")
            if not title == "":
                programs = programs.filter(summary__icontains=summary)

        return programs.distinct()

class ProgramCreateAPIView(CreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProgramRetrieveAPIView(RetrieveAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProgramUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ProgramDeleteAPIView(DestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
