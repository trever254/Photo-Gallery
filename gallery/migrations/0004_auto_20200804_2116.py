# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-08-04 18:16
from __future__ import unicode_literals

from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_link',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='pic',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]

class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_image_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_link',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='pic',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]