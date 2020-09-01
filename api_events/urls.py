from django.urls import path
from . import views

app_name = 'api_events'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.EventListAPIView.as_view(), name='list'),
    path('create/', views.EventCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.EventRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.EventUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventDeleteAPIView.as_view(), name='delete'),
]
