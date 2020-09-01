from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_groups'

urlpatterns = [
    path('list/', views.GroupListView, name='list'),
    path('create/', views.GroupCreateView, name='create'),
    path('<int:pk>/read/', views.GroupEditView, name='read'),
    path('<int:pk>/edit/', views.GroupEditView, name='edit'),
    path('<int:pk>/delete/', views.GroupDeleteView, name='delete'),
    path('multipledelete/', views.GroupMultipleDeleteView, name='multipledelete'),
]
