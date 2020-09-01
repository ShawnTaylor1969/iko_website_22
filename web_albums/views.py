from django.shortcuts import render, get_object_or_404
from api_albums.models import Album
from api_spaces.models import Space
from .tables import AlbumTable
from .forms import Album_CreateForm, Album_EditForm, Album_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def AlbumListView(request, space_pk):
    template_name = "web_albums/album_list.html"

    space = Space.objects.get(pk=space_pk)

    albums = Album.objects.filter(space=space).order_by('title')
    table = AlbumTable(albums)
    context = {"table": table, "space": space}
    return render(request, template_name, context)

def AlbumCreateView(request, space_pk):
    template_name = 'web_albums/modal_album_create.html'

    space = Space.objects.get(pk=space_pk)

    data = dict()
    if request.method == 'POST':
        album_form = Album_CreateForm(request.POST, request.FILES or None)
        if album_form.is_valid():
            album_form.save(commit=False)
            album_form.instance.space = space
            album_form.instance.author = request.user
            album_form.save(commit=True)
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        album_form = Album_CreateForm()
    context = {'album_form': album_form, "space": space, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def AlbumReadView(request, pk):
    template_name = 'web_albums/modal_album_read.html'
    data = dict()
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        album_form = Album_ReadForm(instance=album)
    context = {'album_form': album_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def AlbumEditView(request, pk):
    template_name = 'web_albums/modal_album_edit.html'
    data = dict()
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        print(request.FILES)
        album_form = Album_EditForm(request.POST, request.FILES or None, instance=album)
        if album_form.is_valid():
            album.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        album_form = Album_EditForm(instance=album)
    context = {'album_form': album_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def AlbumDeleteView(request, pk):
    template_name = 'web_albums/modal_album_delete.html'
    data = dict()
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'album': album, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def AlbumMultipleDeleteView(request):
    template_name = 'web_albums/modal_album_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    albums = Album.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for album in albums:
            album.delete()
        data['form_is_valid'] = True
    else:
        context ={'albums': albums,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
