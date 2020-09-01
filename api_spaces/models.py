from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User, Group

class Space(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive')
    ]
    SPACE_TYPE_CHOICES = [
        ('GENERAL', 'General use'),
        ('BLOG', 'Blog'),
        ('INTERNET', 'Internet')
    ]
    ADMIN_METHOD_CHOICES = [
        ('POSITION', 'A specific position'),
        ('USER', 'A specific user'),
        ('WEBADMIN', 'Website Administrator')
    ]
    SPACE_LAYOUTS = [
        ('STANDARD', 'Standard'),
        ('PREDEFINED', 'Pre-defined'),
        ('CUSTOM_URL', 'Custom URL')
    ]
    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    summary                       = models.CharField(max_length=2000, null=False, blank=False)
    body                          = models.TextField()
    image                         = models.ImageField(upload_to='space_images', null=True, blank=True)

    type                          = models.CharField(max_length=20, choices=SPACE_TYPE_CHOICES, default='GENERAL')

    layout                        = models.CharField(max_length=20, choices=SPACE_LAYOUTS, default='STANDARD')
    url                           = models.CharField(max_length=128, blank=True, null=True, default='')
    show_application_menu         = models.BooleanField(default=True)
    show_space_menu               = models.BooleanField(default=False)

    content_types                 = models.ManyToManyField('api_contenttypes.ContentType', blank=True, related_name='content_type_spaces_new')
    status                        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')

    admin_method                  = models.CharField(max_length=20, choices=ADMIN_METHOD_CHOICES, default='POSITION')
    admin_position                = models.ForeignKey('api_positions.Position', on_delete= models.CASCADE,related_name='admin_position_spaces', null=True, blank=True)
    admin_user                    = models.ForeignKey(User, on_delete= models.CASCADE,related_name='admin_user_spaces', null=True, blank=True)

    public_access                 = models.BooleanField(default=False)
    private_access                = models.BooleanField(default=True)
    restricted_access             = models.BooleanField(default=False)
    restricted_to_positions       = models.ManyToManyField('api_positions.Position', blank=True, related_name='position_spaces')
    restricted_to_groups          = models.ManyToManyField('api_groups.Group', blank=True, related_name='group_spaces')

    user_space                    = models.BooleanField(default=False)
    system_space                  = models.BooleanField(default=False)
    created_dateTime              = models.DateTimeField("Created", auto_now=False, auto_now_add=True)

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        if self.user_space:
            value = "User space " + self.admin_user.first_name + " "  + self.admin_user.last_name
        else:
            value = self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Space.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_authorized(self, user):
        authorized = False
        reason = "Denied"
        if self.public_access:
            authorized = True
            reason = "Public access"
        else:
            if not user.is_anonymous and user.is_active:
                if self.private_access:
                    authorized = True
                    reason = "Private access"
                else:
                    for position in user.membershipProfile.positions.all():
                        if self.restricted_to_positions.all().filter(id=position.id).count() > 0:
                            authorized = True
                            reason = "Restricted access: Allowed to " + position.title
                            break
        return authorized

    def get_absolute_url(self):
        return reverse(self.content_type.namespace + ":content_crud",kwargs={"slug": self.slug, "crud": "read"})

    def get_update_url(self):
        return reverse('osc_spaces:space_crud', kwargs={"slug": self.slug, 'crud': 'update'})

    def get_homepage_url(self):
        if self.layout == "CUSTOM_URL":
            return self.url
        else:
            return reverse('osc_spaces:space_homepage', kwargs={"slug": self.slug})
