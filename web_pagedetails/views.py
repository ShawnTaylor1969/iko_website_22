from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_pagedetails.models import PageDetail
from api_spaces.models import Space
from .tables import PageDetailTable
from .forms import PageDetail_CreateForm, PageDetail_EditForm, PageDetail_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def PageDetailListView(request, space_pk):
    template_name = "web_pagedetails/pagedetail_list.html"

    space = Space.objects.get(pk=space_pk)

    pagedetails = PageDetail.objects.all().order_by('title')
    table = PageDetailTable(pagedetails)
    context = {"table": table, "space": space}
    return render(request, template_name, context)

def PageDetailCreateView(request, space_pk):
    template_name = 'web_pagedetails/pagedetail_create.html'

    space = Space.objects.get(pk=space_pk)

    data = dict()
    if request.method == 'POST':
        pagedetail_form = PageDetail_CreateForm(request.POST)
        if pagedetail_form.is_valid():
            pagedetail_form.save(commit=False)
            pagedetail_form.instance.space = space
            pagedetail_form.save(commit=True)
            return redirect(reverse('web_pagedetails:list', kwargs={'space_pk': space.pk}))
    else:
        pagedetail_form = PageDetail_CreateForm()
    context = {'pagedetail_form': pagedetail_form, "space": space, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def PageDetailReadView(request, pk):
    template_name = 'web_pagedetails/pagedetail_read.html'
    data = dict()
    pagedetail = get_object_or_404(PageDetail, pk=pk)
    if request.method == 'POST':
        return redirect(reverse('web_pagedetails:list', kwargs={'space_pk': space.pk}))
    else:
        pagedetail_form = PageDetail_ReadForm(instance=pagedetail)
    context = {'pagedetail_form': pagedetail_form, 'space': pagedetail.space, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def PageDetailEditView(request, pk):
    template_name = 'web_pagedetails/pagedetail_edit.html'
    data = dict()
    pagedetail = get_object_or_404(PageDetail, pk=pk)
    if request.method == 'POST':
        pagedetail_form = PageDetail_EditForm(request.POST, instance=pagedetail)
        if pagedetail_form.is_valid():
            pagedetail.save()
            print(pagedetail.space.pk)
            return redirect(reverse('web_pagedetails:list', kwargs={'space_pk': pagedetail.space.pk}))
    else:
        pagedetail_form = PageDetail_EditForm(instance=pagedetail)
    context = {'pagedetail_form': pagedetail_form, 'space': pagedetail.space, 'action_url': request.get_full_path()}
    return render(request, template_name, context)

def PageDetailDeleteView(request, pk):
    template_name = 'web_pagedetails/modal_pagedetail_delete.html'
    data = dict()
    pagedetail = get_object_or_404(PageDetail, pk=pk)
    if request.method == 'POST':
        pagedetail.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'pagedetail': pagedetail, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PageDetailMultipleDeleteView(request):
    template_name = 'web_pagedetails/modal_pagedetail_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    pagedetails = PageDetail.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for pagedetail in pagedetails:
            pagedetail.delete()
        data['form_is_valid'] = True
    else:
        context ={'pagedetails': pagedetails,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
