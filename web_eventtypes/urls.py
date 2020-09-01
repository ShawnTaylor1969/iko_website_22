from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_eventtypes'

urlpatterns = [
    path('<int:space_pk>/list/', views.EventTypeListView, name='list'),
    path('<int:space_pk>/create/', views.EventTypeCreateView, name='create'),
    path('<int:pk>/read/', views.EventTypeEditView, name='read'),
    path('<int:pk>/edit/', views.EventTypeEditView, name='edit'),
    path('<int:pk>/delete/', views.EventTypeDeleteView, name='delete'),
    path('multipledelete/', views.EventTypeMultipleDeleteView, name='multipledelete'),
]
