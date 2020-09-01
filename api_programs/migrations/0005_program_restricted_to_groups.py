# Generated by Django 3.0.8 on 2020-08-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_groups', '0001_initial'),
        ('api_programs', '0004_auto_20200825_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='restricted_to_groups',
            field=models.ManyToManyField(blank=True, related_name='group_programs', to='api_groups.Group'),
        ),
    ]
