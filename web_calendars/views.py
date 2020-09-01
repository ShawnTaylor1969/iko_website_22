from django.shortcuts import render, get_object_or_404
from api_calendars.models import Calendar
from api_spaces.models import Space
from .tables import CalendarTable
from .forms import Calendar_CreateForm, Calendar_EditForm, Calendar_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def CalendarListView(request, space_pk):
    template_name = "web_calendars/calendar_list.html"

    space = Space.objects.get(pk=space_pk)

    calendars = Calendar.objects.all().order_by('title')
    table = CalendarTable(calendars)
    context = {"table": table, "space": space}
    return render(request, template_name, context)

def CalendarCreateView(request, space_pk):
    template_name = 'web_calendars/modal_calendar_create.html'

    space = Space.objects.get(pk=space_pk)

    data = dict()
    if request.method == 'POST':
        calendar_form = Calendar_CreateForm(request.POST)
        if calendar_form.is_valid():
            calendar_form.save(commit=False)
            calendar_form.instance.space = space
            calendar_form.instance.organizer = request.user
            calendar_form.save(commit=True)
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        calendar_form = Calendar_CreateForm()
    context = {'calendar_form': calendar_form, "space": space, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def CalendarReadView(request, pk):
    template_name = 'web_calendars/modal_calendar_read.html'
    data = dict()
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        calendar_form = Calendar_ReadForm(instance=calendar)
    context = {'calendar_form': calendar_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def CalendarEditView(request, pk):
    template_name = 'web_calendars/modal_calendar_edit.html'
    data = dict()
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        calendar_form = Calendar_EditForm(request.POST, instance=calendar)
        if calendar_form.is_valid():
            calendar.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        calendar_form = Calendar_EditForm(instance=calendar)
    context = {'calendar_form': calendar_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def CalendarDeleteView(request, pk):
    template_name = 'web_calendars/modal_calendar_delete.html'
    data = dict()
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        calendar.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'calendar': calendar, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def CalendarMultipleDeleteView(request):
    template_name = 'web_calendars/modal_calendar_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    calendars = Calendar.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for calendar in calendars:
            calendar.delete()
        data['form_is_valid'] = True
    else:
        context ={'calendars': calendars,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
