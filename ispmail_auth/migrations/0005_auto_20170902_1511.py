# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ispmail_auth', '0004_auto_20170902_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
