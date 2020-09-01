from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_timelines.models import Timeline
from .tables import TimelineTable
from .forms import Timeline_CreateForm, Timeline_EditForm, Timeline_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def TimelineListView(request):
    template_name = "web_timelines/timeline_list.html"
    timelines = Timeline.objects.all().order_by('created_dateTime')
    table = TimelineTable(timelines)
    context = {"table": table}
    return render(request, template_name, context)
    
