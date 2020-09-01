from django.urls import path
from . import views

app_name = 'api_calendars'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.CalendarListAPIView.as_view(), name='list'),
    path('create/', views.CalendarCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.CalendarRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.CalendarUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.CalendarDeleteAPIView.as_view(), name='delete'),
]
