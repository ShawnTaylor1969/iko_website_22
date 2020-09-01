from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_pagedetails'

urlpatterns = [
    path('<int:space_pk>/list/', views.PageDetailListView, name='list'),
    path('<int:space_pk>/create', views.PageDetailCreateView, name='create'),
    path('<int:pk>/read/', views.PageDetailEditView, name='read'),
    path('<int:pk>/edit/', views.PageDetailEditView, name='edit'),
    path('<int:pk>/delete/', views.PageDetailDeleteView, name='delete'),
    path('multipledelete/', views.PageDetailMultipleDeleteView, name='multipledelete'),
]
