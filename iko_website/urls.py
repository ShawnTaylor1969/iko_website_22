"""iko_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from web_authentication import views as authentication_views
from web_members import views as member_views
from web_members.forms import CustomAuthenticationForm
from . import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', member_views.CreateUser_View.as_view(), name='sign_up'),
    path('login/', auth_views.LoginView.as_view(
            template_name='web_authentication/login.html',
            authentication_form=CustomAuthenticationForm,
            extra_context={
              'title': 'Login',
              'site_title': 'My Site',
              'site_header': 'My Site Login'}), name='log_in'),
    path('logout/', authentication_views.user_logout, name='log_out'),
    path('summernote/', include('django_summernote.urls')),
    path('authentication/', include('web_authentication.urls', namespace='web_authentication')),

    path('api/configurations/', include('api_configurations.urls', namespace='api_configurations')),
    path('api/contenttypes/', include('api_contenttypes.urls', namespace='api_contenttypes')),
    path('api/spaces/', include('api_spaces.urls', namespace='api_spaces')),
    path('api/programs/', include('api_programs.urls', namespace='api_programs')),
    path('api/spacelinks/', include('api_spacelinks.urls', namespace='api_spacelinks')),
    path('api/groups/', include('api_groups.urls', namespace='api_groups')),
    path('api/positions/', include('api_positions.urls', namespace='api_positions')),
    path('api/notifications/', include('api_notifications.urls', namespace='api_notifications')),
    path('api/timelines/', include('api_timelines.urls', namespace='api_timelines')),
    path('api/wall/', include('api_walls.urls', namespace='api_walls')),
    path('api/users/', include('api_users.urls', namespace='api_users')),
    path('api/members/', include('api_members.urls', namespace='api_members')),
    path('api/articles/', include('api_articles.urls', namespace='api_articles')),
    path('api/albums/', include('api_albums.urls', namespace='api_albums')),
    path('api/photos/', include('api_photos.urls', namespace='api_photos')),
    path('api/pagedetails/', include('api_pagedetails.urls', namespace='api_pagedetails')),
    path('api/calendars/', include('api_calendars.urls', namespace='api_calendars')),

    path('members/', include('web_members.urls', namespace='web_members')),
    path('positions/', include('web_positions.urls', namespace='web_positions')),
    path('groups/', include('web_groups.urls', namespace='web_groups')),
    path('spaces/', include('web_spaces.urls', namespace='web_spaces')),
    path('programs/', include('web_programs.urls', namespace='web_programs')),
    path('notifications/', include('web_notifications.urls', namespace='web_notifications')),

    path('albums/', include('web_albums.urls', namespace='web_albums')),
    path('photos/', include('web_photos.urls', namespace='web_photos')),
    path('pagedetails/', include('web_pagedetails.urls', namespace='web_pagedetails')),

    path('calendars/', include('web_calendars.urls', namespace='web_calendars')),
    path('eventtypes/', include('web_eventtypes.urls', namespace='web_eventtypes')),
    path('eventschedules/', include('web_eventschedules.urls', namespace='web_eventschedules')),

    path('wall/', include('web_walls.urls', namespace='web_walls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
