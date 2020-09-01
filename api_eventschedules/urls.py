from django.urls import path
from . import views

app_name = 'api_eventschedules'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.EventScheduleListAPIView.as_view(), name='list'),
    path('create/', views.EventScheduleCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.EventScheduleRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.EventScheduleUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventScheduleDeleteAPIView.as_view(), name='delete'),
]
