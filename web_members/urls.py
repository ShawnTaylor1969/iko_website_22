from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'web_members'

urlpatterns = [
    path('list/', views.MemberListView, name='list'),
    path('<int:pk>/read/', views.MemberEditView, name='read'),
    path('<int:pk>/edit/', views.MemberEditView, name='edit'),
    path('<int:pk>/editmember/', views.EditMemberView, name='edit_member'),
    path('<int:pk>/delete/', views.MemberDeleteView, name='delete'),
    path('multipledelete/', views.MemberMultipleDeleteView, name='multipledelete'),

    path('sisters/', views.SisterListView, name='sisters'),
    path('sisters_filters', views.sisters_filters, name='sisters_filter'),
]
