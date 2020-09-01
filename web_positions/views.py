from django.shortcuts import render, get_object_or_404
from api_positions.models import Position
from .tables import PositionTable
from .forms import Position_CreateForm, Position_EditForm, Position_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def PositionListView(request):
    template_name = "web_positions/position_list.html"
    positions = Position.objects.all().order_by('title')
    table = PositionTable(positions)
    context = {"table": table}
    return render(request, template_name, context)

def PositionCreateView(request):
    template_name = 'web_positions/modal_position_create.html'
    data = dict()
    if request.method == 'POST':
        position_form = Position_CreateForm(request.POST)

        if position_form.is_valid():
            position_form.instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        position_form = Position_CreateForm()
    context = {'position_form': position_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PositionReadView(request, pk):
    template_name = 'web_positions/modal_position_read.html'
    data = dict()
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        position_form = Position_ReadForm(instance=position)
    context = {'position_form': position_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PositionEditView(request, pk):
    template_name = 'web_positions/modal_position_edit.html'
    data = dict()
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position_form = Position_EditForm(request.POST, instance=position)

        if position_form.is_valid():
            position.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        position_form = Position_EditForm(instance=position)
    context = {'position_form': position_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PositionDeleteView(request, pk):
    template_name = 'web_positions/modal_position_delete.html'
    data = dict()
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'position': position, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PositionMultipleDeleteView(request):
    template_name = 'web_positions/modal_position_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    positions = Position.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for position in positions:
            position.delete()
        data['form_is_valid'] = True
    else:
        context ={'positions': positions,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
