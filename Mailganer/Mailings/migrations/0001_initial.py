# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-11-22 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0424\u0418\u041e')),
                ('email_address', models.EmailField(max_length=255, verbose_name='email \u0430\u0434\u0440\u0435\u0441')),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
            ],
        ),
    ]
