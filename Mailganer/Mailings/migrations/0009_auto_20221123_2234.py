# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-23 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mailings', '0008_auto_20221123_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing_message',
            name='status',
            field=models.CharField(choices=[('OPEN', 'Open'), ('NOT OPEN', 'Not open')], default='NOT OPEN', max_length=255, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441'),
        ),
    ]