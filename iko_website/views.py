from django.views.generic import View, TemplateView
from django.shortcuts import render, get_object_or_404
from api_members.models import Member
from api_photos.models import Photo
from api_events.models import Event
from api_pagedetails.models import PageDetail
from random import shuffle
from datetime import timedelta, date
from django.db.models import Q

# Create your views here.
def HomePage(request):
    template_name = 'index.html'
    main_area_public = PageDetail.objects.get(slug='home-page-main-area-public')

    # Get Featured Content List
    # featuredContentArea = FeaturedContentArea.objects.filter(space=Space.objects.get(slug='home-page'), slug='home-page-featured-content-list')
    # home_page_featured_content_list = Content.objects.filter(site_featured_content_area__in=featuredContentArea).order_by('-created_dateTime')

    today = date.today()
    fifteen_days = today + timedelta(days=15)
    birthdays = Member.objects.all()
    if today.month == fifteen_days.month:
        birthdays = birthdays.filter(
            birth_date__month=today.month,
            birth_date__day__gte=today.day,
            birth_date__day__lte=fifteen_days.day,
        )
    else:
        birthdays = birthdays.filter(
            Q(birth_date__month=today.month, birth_date__day__gte=fifteen_days.day) |
            Q(birth_date__month=fifteen_days.month, birth_date__day__lte=fifteen_days.day)
        )

    if birthdays.count() > 5:
        birthdays = birthdays[:5]

    # Get Featured Events
    featured_events = Event.objects.all().order_by('start_dateTime')
    print(featured_events)
    #
    # Get collage pictures
    collage_contents = Photo.objects.filter(album__slug='site-administration-home-page-banner')
    collage_list = list(collage_contents)
    shuffle(collage_list)
    #
    # content_types = ContentType.objects.filter(active=True).order_by("title")
    #
    # section_links = TreeItem.objects.filter(root__slug="home-page-links").order_by("sequence")
    #
    # context = {"collage_contents": collage_list, "section_links": section_links, "home_page_main_featured_content": home_page_main_featured_content, "home_page_featured_content_list": home_page_featured_content_list, "birthdays": birthdays, "featured_events": featured_events, "content_types": content_types}
    context = {"collage_contents": collage_list, "main_area_public": main_area_public, "birthdays": birthdays, "featured_events": featured_events}
    return render(request, template_name, context)

def HomeNews(request):
    template_name = 'index_news.html'
    # Get Featured News and Announcements
    article_space_list = []
    contentSpaces = ContentSpace.objects.filter(content_type__slug='articles')
    for contentSpace in contentSpaces:
        if contentSpace.content_community.is_authorized(request.user):
            article_space_list.append(contentSpace)
        else:
            article_space_list.append(contentSpace)
    featured_articles = Content.objects.filter(featured=True, content_space__in=article_space_list).order_by('-id')

    # Get Featured Events
    event_space_list = []
    contentSpaces = ContentSpace.objects.filter(content_type__slug='events')
    for contentSpace in contentSpaces:
        if contentSpace.content_community.is_authorized(request.user):
            event_space_list.append(contentSpace)
    featured_events = Content.objects.filter(featured=True, content_space__in=event_space_list)

    # Get collage pictures
    collage_contents = Content.objects.filter(content_space__slug='home-page-collage')
    collage_list = list(collage_contents)
    shuffle(collage_list)

    context = {"featured_articles": featured_articles, "featured_events": featured_events, "collage_contents": collage_list}
    return render(request, template_name, context)

# def cssgrid(request):
#     template_name = "cssgrid.html"
#     context = {}
#     return render(request, template_name, context)
#
# class SiteTree(TemplateView):
#     template_name = 'sitetree/menu.html'
#
# class ComingSoon(TemplateView):
#     template_name = 'comingsoon.html'
