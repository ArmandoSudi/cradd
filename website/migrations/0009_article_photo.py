# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]