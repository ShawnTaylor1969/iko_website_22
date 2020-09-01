from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_notifications'

urlpatterns = [
    path('list/', views.notification_list, name='notifications'),
    path('<int:pk>/delete', views.notification_delete, name='notification_delete'),
    path('multipledelete/', views.notification_multipledelete, name='notification_multipledelete'),
]
