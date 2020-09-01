# Generated by Django 3.0.8 on 2020-08-26 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_members', '0011_auto_20200826_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='member_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
