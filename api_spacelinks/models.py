from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class SpaceLink(models.Model):
    ITEMTYPE_CHOICES = [
        ('ANOTHER_SPACE', 'Link to another Application or Space'),
        ('CONTENT', 'Link to content'),
        ('PROGRAM', 'Link to a program'),
        ('URL', 'Link to an external Url'),
        ('GROUP_HEADER', 'Group header'),
        ('FOLDER', 'Folder'),
        ('SPACER', 'Spacer')
    ]
    space                         = models.ForeignKey('api_spaces.Space', on_delete=models.CASCADE, null=True)
    root_link                     = models.BooleanField(default=False)
    parent                        = models.ForeignKey('self', blank=True, null=True, default=None, on_delete=models.CASCADE, related_name="child_links")

    title                         = models.CharField(max_length=200)
    slug                          = models.SlugField(max_length=256, unique=True)
    sequence                      = models.IntegerField(default=0)

    type                          = models.CharField(max_length=20, choices=ITEMTYPE_CHOICES, default='MENU')
    another_space                 = models.ForeignKey('api_spaces.Space', blank=True, null=True, on_delete=models.CASCADE, related_name="space_links")
    content_type                  = models.ForeignKey('api_contenttypes.ContentType', blank=True, null=True, on_delete=models.CASCADE, related_name="contenttype_links")
    content_slug                  = models.SlugField(max_length=256, blank=True, null=True)
    program                       = models.ForeignKey('api_programs.Program', blank=True, null=True, on_delete=models.CASCADE, related_name="program_links")
    url                           = models.CharField(max_length=128, blank=True, null=True, default='')
    icon_URL                      = models.CharField(max_length=200, blank=True, null=True, default='')

    # public_access                 = models.BooleanField(default=False)
    # private_access                = models.BooleanField(default=True)
    # restricted_access             = models.BooleanField(default=False)
    # restricted_to_roles           = models.ManyToManyField(Role, blank=True, related_name='menuitem_roles_allowed')

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value = ""
        if self.space:
            value = self.space.slug + "-"
        value = value + self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not SpaceLink.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        # if self.slug == "":
        self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
