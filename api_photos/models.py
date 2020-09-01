from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Photo(models.Model):
    album                         = models.ForeignKey('api_albums.Album', on_delete=models.CASCADE, null=True, blank=True)
    title                         = models.CharField(max_length=200)
    slug                          = models.SlugField(max_length=200, unique=True, null=True)
    summary                       = models.CharField(max_length=2000, blank=True, default='')
    uploaded_by                   = models.ForeignKey(User, on_delete= models.CASCADE,related_name='photo_uploads')
    picture                       = models.ImageField(upload_to='photos/', null=True, blank=True, height_field='picture_height', width_field='picture_width')
    picture_height                = models.IntegerField(default=0)
    picture_width                 = models.IntegerField(default=0)

    views                         = models.ManyToManyField(User, blank=True, related_name='photo_views')
    likes                         = models.ManyToManyField(User, blank=True, related_name='photo_likes')
    dislikes                      = models.ManyToManyField(User, blank=True, related_name='photo_dislikes')

    inherit_parent_permissions    = models.BooleanField(default=True)

    updated_dateTime              = models.DateTimeField("Last updated", auto_now=True, auto_now_add=False)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['title']

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = ""
        if self.album.space:
            value = self.album.space.slug + "-"
        value = value + self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Photo.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
