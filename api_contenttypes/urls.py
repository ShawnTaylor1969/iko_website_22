from django.urls import path
from . import views

app_name = 'api_contenttypes'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.ContentTypeListAPIView.as_view(), name='list'),
    path('create/', views.ContentTypeCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.ContentTypeRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.ContentTypeUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ContentTypeDeleteAPIView.as_view(), name='delete'),
]
