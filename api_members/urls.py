from django.urls import path
from . import views

app_name = 'api_members'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.MemberListAPIView.as_view(), name='list'),
    path('create/', views.MemberCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.MemberRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.MemberUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.MemberDeleteAPIView.as_view(), name='delete'),
]
