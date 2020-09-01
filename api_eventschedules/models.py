from django.db import models
from datetime import timedelta, datetime
from django.utils.text import slugify
import itertools

#models
from django.contrib.auth.models import User

class EventSchedule(models.Model):
    FREQUENCY_CHOICES = [
        ('ONCE', 'Once'),
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly')
    ]
    WEEKLY_CHOICES = [
        ('EVERYNWEEKS', 'Every n-weeks'),
        ('WEEKOFMONTH', 'Week of Month'),
    ]
    WEEKOFMONTH_CHOICES = [
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth')
    ]
    END_CHOICES = [
        ('NEVER', 'Never'),
        ('OCCURRENCES', 'After n-occurrences'),
        ('ENDDATE', 'End date')
    ]

    calendar                      = models.ForeignKey('api_calendars.Calendar', on_delete=models.CASCADE, null=True)
    event_type                    = models.ForeignKey('api_eventtypes.EventType', on_delete=models.CASCADE, null=True)

    title                         = models.CharField(max_length=200, unique=True)
    slug                          = models.SlugField(max_length=200, unique=True)
    organizer                     = models.ForeignKey(User, on_delete= models.CASCADE,related_name='eventschedule_organizers')
    body                          = models.TextField(null=True, blank=True, default='')
    picture                       = models.ImageField(upload_to='eventschedules/', null=True, blank=True, height_field='picture_height', width_field='picture_width')
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
    frequency                     = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='ONCE')
    # DAILY
    repeat_every_n_days           = models.IntegerField("Repeat every n-days", default=1, null=False)
    # WEEKLY
    weekly_frequency              = models.CharField(max_length=20, choices=WEEKLY_CHOICES, default='EVERYNWEEKS')
    repeat_every_n_weeks          = models.IntegerField("Repeat every n-weeks", default=1, null=False)
    repeat_week_of_month          = models.CharField(max_length=1, choices=WEEKOFMONTH_CHOICES, default='1')
    repeat_on_Mon                 = models.BooleanField(default=False)
    repeat_on_Tue                 = models.BooleanField(default=False)
    repeat_on_Wed                 = models.BooleanField(default=False)
    repeat_on_Thu                 = models.BooleanField(default=False)
    repeat_on_Fri                 = models.BooleanField(default=False)
    repeat_on_Sat                 = models.BooleanField(default=False)
    repeat_on_Sun                 = models.BooleanField(default=False)
    # MONTHLY
    repeat_last_day_of_month      = models.BooleanField(default=False)
    repeat_day_of_the_month       = models.IntegerField("Day of the month", default=1, null=False)
    # YEARLY
    repeat_every_n_years          = models.IntegerField("Repeat every n-years", default=1, null=False)
    # END
    end_series                    = models.CharField(max_length=20, choices=END_CHOICES, default='NEVER')
    series_occurrences            = models.IntegerField(default=0, null=False)

    location                      = models.CharField(max_length=512, default='', blank=True, null=False)
    show_as_busy                  = models.BooleanField(default=True)

    follows                       = models.ManyToManyField(User, blank=True, related_name='eventschedule_follows')
    likes                         = models.ManyToManyField(User, blank=True, related_name='eventschedule_likes')
    dislikes                      = models.ManyToManyField(User, blank=True, related_name='eventschedule_dislikes')

    inherit_space_permissions     = models.BooleanField(default=True)

    class Meta:
        ordering = ['start_dateTime']

    def _generate_slug(self):
        max_length = self._meta.get_field('slug').max_length
        value =  self.title
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not EventSchedule.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        self.slug = slug_candidate

    def save(self, *args, **kwargs):
        if self.slug == "":
            self._generate_slug()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
