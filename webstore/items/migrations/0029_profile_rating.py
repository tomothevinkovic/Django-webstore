# Generated by Django 2.1 on 2018-08-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0028_remove_profile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.CharField(default=None, max_length=3),
        ),
    ]
