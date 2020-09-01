from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_timelines'

urlpatterns = [
    path('list/', views.TimelineListView, name='list'),
]
