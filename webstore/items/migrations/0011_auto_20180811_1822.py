# Generated by Django 2.1 on 2018-08-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_auto_20180811_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.FileField(upload_to='images/'),
        ),
    ]
