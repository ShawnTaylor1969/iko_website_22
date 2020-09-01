from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools
from django.dispatch import receiver
from django.db.models.signals import post_save

#models
from django.contrib.auth.models import User
from api_eventschedules.models import EventSchedule

class Event(models.Model):
    eventschedule                 = models.ForeignKey('api_eventschedules.EventSchedule', on_delete=models.CASCADE, null=True)
    calendar                      = models.ForeignKey('api_calendars.Calendar', on_delete=models.CASCADE, null=True)

    event_type                    = models.ForeignKey('api_eventtypes.EventType', on_delete=models.CASCADE, null=True)

    title                         = models.CharField(max_length=200, unique=True)
    organizer                     = models.ForeignKey(User, on_delete= models.CASCADE,related_name='event_organizers')
    body                          = models.TextField(null=True, blank=True, default='')
    picture                       = models.ImageField(upload_to='events/', null=True, blank=True, height_field='picture_height', width_field='picture_width')
    picture_height                = models.IntegerField(default=0, blank=True, null=True)
    picture_width                 = models.IntegerField(default=0, blank=True, null=True)

    public_body_same_as           = models.BooleanField(default=True)
    public_body                   = models.TextField(null=True, blank=True, default='')
    independent_body_same_as      = models.BooleanField(default=True)
    independent_body              = models.TextField(null=True, blank=True, default='')
    active_body_same_as           = models.BooleanField(default=True)
    active_body                   = models.TextField(null=True, blank=True, default='')
    alumni_body_same_as           = models.BooleanField(default=True)
    alumni_body                   = models.TextField(null=True, blank=True, default='')

    is_active                     = models.BooleanField(default=True)

    start_dateTime                = models.DateTimeField("Start time", auto_now=False, auto_now_add=False, null=True)
    end_dateTime                  = models.DateTimeField("End time", auto_now=False, auto_now_add=False, null=True)
    all_day_event                 = models.BooleanField(default=False)

    location                      = models.CharField(max_length=512, default='', blank=True, null=False)
    show_as_busy                  = models.BooleanField(default=True)

    follows                       = models.ManyToManyField(User, blank=True, related_name='event_follows')
    likes                         = models.ManyToManyField(User, blank=True, related_name='event_likes')
    dislikes                      = models.ManyToManyField(User, blank=True, related_name='event_dislikes')

    inherit_space_permissions     = models.BooleanField(default=True)

    class Meta:
        ordering = ['start_dateTime']

    def __str__(self):
        return self.title

    @receiver(post_save, sender=EventSchedule)
    def post_save_EventSchedule(sender, instance, created, **kwargs):
        if created:
            if instance.frequency == "ONCE":
                event = Event(eventschedule=instance, calendar=instance.calendar, event_type=instance.event_type, \
                            title=instance.title, organizer=instance.organizer, body=instance.body, picture=instance.picture, picture_width=instance.picture_width, picture_height= instance.picture_height, \
                            public_body_same_as=instance.public_body_same_as, independent_body_same_as=instance.independent_body_same_as, active_body_same_as=instance.active_body_same_as, alumni_body_same_as=instance.alumni_body_same_as, \
                            is_active=instance.is_active, start_dateTime=instance.start_dateTime, end_dateTime=instance.end_dateTime, all_day_event=instance.all_day_event, location=instance.location, show_as_busy=instance.show_as_busy
                        )
                event.save()
                pass
            if instance.frequency == "DAILY":
                pass
            if instance.frequency == "WEEKLY":
                pass
            if instance.frequency == "MONTHLY":
                pass
            if instance.frequency == "YEARLY":
                pass
