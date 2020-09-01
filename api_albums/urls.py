from django.urls import path
from . import views

app_name = 'api_albums'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.AlbumListAPIView.as_view(), name='list'),
    path('create/', views.AlbumCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.AlbumRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.AlbumUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AlbumDeleteAPIView.as_view(), name='delete'),
]
