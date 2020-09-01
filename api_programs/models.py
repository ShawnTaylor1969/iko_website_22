from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class Program(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive')
    ]
    TYPE_CHOICES = [
        ('CRUD', 'CRUD'),
        ('CRUD_LIST', 'CRUD List'),
        ('GENERAL', 'General')
    ]
    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    summary                       = models.CharField(max_length=2000, null=False, blank=False)
    body                          = models.TextField()
    image                         = models.ImageField(upload_to='space_images', null=True, blank=True)

    type                          = models.CharField(max_length=20, choices=TYPE_CHOICES, default='GENERAL')

    url                           = models.CharField(max_length=128, blank=True, null=True, default='')
    show_application_menu         = models.BooleanField(default=False)
    show_space_menu               = models.BooleanField(default=False)

    status                        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    public_access                 = models.BooleanField(default=False)
    private_access                = models.BooleanField(default=True)
    restricted_access             = models.BooleanField(default=False)
    restricted_to_positions       = models.ManyToManyField('api_positions.Position', blank=True, related_name='position_programs')
    restricted_to_groups          = models.ManyToManyField('api_groups.Group', blank=True, related_name='group_programs')

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Program.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
        else:
            self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
