# Generated by Django 3.0.8 on 2020-08-15 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_spaces', '0001_initial'),
        ('api_spacelinks', '0003_auto_20200815_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='spacelink',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_spaces.Space'),
        ),
    ]
