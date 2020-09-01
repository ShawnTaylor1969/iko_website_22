from django.db import models
from datetime import timedelta, datetime
from django.utils import timezone
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Notification(models.Model):
    notify_user                   = models.ForeignKey(User, on_delete= models.CASCADE,related_name='notifications')
    source_user                   = models.ForeignKey(User, on_delete= models.CASCADE,related_name='source_of_notification')
    token                         = models.CharField(max_length=128, blank=True, default='', null=True)
    message                       = models.TextField(default='')
    content_app_id                = models.CharField(max_length=128, blank=True, default='', null=True)
    content_slug                  = models.SlugField(max_length=200, blank=True, default='', null=True)
    cleared                       = models.BooleanField(default=False)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=False, null=True)
    cleared_dateTime              = models.DateTimeField("Closed", auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.message

    def add_notification(notify_user=None, source_user=None, message=None, token=None, content=None, created_dateTime=timezone.now()):
        # If the content url is blank, then it is a straight message and needs to be created straight up.
        # otherwise, the message should be combined with a preceding message to reduce message overloading.
        if not content:
            notification = Notification(notify_user=notify_user, source_user=source_user, message=message, token=token)
            notification.save()
        else:
            notifications = Notification.objects.filter(notify_user=notify_user, content=content, cleared=False)
            if (notifications.count() > 0):
                notification = notifications[0]
                notification.source_user = source_user
                notification.message = message
                notification.created_dateTime = created_dateTime
                notification.save()
                notification_detail = NotificationDetail(notification=notification, source_user=source_user, message=message, created_dateTime=notification.created_dateTime)
                notification_detail.save()
            else:
                notification = Notification(notify_user=notify_user, source_user=source_user, message=message, content=content, created_dateTime=created_dateTime)
                notification.save()
                notification_detail = NotificationDetail(notification=notification, source_user=source_user, message=message, created_dateTime=notification.created_dateTime)
                notification_detail.save()

class NotificationDetail(models.Model):
    notification                  = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='detail_messages')
    source_user                   = models.ForeignKey(User, on_delete= models.CASCADE,related_name='source_of_notification_detail')
    message                       = models.TextField(default='')
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=False, null=True)

    class Meta:
        ordering = ['-created_dateTime']

    def __str__(self):
        return self.message
