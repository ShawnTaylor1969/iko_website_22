# Generated by Django 3.0.8 on 2020-08-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_positions', '0002_auto_20200819_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
    ]
