from django.urls import path
from . import views

app_name = 'api_configurations'

urlpatterns = [
    path('', views.api_root),
    path('read/', views.ConfigurationRetrieveAPIView.as_view(), name='read'),
    path('edit/', views.ConfigurationUpdateAPIView.as_view(), name='update'),
]
