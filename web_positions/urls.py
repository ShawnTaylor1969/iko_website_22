from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_positions'

urlpatterns = [
    path('list/', views.PositionListView, name='list'),
    path('create/', views.PositionCreateView, name='create'),
    path('<int:pk>/read/', views.PositionEditView, name='read'),
    path('<int:pk>/edit/', views.PositionEditView, name='edit'),
    path('<int:pk>/delete/', views.PositionDeleteView, name='delete'),
    path('multipledelete/', views.PositionMultipleDeleteView, name='multipledelete'),
]
