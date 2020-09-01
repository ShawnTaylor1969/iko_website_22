from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools
from datetime import date
from dateutil.relativedelta import relativedelta
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

#models
from django.contrib.auth.models import User

class Member(models.Model):
    MEMBER_TYPE = [
        ('ACTIVE', 'I am a Soronian active'),
        ('ALUMNI', 'I am a Soronian alumni'),
        ('INDEPENDENT', 'I might become a Soronian Sister (Independent)'),
    ]

    STATUS_CHOICES = [
        ('REGISTERED', 'Registered'),
        ('PROFILED', 'Profiled'),
        ('ACTIVATED', 'Activated'),
        ('INACTIVATED', 'Inactivated')
    ]

    birth_date_default = date.today() - relativedelta(years=17)

    #Create relationship with admin User
    user                                = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='member_profile')

    # profile questions
    type                                = models.CharField(max_length=20, choices=MEMBER_TYPE, default='SISTER')

    #add additional attributes
    about_me                            = models.TextField(default='', blank=True)
    picture                             = models.ImageField(upload_to='profile_pics',blank=True, width_field='picture_width', height_field='picture_height')
    picture_width                       = models.IntegerField(default=0)
    picture_height                      = models.IntegerField(default=0)
    pledge_class                        = models.IntegerField(default=0)
    graduation_year                     = models.IntegerField(default=0)
    birth_date                          = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True, default=birth_date_default)

    status                              = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REGISTERED')
    is_new_blood                        = models.BooleanField(default=False)
    house_positions                     = models.ManyToManyField('api_positions.Position', blank=True, related_name='user_positions', verbose_name='Positions')

    profiled                            = models.BooleanField(default=False)
    profiled_dateTime                   = models.DateTimeField("Profiled Date/Time", auto_now=False, auto_now_add=False, null=True, blank=True)

    validated                           = models.BooleanField(default=False)
    validated_by                        = models.ForeignKey(User, on_delete= models.CASCADE,related_name='validated_users', null=True, blank=True)
    validated_dateTime                  = models.DateTimeField("Validated Date/Time", auto_now=False, auto_now_add=False, null=True, blank=True)

    activated                           = models.BooleanField(default=False)
    activated_by                        = models.ForeignKey(User, on_delete= models.CASCADE,related_name='activated_users', null=True, blank=True)
    activated_dateTime                  = models.DateTimeField("Actived Date/Time", auto_now=True, auto_now_add=False)

    updated_dateTime                    = models.DateTimeField("Last Updated Date/Time", auto_now=True, auto_now_add=False)
    created_dateTime                    = models.DateTimeField("Created Date/Time", auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Member.objects.create(user=instance)
