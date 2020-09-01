from django.urls import path
from . import views

app_name = 'api_spaces'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.SpaceListAPIView.as_view(), name='list'),
    path('create/', views.SpaceCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.SpaceRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.SpaceUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.SpaceDeleteAPIView.as_view(), name='delete'),
]
