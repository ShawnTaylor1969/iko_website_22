from django.shortcuts import render, get_object_or_404
from api_eventtypes.models import EventType
from api_spaces.models import Space
from .tables import EventTypeTable
from .forms import EventType_CreateForm, EventType_EditForm, EventType_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def EventTypeListView(request, space_pk):
    template_name = "web_eventtypes/eventtype_list.html"

    space = Space.objects.get(pk=space_pk)

    eventtypes = EventType.objects.all().order_by('title')
    table = EventTypeTable(eventtypes)
    context = {"table": table, "space": space}
    return render(request, template_name, context)

def EventTypeCreateView(request, space_pk):
    template_name = 'web_eventtypes/modal_eventtype_create.html'

    space = Space.objects.get(pk=space_pk)

    data = dict()
    if request.method == 'POST':
        eventtype_form = EventType_CreateForm(request.POST)
        if eventtype_form.is_valid():
            eventtype_form.save(commit=False)
            eventtype_form.instance.space = space
            eventtype_form.save(commit=True)
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        eventtype_form = EventType_CreateForm()
    context = {'eventtype_form': eventtype_form, "space": space, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def EventTypeReadView(request, pk):
    template_name = 'web_eventtypes/modal_eventtype_read.html'
    data = dict()
    eventtype = get_object_or_404(EventType, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        eventtype_form = EventType_ReadForm(instance=eventtype)
    context = {'eventtype_form': eventtype_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def EventTypeEditView(request, pk):
    template_name = 'web_eventtypes/modal_eventtype_edit.html'
    data = dict()
    eventtype = get_object_or_404(EventType, pk=pk)
    if request.method == 'POST':
        eventtype_form = EventType_EditForm(request.POST, instance=eventtype)
        if eventtype_form.is_valid():
            eventtype.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        eventtype_form = EventType_EditForm(instance=eventtype)
    context = {'eventtype_form': eventtype_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def EventTypeDeleteView(request, pk):
    template_name = 'web_eventtypes/modal_eventtype_delete.html'
    data = dict()
    eventtype = get_object_or_404(EventType, pk=pk)
    if request.method == 'POST':
        eventtype.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'eventtype': eventtype, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def EventTypeMultipleDeleteView(request):
    template_name = 'web_eventtypes/modal_eventtype_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    eventtypes = EventType.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for eventtype in eventtypes:
            eventtype.delete()
        data['form_is_valid'] = True
    else:
        context ={'eventtypes': eventtypes,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
