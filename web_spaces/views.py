from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_spaces.models import Space
from api_walls.models import Wall
from web_walls.tables import WallTable
from .tables import SpaceTable
from .forms import Space_CreateForm, Space_EditForm, Space_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def space_default_homepage(request, pk):
    template_name = "web_spaces/space_default_homepage.html"
    space = Space.objects.get(pk=pk)

    if space.slug == "home-page":
        return redirect(reverse('home'))

    if space.user_space:
        template_name = "web_spaces/space_user_homepage.html"

    wall = Wall.objects.filter(space=space).order_by("-created_dateTime")
    table = WallTable(wall)

    context = {"space": space, "table": table}
    return render(request, template_name, context)

def SpaceListView(request):
    template_name = "web_spaces/space_list.html"
    spaces = Space.objects.all().order_by('title')
    table = SpaceTable(spaces)
    context = {"table": table}
    return render(request, template_name, context)

def SpaceCreateView(request):
    template_name = 'web_spaces/space_create.html'
    data = dict()
    if request.method == 'POST':
        space_form = Space_CreateForm(request.POST, request.FILES or None)
        if space_form.is_valid():
            space_form.instance.save()
            return redirect(reverse('web_spaces:list'))
    else:
        space_form = Space_CreateForm()
    context = {'space_form': space_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def SpaceReadView(request, pk):
    template_name = 'web_spaces/space_read.html'
    data = dict()
    space = get_object_or_404(Space, pk=pk)
    if request.method == 'POST':
        return redirect(reverse('web_spaces:list'))
    else:
        space_form = Space_ReadForm(instance=space)
    context = {'space_form': space_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def SpaceEditView(request, pk):
    template_name = 'web_spaces/space_edit.html'
    data = dict()
    space = get_object_or_404(Space, pk=pk)
    if request.method == 'POST':
        space_form = Space_EditForm(request.POST, request.FILES or None, instance=space)
        if space_form.is_valid():
            space_form.save()
            return redirect(reverse('web_spaces:list'))
    else:
        space_form = Space_EditForm(instance=space)
    context = {'space_form': space_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def SpaceDeleteView(request, pk):
    template_name = 'web_spaces/modal_space_delete.html'
    data = dict()
    space = get_object_or_404(Space, pk=pk)
    if request.method == 'POST':
        space.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'space': space, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def SpaceMultipleDeleteView(request):
    template_name = 'web_spaces/modal_space_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    spaces = Space.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for space in spaces:
            space.delete()
        data['form_is_valid'] = True
    else:
        context ={'spaces': spaces,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
