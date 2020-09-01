from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class ContentType(models.Model):
    title                         = models.CharField(max_length=128, blank=True, null=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    sequence                      = models.IntegerField(blank=True, null=True)
    namespace                     = models.CharField(max_length=128, blank=True, null=True, default='')
    active                        = models.BooleanField(default=True)
    space_page_URL                = models.CharField(max_length=200, blank=True, null=True, default='')
    directory_URL                 = models.CharField(max_length=200, blank=True, null=True, default='')
    icon_URL                      = models.CharField(max_length=200, blank=True, null=True, default='')

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not ContentType.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)
        self.slug = slug_candidate

    def _generate_sequence(self):
        contentTypes = ContentType.objects.all.order_by('-sequence')
        if contentTypes.count == 0:
            self.sequence = 1
        else:
            self.sequence = contentTypes.first().sequence + 1

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
