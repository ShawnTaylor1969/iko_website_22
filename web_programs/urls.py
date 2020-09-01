from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_programs'

urlpatterns = [
    path('list/', views.ProgramListView, name='list'),
    path('create', views.ProgramCreateView, name='create'),
    path('<int:pk>/read/', views.ProgramEditView, name='read'),
    path('<int:pk>/edit/', views.ProgramEditView, name='edit'),
    path('<int:pk>/delete/', views.ProgramDeleteView, name='delete'),
    path('multipledelete/', views.ProgramMultipleDeleteView, name='multipledelete'),
]
