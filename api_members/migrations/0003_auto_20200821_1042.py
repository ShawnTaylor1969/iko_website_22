# Generated by Django 3.0.8 on 2020-08-21 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_members', '0002_member_house_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.date(2003, 8, 21), null=True),
        ),
    ]
