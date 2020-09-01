from django.urls import path
from . import views

app_name = 'api_positions'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.PositionListAPIView.as_view(), name='list'),
    path('create/', views.PositionCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.PositionRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.PositionUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PositionDeleteAPIView.as_view(), name='delete'),
]
