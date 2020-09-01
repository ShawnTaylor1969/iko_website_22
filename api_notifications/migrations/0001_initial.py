# Generated by Django 3.0.8 on 2020-08-21 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('message', models.TextField(default='')),
                ('content_app_id', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('content_slug', models.SlugField(max_length=200, unique=True)),
                ('cleared', models.BooleanField(default=False)),
                ('created_dateTime', models.DateTimeField(null=True, verbose_name='Created')),
                ('cleared_dateTime', models.DateTimeField(null=True, verbose_name='Closed')),
                ('notify_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_of_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NotificationDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='')),
                ('created_dateTime', models.DateTimeField(null=True, verbose_name='Created')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail_messages', to='api_notifications.Notification')),
                ('source_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_of_notification_detail', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_dateTime'],
            },
        ),
    ]