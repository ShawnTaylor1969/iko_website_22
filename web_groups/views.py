from django.shortcuts import render, get_object_or_404
from api_groups.models import Group
from .tables import GroupTable
from .forms import Group_CreateForm, Group_EditForm, Group_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def GroupListView(request):
    template_name = "web_groups/group_list.html"
    groups = Group.objects.all().order_by('title')
    table = GroupTable(groups)
    context = {"table": table}
    return render(request, template_name, context)

def GroupCreateView(request):
    template_name = 'web_groups/modal_group_create.html'
    data = dict()
    if request.method == 'POST':
        group_form = Group_CreateForm(request.POST)
        if group_form.is_valid():
            group_form.instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        group_form = Group_CreateForm()
    context = {'group_form': group_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def GroupReadView(request, pk):
    template_name = 'web_groups/modal_group_read.html'
    data = dict()
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        group_form = Group_ReadForm(instance=group)
    context = {'group_form': group_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def GroupEditView(request, pk):
    template_name = 'web_groups/modal_group_edit.html'
    data = dict()
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group_form = Group_EditForm(request.POST, instance=group)
        if group_form.is_valid():
            group.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        group_form = Group_EditForm(instance=group)
    context = {'group_form': group_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def GroupDeleteView(request, pk):
    template_name = 'web_groups/modal_group_delete.html'
    data = dict()
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'group': group, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def GroupMultipleDeleteView(request):
    template_name = 'web_groups/modal_group_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    groups = Group.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for group in groups:
            group.delete()
        data['form_is_valid'] = True
    else:
        context ={'groups': groups,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
