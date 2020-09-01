from django.urls import path
from . import views

app_name = 'api_photos'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.PhotoListAPIView.as_view(), name='list'),
    path('create/', views.PhotoCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.PhotoRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.PhotoUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PhotoDeleteAPIView.as_view(), name='delete'),
]
