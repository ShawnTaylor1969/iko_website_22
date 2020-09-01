from .models import Configuration
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication
    )
from .serializers import (
    ConfigurationCreateUpdateSerializer,
    ConfigurationDetailSerializer
    )
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.reverse import reverse



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'read_configuration': reverse('api_configurations:read', request=request, format=format),
        'edit_configuration': reverse('api_configurations:update', request=request, format=format),
    })

class ConfigurationRetrieveAPIView(RetrieveAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationDetailSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]

    def get_object(self):
        queryset = self.get_queryset()
        configurations = Configuration.objects.all()
        if len(configurations) == 0:
            configuration = Configuration(organization_name='Default Organization', domain_name='www.defaultorg.xxx')
            configuration.save()
        else:
            configuration = configurations.first()
        return configuration

class ConfigurationUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationCreateUpdateSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        configurations = Configuration.objects.all()
        if len(configurations) == 0:
            configuration = Configuration(organization_name='Default Organization', domain_name='www.defaultorg.xxx')
            configuration.save()
        else:
            configuration = configurations.first()
        return configuration
