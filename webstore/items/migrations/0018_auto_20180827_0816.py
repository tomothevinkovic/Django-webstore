# Generated by Django 2.1 on 2018-08-27 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_user_logged_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
