from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Calendar(models.Model):
    space                         = models.ForeignKey('api_spaces.Space', on_delete=models.CASCADE, null=True)
    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    organizer                     = models.ForeignKey(User, on_delete= models.CASCADE,related_name='calendar_organizers')
    summary                       = models.CharField(max_length=2000, blank=True, default='')
    picture                       = models.ImageField(upload_to='calendars/', null=True, blank=True, height_field='picture_height', width_field='picture_width')
    picture_height                = models.IntegerField(default=0, blank=True, null=True)
    picture_width                 = models.IntegerField(default=0, blank=True, null=True)

    follows                       = models.ManyToManyField(User, blank=True, related_name='calendar_follows')

    inherit_space_permissions     = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = ""
        if self.space:
            value = self.space.slug + "-"
        value = value + self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Calendar.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if self.slug == "":
            self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
