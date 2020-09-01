from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_photos'

urlpatterns = [
    path('<int:album_pk>/list/', views.PhotoListView, name='list'),
    path('<int:album_pk>/create/', views.PhotoCreateView, name='create'),
    path('<int:pk>/read/', views.PhotoEditView, name='read'),
    path('<int:pk>/edit/', views.PhotoEditView, name='edit'),
    path('<int:pk>/delete/', views.PhotoDeleteView, name='delete'),
    path('multipledelete/', views.PhotoMultipleDeleteView, name='multipledelete'),
]
