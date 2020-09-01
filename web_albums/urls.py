from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_albums'

urlpatterns = [
    path('<int:space_pk>/list/', views.AlbumListView, name='list'),
    path('<int:space_pk>/create/', views.AlbumCreateView, name='create'),
    path('<int:pk>/read/', views.AlbumEditView, name='read'),
    path('<int:pk>/edit/', views.AlbumEditView, name='edit'),
    path('<int:pk>/delete/', views.AlbumDeleteView, name='delete'),
    path('multipledelete/', views.AlbumMultipleDeleteView, name='multipledelete'),
]
