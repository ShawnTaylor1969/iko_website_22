from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_spaces'

urlpatterns = [
    path('list/', views.SpaceListView, name='list'),
    path('create', views.SpaceCreateView, name='create'),
    path('<int:pk>/read/', views.SpaceEditView, name='read'),
    path('<int:pk>/edit/', views.SpaceEditView, name='edit'),
    path('<int:pk>/delete/', views.SpaceDeleteView, name='delete'),
    path('multipledelete/', views.SpaceMultipleDeleteView, name='multipledelete'),
    path('<int:pk>/homepage/', views.space_default_homepage, name='homepage'),

]
