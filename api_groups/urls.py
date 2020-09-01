from django.urls import path
from . import views

app_name = 'api_groups'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.GroupListAPIView.as_view(), name='list'),
    path('create/', views.GroupCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.GroupRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.GroupUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.GroupDeleteAPIView.as_view(), name='delete'),
]
