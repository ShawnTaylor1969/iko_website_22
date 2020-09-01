from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_eventschedules.models import EventSchedule
from api_calendars.models import Calendar
from api_eventtypes.models import EventType
from .tables import EventScheduleTable
from .forms import EventSchedule_CreateForm, EventSchedule_EditForm, EventSchedule_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def EventScheduleListView(request, calendar_pk):
    template_name = "web_eventschedules/eventschedule_list.html"

    calendar = Calendar.objects.get(pk=calendar_pk)
    space = calendar.space

    eventschedules = EventSchedule.objects.all().order_by('title')
    table = EventScheduleTable(eventschedules)
    context = {"table": table, "calendar": calendar, "space": space}
    return render(request, template_name, context)

def EventScheduleCreateView(request, calendar_pk):
    template_name = 'web_eventschedules/eventschedule_create.html'

    calendar = Calendar.objects.get(pk=calendar_pk)
    space = calendar.space

    # Add the General Event Type if there are no other choices
    eventtypes = EventType.objects.filter(space=space)
    if eventtypes.count() == 0:
        eventType = EventType(title='General', space=space)
        eventType.save()

    data = dict()
    if request.method == 'POST':
        eventschedule_form = EventSchedule_CreateForm(request.POST, request.FILES or None)
        if eventschedule_form.is_valid():
            eventschedule_form.save(commit=False)
            eventschedule_form.instance.calendar = calendar
            eventschedule_form.instance.organizer = request.user
            eventschedule_form.save(commit=True)
            return redirect(reverse('web_eventschedules:list', kwargs={"calendar_pk": eventschedule_form.instance.calendar.pk}))
    else:
        eventschedule_form = EventSchedule_CreateForm(initial={'start_dateTime': date.today(), 'end_dateTime': date.today()})

    print(eventschedule_form.non_field_errors)
    print(eventschedule_form.errors)

    context = {'eventschedule_form': eventschedule_form, "calendar": calendar, "space": space, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def EventScheduleReadView(request, pk):
    template_name = 'web_eventschedules/eventschedule_read.html'
    data = dict()
    eventschedule = get_object_or_404(EventSchedule, pk=pk)
    if request.method == 'POST':
        return redirect(reverse('web_eventschedules:list', kwargs={'calendar_pk': eventschedule.calendar.pk}))
    else:
        eventschedule_form = EventSchedule_ReadForm(instance=eventschedule)
    context = {'eventschedule_form': eventschedule_form, 'space': eventschedule.calendar.space, 'calendar': eventschedule.calendar, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def EventScheduleEditView(request, pk):
    template_name = 'web_eventschedules/eventschedule_edit.html'
    data = dict()
    eventschedule = get_object_or_404(EventSchedule, pk=pk)
    if request.method == 'POST':
        eventschedule_form = EventSchedule_EditForm(request.POST, request.FILES or None, instance=eventschedule)
        if eventschedule_form.is_valid():
            eventschedule.save()
            calendar= eventschedule.calendar
            print(calendar)
            return redirect(reverse('web_eventschedules:list', kwargs={'calendar_pk': eventschedule.calendar.pk}))
    else:
        eventschedule_form = EventSchedule_EditForm(instance=eventschedule)
    context = {'eventschedule_form': eventschedule_form, 'space': eventschedule.calendar.space, 'calendar': eventschedule.calendar, 'action_url': request.get_full_path()}
    print(context)
    return render(request, template_name, context)

def EventScheduleDeleteView(request, pk):
    template_name = 'web_eventschedules/modal_eventschedule_delete.html'
    data = dict()
    eventschedule = get_object_or_404(EventSchedule, pk=pk)
    if request.method == 'POST':
        eventschedule.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'eventschedule': eventschedule, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def EventScheduleMultipleDeleteView(request):
    template_name = 'web_eventschedules/modal_eventschedule_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    eventschedules = EventSchedule.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for eventschedule in eventschedules:
            eventschedule.delete()
        data['form_is_valid'] = True
    else:
        context ={'eventschedules': eventschedules,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
