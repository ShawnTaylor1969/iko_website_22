# Generated by Django 3.0.8 on 2020-08-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='url',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
    ]
