# Generated by Django 3.0.8 on 2020-08-28 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_spaces', '0002_auto_20200825_1022'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('summary', models.CharField(max_length=2000)),
                ('picture', models.ImageField(blank=True, height_field='picture_height', null=True, upload_to='albums/', width_field='picture_width')),
                ('picture_height', models.IntegerField(default=0)),
                ('picture_width', models.IntegerField(default=0)),
                ('inherit_space_permissions', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_authors', to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(blank=True, related_name='album_follows', to=settings.AUTH_USER_MODEL)),
                ('space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_spaces.Space')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
