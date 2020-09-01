from django.urls import path
from . import views

app_name = 'api_articles'

urlpatterns = [
    path('', views.api_root),
    path('list/', views.ArticleListAPIView.as_view(), name='list'),
    path('create/', views.ArticleCreateAPIView.as_view(), name='create'),
    path('<int:pk>/read/', views.ArticleRetrieveAPIView.as_view(), name='read'),
    path('<int:pk>/edit/', views.ArticleUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', views.ArticleDeleteAPIView.as_view(), name='delete'),
]
