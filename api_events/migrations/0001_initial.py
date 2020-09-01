# Generated by Django 3.0.8 on 2020-09-01 00:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_eventtypes', '0001_initial'),
        ('api_eventschedules', '0006_auto_20200831_2031'),
        ('api_calendars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('body', models.TextField(blank=True, default='', null=True)),
                ('picture', models.ImageField(blank=True, height_field='picture_height', null=True, upload_to='events/', width_field='picture_width')),
                ('picture_height', models.IntegerField(blank=True, default=0, null=True)),
                ('picture_width', models.IntegerField(blank=True, default=0, null=True)),
                ('public_body_same_as', models.BooleanField(default=True)),
                ('public_body', models.TextField(blank=True, default='', null=True)),
                ('independent_body_same_as', models.BooleanField(default=True)),
                ('independent_body', models.TextField(blank=True, default='', null=True)),
                ('active_body_same_as', models.BooleanField(default=True)),
                ('active_body', models.TextField(blank=True, default='', null=True)),
                ('alumni_body_same_as', models.BooleanField(default=True)),
                ('alumni_body', models.TextField(blank=True, default='', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_dateTime', models.DateTimeField(null=True, verbose_name='Start time')),
                ('end_dateTime', models.DateTimeField(null=True, verbose_name='End time')),
                ('all_day_event', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, default='', max_length=512)),
                ('show_as_busy', models.BooleanField(default=True)),
                ('inherit_space_permissions', models.BooleanField(default=True)),
                ('calendar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_calendars.Calendar')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='event_dislikes', to=settings.AUTH_USER_MODEL)),
                ('event_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_eventtypes.EventType')),
                ('eventschedule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_eventschedules.EventSchedule')),
                ('follows', models.ManyToManyField(blank=True, related_name='event_follows', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='event_likes', to=settings.AUTH_USER_MODEL)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_organizers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['start_dateTime'],
            },
        ),
    ]
