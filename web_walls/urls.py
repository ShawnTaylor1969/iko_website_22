from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_walls'

urlpatterns = [
    path('<int:space_pk>/list/', views.WallListView, name='list'),
    path('<int:space_pk>/create/', views.WallCreateView, name='create'),
    path('<int:pk>/read/', views.WallEditView, name='read'),
    path('<int:pk>/edit/', views.WallEditView, name='edit'),
    path('<int:pk>/delete/', views.WallDeleteView, name='delete'),
    path('multipledelete/', views.WallMultipleDeleteView, name='multipledelete'),
]
