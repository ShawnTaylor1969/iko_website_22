from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Wall(models.Model):
    space                         = models.ForeignKey('api_spaces.Space', on_delete=models.CASCADE, null=True)
    picture                       = models.ImageField(upload_to='walls/', null=True, blank=True, height_field='picture_height', width_field='picture_width')
    picture_height                = models.IntegerField(default=0, blank=True, null=True)
    picture_width                 = models.IntegerField(default=0, blank=True, null=True)
    title                         = models.CharField(max_length=200, unique=True)
    message                       = models.TextField(default='', blank=True, null=True)

    content_app_id                = models.CharField(max_length=128, blank=True, default='', null=True)
    content_pk                    = models.IntegerField(default=0)

    likes                         = models.ManyToManyField(User, blank=True, related_name='wall_likes')
    dislikes                      = models.ManyToManyField(User, blank=True, related_name='wall_dislikes')

    created_by                    = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_dateTime']

    def __str__(self):
        return self.title
