# Generated by Django 3.0.8 on 2020-07-30 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('api_contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('summary', models.CharField(max_length=2000)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='space_images')),
                ('type', models.CharField(choices=[('GENERAL', 'General use'), ('BLOG', 'Blog'), ('INTERNET', 'Internet')], default='GENERAL', max_length=20)),
                ('layout', models.CharField(choices=[('STANDARD', 'Standard'), ('PREDEFINED', 'Pre-defined'), ('CUSTOM_URL', 'Custom URL')], default='STANDARD', max_length=20)),
                ('url', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('show_application_menu', models.BooleanField(default=True)),
                ('show_space_menu', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=20)),
                ('admin_method', models.CharField(choices=[('ROLE', 'A specific role'), ('USER', 'A specific user'), ('WEBADMIN', 'Website Administrator')], default='ROLE', max_length=20)),
                ('public_access', models.BooleanField(default=False)),
                ('private_access', models.BooleanField(default=True)),
                ('restricted_access', models.BooleanField(default=False)),
                ('user_space', models.BooleanField(default=False)),
                ('system_space', models.BooleanField(default=False)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('admin_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_role_spaces', to='auth.Group')),
                ('admin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_user_spaces', to=settings.AUTH_USER_MODEL)),
                ('content_types', models.ManyToManyField(blank=True, related_name='content_type_spaces_new', to='api_contenttypes.ContentType')),
                ('restricted_to_roles', models.ManyToManyField(blank=True, related_name='role_spaces', to='auth.Group')),
            ],
        ),
    ]
