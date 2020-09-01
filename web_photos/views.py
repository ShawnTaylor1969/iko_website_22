from django.shortcuts import render, get_object_or_404
from api_albums.models import Album
from api_photos.models import Photo
from .tables import PhotoTable
from .forms import Photo_CreateForm, Photo_EditForm, Photo_ReadForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def PhotoListView(request, album_pk):
    template_name = "web_photos/photo_list.html"

    album = Album.objects.get(pk=album_pk)

    photos = Photo.objects.filter(album=album).order_by('title')
    table = PhotoTable(photos)
    context = {"table": table, "album": album}
    return render(request, template_name, context)

def PhotoCreateView(request, album_pk):
    template_name = 'web_photos/modal_photo_create.html'

    album = Album.objects.get(pk=album_pk)

    data = dict()
    if request.method == 'POST':
        photo_form = Photo_CreateForm(request.POST, request.FILES)
        files = request.FILES.getlist('picture')
        if photo_form.is_valid():
            for f in files:
                 file_instance = Photo(picture=f)
                 file_instance.album = album
                 file_instance.title = photo_form.instance.title
                 file_instance.summary = photo_form.instance.summary
                 file_instance.uploaded_by = request.user
                 file_instance.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        photo_form = Photo_CreateForm()
    context = {'photo_form': photo_form, "album": album, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PhotoReadView(request, pk):
    template_name = 'web_photos/modal_photo_read.html'
    data = dict()
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        data['form_is_valid'] = False
    else:
        photo_form = Photo_ReadForm(instance=photo)
    context = {'photo_form': photo_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PhotoEditView(request, pk):
    template_name = 'web_photos/modal_photo_edit.html'
    data = dict()
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo_form = Photo_EditForm(request.POST, request.FILES or None, instance=photo)
        if photo_form.is_valid():
            photo.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        photo_form = Photo_EditForm(instance=photo)
    context = {'photo_form': photo_form, 'action_url': request.get_full_path()}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PhotoDeleteView(request, pk):
    template_name = 'web_photos/modal_photo_delete.html'
    data = dict()
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
    else:
        context = {'photo': photo, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def PhotoMultipleDeleteView(request):
    template_name = 'web_photos/modal_photo_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('multlist')
    delete_pks = deleteList.split(":")
    photos = Photo.objects.filter(pk__in=delete_pks)

    if request.method == "POST":
        for photo in photos:
            photo.delete()
        data['form_is_valid'] = True
    else:
        context ={'photos': photos,  'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
