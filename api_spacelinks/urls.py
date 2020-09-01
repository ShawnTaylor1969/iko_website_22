from django.urls import path
from . import views

app_name = 'api_spacelinks'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.SpaceLinkListAPIView.as_view(), name='list'),
    path('create/', views.SpaceLinkCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.SpaceLinkRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.SpaceLinkUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SpaceLinkDeleteAPIView.as_view(), name='delete'),
]
