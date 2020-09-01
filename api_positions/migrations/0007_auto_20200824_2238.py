# Generated by Django 3.0.8 on 2020-08-25 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_positions', '0006_auto_20200824_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='parent_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_positions.Position'),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]