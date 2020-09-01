from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Timeline(models.Model):
    EVENT_CHOICES = [
        ('CREATE_CONTENT', 'Create content'),
        ('SHARE_CONTENT', 'Share content'),
        ('LIKE_CONTENT', 'Like content'),
        ('DISLIKE_CONTENT', 'Dislike content'),
        ('FOLLOW_CONTENT', 'Follow content'),
        ('APPLICATION_EVENT', 'Application event')
    ]
    event                         = models.CharField(max_length=20, choices=EVENT_CHOICES, default='CREATECONTENT')
    event_user                    = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    space                         = models.ForeignKey('api_spaces.Space', on_delete=models.CASCADE, null=True)
    title                         = models.CharField(max_length=256, default='', blank=True, null=True)
    message                       = models.TextField(default='', blank=True, null=True)
    content_app_id                = models.CharField(max_length=128, blank=True, default='', null=True)
    content_slug                  = models.SlugField(max_length=200, blank=True, default='', null=True)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_dateTime']

    def __str__(self):
        return self.title
