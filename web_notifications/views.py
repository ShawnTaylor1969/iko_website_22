from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from api_notifications.models import Notification
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from datetime import date

def notification_list(request):
    template_name = "web_notifications/notifications.html"
    notifications = Notification.objects.filter(notify_user=request.user, cleared=False).order_by('-created_dateTime')

    context = {'notifications': notifications, 'modal_lg': 'True'}
    return render(request, template_name, context)

def notification_delete(request, pk):
    template_name = 'web_notifications/modal_notification_delete.html'
    data = dict()
    notification = get_object_or_404(Notification, pk=pk)
    if request.method == 'POST':
        notification.delete()
        data['form_is_valid'] = True
    else:
        context = {'notification': notification, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def notification_multipledelete(request):
    template_name = 'web_notifications/modal_notification_multipledelete.html'
    data = dict()
    deleteList = request.GET.get('deletelist')
    delete_pks = deleteList.split(":")
    notifications = Notification.objects.filter(pk__in=delete_pks).order_by('-created_dateTime')

    if request.method == "POST":
        notifications.delete()
        data['form_is_valid'] = True
    else:
        context ={'notifications': notifications, 'deletelist': deleteList, 'action_url': request.get_full_path()}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)
