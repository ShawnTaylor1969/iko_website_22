from django.urls import path
from . import views

app_name = 'api_programs'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.ProgramListAPIView.as_view(), name='list'),
    path('create/', views.ProgramCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.ProgramRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.ProgramUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ProgramDeleteAPIView.as_view(), name='delete'),
]
