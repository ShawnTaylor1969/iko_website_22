from django.shortcuts import render, get_object_or_404
from api_walls.models import Wall
from api_spaces.models import Space
from .tables import WallTable
from .forms import Wall_CreateForm, Wall_EditForm, Wall_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def WallListView(request, space_pk):
    template_name = "web_walls/wall_list.html"

    space = Space.objects.get(pk=space_pk)

    walls = Wall.objects.all().order_by('-created_dateTime')
    table = WallTable(walls)
    context = {"table": table, "space": space}
    return render(request, template_name, context)

def WallCreateView(request, space_pk):
    template_name = 'web_walls/modal_wall_create.html'

    space = Space.objects.get(pk=space_pk)

    data = dict()
    if request.method == 'POST':
        wall_form = Wall_CreateForm(request.POST, request.FILES or None)
        if wall_form.is_valid():
            wall_form.save(commit=False)
            wall_form.instance.space = space
            wall_form.instance.created_by = request.user
            wall_form.save(commit=True)
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        wall_form = Wall_CreateForm()
    context = {'wall_form': wall_form, "space": space, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def WallReadView(request, pk):
    template_name = 'web_walls/modal_wall_read.html'
    data = dict()
    wall = get_object_or_404(Wall, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        wall_form = Wall_ReadForm(instance=wall)
    context = {'wall_form': wall_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def WallEditView(request, pk):
    template_name = 'web_walls/modal_wall_edit.html'
    data = dict()
    wall = get_object_or_404(Wall, pk=pk)
    if request.method == 'POST':
        wall_form = Wall_EditForm(request.POST, request.FILES or None, instance=wall)
        if wall_form.is_valid():
            wall.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        wall_form = Wall_EditForm(instance=wall)
    context = {'wall_form': wall_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def WallDeleteView(request, pk):
    template_name = 'web_walls/modal_wall_delete.html'
    data = dict()
    wall = get_object_or_404(Wall, pk=pk)
    if request.method == 'POST':
        wall.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'wall': wall, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def WallMultipleDeleteView(request):
    template_name = 'web_walls/modal_wall_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    walls = Wall.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for wall in walls:
            wall.delete()
        data['form_is_valid'] = True
    else:
        context ={'walls': walls,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
