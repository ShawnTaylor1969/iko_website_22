from django.urls import path
from . import views

app_name = 'api_timelines'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.TimelineListAPIView.as_view(), name='list'),
    path('create/', views.TimelineCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.TimelineRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.TimelineUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TimelineDeleteAPIView.as_view(), name='delete'),
]
