# Generated by Django 2.1.1 on 2018-09-22 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0042_auto_20180922_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rated_profile',
        ),
        migrations.AddField(
            model_name='rating',
            name='rated_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='rated_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='reviewer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]