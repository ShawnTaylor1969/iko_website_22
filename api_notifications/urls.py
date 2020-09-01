from django.urls import path
from . import views

app_name = 'api_notifications'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.NotificationListAPIView.as_view(), name='list'),
    path('create/', views.NotificationCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.NotificationRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.NotificationUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NotificationDeleteAPIView.as_view(), name='delete'),
]
