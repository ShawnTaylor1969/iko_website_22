from django.urls import path
from . import views

app_name = 'api_walls'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.WallListAPIView.as_view(), name='list'),
    path('create/', views.WallCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.WallRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.WallUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.WallDeleteAPIView.as_view(), name='delete'),
]
