from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_programs.models import Program
from .tables import ProgramTable
from .forms import Program_CreateForm, Program_EditForm, Program_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def ProgramListView(request):
    template_name = "web_programs/program_list.html"
    programs = Program.objects.all().order_by('title')
    table = ProgramTable(programs)
    context = {"table": table}
    return render(request, template_name, context)

def ProgramCreateView(request):
    template_name = 'web_programs/program_create.html'
    data = dict()
    if request.method == 'POST':
        program_form = Program_CreateForm(request.POST)
        if program_form.is_valid():
            program_form.instance.save()
            return redirect(reverse('web_programs:list'))
    else:
        program_form = Program_CreateForm()
    context = {'program_form': program_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def ProgramReadView(request, pk):
    template_name = 'web_programs/program_read.html'
    data = dict()
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        return redirect(reverse('web_programs:list'))
    else:
        program_form = Program_ReadForm(instance=program)
    context = {'program_form': program_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def ProgramEditView(request, pk):
    template_name = 'web_programs/program_edit.html'
    data = dict()
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program_form = Program_EditForm(request.POST, instance=program)
        if program_form.is_valid():
            program.save()
            return redirect(reverse('web_programs:list'))
    else:
        program_form = Program_EditForm(instance=program)
    context = {'program_form': program_form, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def ProgramDeleteView(request, pk):
    template_name = 'web_programs/modal_program_delete.html'
    data = dict()
    program = get_object_or_404(Program, pk=pk)
    if request.method == 'POST':
        program.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'program': program, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def ProgramMultipleDeleteView(request):
    template_name = 'web_programs/modal_program_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    programs = Program.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for program in programs:
            program.delete()
        data['form_is_valid'] = True
    else:
        context ={'programs': programs,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
