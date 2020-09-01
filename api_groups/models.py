from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
class Group(models.Model):
    #Create relationship with authorization Role
    title                         = models.CharField(max_length=200)
    slug                          = models.SlugField(max_length=200, unique=True, null=True)
    positions                     = models.ManyToManyField('api_positions.Position', blank=True, symmetrical=False)

    class Meta:
        ordering = ['title']

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Group.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
