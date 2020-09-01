from django.urls import path
from . import views

app_name = 'api_eventtypes'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.EventTypeListAPIView.as_view(), name='list'),
    path('create/', views.EventTypeCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.EventTypeRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.EventTypeUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.EventTypeDeleteAPIView.as_view(), name='delete'),
]
