# Generated by Django 3.0.8 on 2020-08-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_positions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='parentPosition',
        ),
        migrations.AddField(
            model_name='position',
            name='parent_positions',
            field=models.ManyToManyField(blank=True, related_name='_position_parent_positions_+', to='api_positions.Position', verbose_name='Parent Positions'),
        ),
    ]
