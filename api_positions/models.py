from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Position(models.Model):
    #Create relationship with authorization Role
    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True, null=True)
    is_top_five                   = models.BooleanField(default=False)
    parent_position               = models.ForeignKey('self', on_delete= models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Position.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        self._generate_slug()

        if self.is_top_five and self.parent_position != None:
            self.parent_position = None

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
