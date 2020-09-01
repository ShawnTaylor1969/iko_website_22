#models
from .models import PageDetail
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
    PageDetailListSerializer,
    PageDetailCreateUpdateSerializer,
    PageDetailDetailSerializer
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
from .pagination import PageDetailPageNumberPagination

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'pagedetails': reverse('api_pagedetails:list', request=request, format=format),
        'new_pagedetail': reverse('api_pagedetails:create', request=request, format=format),
    })

class PageDetailListAPIView(ListAPIView):
    serializer_class = PageDetailListSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    pagination_class = PageDetailPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pagedetails = PageDetail.objects.all()
        search = self.request.GET.get("search", "")
        if search == "":
            title = self.request.GET.get("title", "")
            if not title == "":
                pagedetails = pagedetails.filter(title__icontains=title)

            body = self.request.GET.get("body", "")
            if not body == "":
                pagedetails = pagedetails.filter(body__icontains=summary)

        return pagedetails.distinct()

class PageDetailCreateAPIView(CreateAPIView):
    queryset = PageDetail.objects.all()
    serializer_class = PageDetailCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PageDetailRetrieveAPIView(RetrieveAPIView):
    queryset = PageDetail.objects.all()
    serializer_class = PageDetailDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PageDetailUpdateAPIView(RetrieveUpdateAPIView):
    queryset = PageDetail.objects.all()
    serializer_class = PageDetailCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

class PageDetailDeleteAPIView(DestroyAPIView):
    queryset = PageDetail.objects.all()
    serializer_class = PageDetailDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
