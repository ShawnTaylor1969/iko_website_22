from django.urls import path
from . import views

app_name = 'api_pagedetails'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.PageDetailListAPIView.as_view(), name='list'),
    path('create/', views.PageDetailCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.PageDetailRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.PageDetailUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PageDetailDeleteAPIView.as_view(), name='delete'),
]
