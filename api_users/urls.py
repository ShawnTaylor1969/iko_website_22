from django.urls import path
from . import views

app_name = 'api_users'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.UserListAPIView.as_view(), name='list'),
    path('create/', views.UserCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.UserRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.UserUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.UserDeleteAPIView.as_view(), name='delete'),
]
