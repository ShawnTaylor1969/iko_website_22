from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_eventschedules'

urlpatterns = [
    path('<int:calendar_pk>/list/', views.EventScheduleListView, name='list'),
    path('<int:calendar_pk>/create', views.EventScheduleCreateView, name='create'),
    path('<int:pk>/read/', views.EventScheduleEditView, name='read'),
    path('<int:pk>/edit/', views.EventScheduleEditView, name='edit'),
    path('<int:pk>/delete/', views.EventScheduleDeleteView, name='delete'),
    path('multipledelete/', views.EventScheduleMultipleDeleteView, name='multipledelete'),
]
