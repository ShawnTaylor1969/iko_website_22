from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Article(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE_NOTPUBLISHED', 'Active (Not published)'),
        ('ACTIVE_PUBLISHED', 'Active (Published)'),
        ('INACTIVE_EXPIRED', 'Inactive (Expired)'),
        ('INACTIVE_ARCHIVED', 'Inactive (Archived)'),
        ('INACTIVE_REMOVED', 'Inactive (Removed)')
    ]
    IMAGESIZE_CHOICES = [
        ('NORMAL', 'Normal'),
        ('BIG', 'Big'),
        ('TALL', 'Tall'),
        ('WIDE', 'Wide')
    ]
    space                         = models.ForeignKey('api_spaces.Space', on_delete=models.CASCADE, null=True)
    #publication                   = models.ForeignKey(Publication, on_delete=models.CASCADE, null=True, blank=True)
    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    author                        = models.ForeignKey(User, related_name='articles', on_delete= models.CASCADE)
    summary                       = models.CharField(max_length=2000)
    body                          = models.TextField()
    image                         = models.ImageField("Image",upload_to='articles_images', null=True, blank=True)
    image_size                    = models.CharField(max_length=20, choices=IMAGESIZE_CHOICES, default='NORMAL')

    related_content               = models.ManyToManyField('self', blank=True, related_name='related_articles')
    status                        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')

    featured                      = models.BooleanField(default=False)
    featured_start_dateTime       = models.DateField("Featured Start", auto_now=False, auto_now_add=False, null=True, blank=True)
    featured_end_dateTime         = models.DateField("Featured End", auto_now=False, auto_now_add=False, null=True, blank=True)

    required_reading              = models.BooleanField(default=False)
    publication_dateTime          = models.DateField("Publication", auto_now=False, auto_now_add=False, null=True, blank=True, default=datetime.now)
    expiration_dateTime           = models.DateField("Expiration", auto_now=False, auto_now_add=False, null=True, blank=True, default=datetime.now)

    reads                         = models.ManyToManyField(User, blank=True, related_name='article_reads')
    likes                         = models.ManyToManyField(User, blank=True, related_name='article_likes')
    dislikes                      = models.ManyToManyField(User, blank=True, related_name='article_dislikes')
    follows                       = models.ManyToManyField(User, blank=True, related_name='article_follows')
    read_dateTime                 = models.DateTimeField("Last read", auto_now=False, auto_now_add=False, null=True, blank=True)
    updated_dateTime              = models.DateTimeField("Last updated", auto_now=True, auto_now_add=False)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=True)

    inherit_parent_permissions    = models.BooleanField(default=True)


    class Meta:
        ordering = ['-created_dateTime']

    def __str__(self):
        return self.title
