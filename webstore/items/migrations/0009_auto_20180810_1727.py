# Generated by Django 2.1 on 2018-08-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20180810_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.FileField(upload_to='C:/Users/Tomislav/Desktop/python/django/webstore/media/'),
        ),
    ]
