# Generated by Django 3.0.8 on 2020-08-31 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_eventschedules', '0003_auto_20200830_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventschedule',
            name='weekly_frequency',
            field=models.CharField(choices=[('EVERYNWEEKS', 'Every n-weeks'), ('WEEKOFMONTH', 'Week of Month')], default='EVERYNWEEKS', max_length=20),
        ),
    ]