from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_calendars'

urlpatterns = [
    path('<int:space_pk>/list/', views.CalendarListView, name='list'),
    path('<int:space_pk>/create/', views.CalendarCreateView, name='create'),
    path('<int:pk>/read/', views.CalendarEditView, name='read'),
    path('<int:pk>/edit/', views.CalendarEditView, name='edit'),
    path('<int:pk>/delete/', views.CalendarDeleteView, name='delete'),
    path('multipledelete/', views.CalendarMultipleDeleteView, name='multipledelete'),
]
