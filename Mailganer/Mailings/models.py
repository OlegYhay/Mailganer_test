# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models

from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
from django.views import View


@python_2_unicode_compatible
class Subscribers(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    email_address = models.EmailField(max_length=255, verbose_name='email адрес')
    date_of_birth = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name + '-' + self.email_address


@python_2_unicode_compatible
class Mailing(models.Model):
    STATUS_CHOICES = (
        ("DONE", "Done"),
        ("CREATED", "Created"),
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    title = models.CharField(max_length=255, verbose_name='Загловок сообщения')
    text_message = models.TextField(verbose_name='Текст сообщения')
    mailing_date = models.DateTimeField(verbose_name='Дата начала рассылки')
    subscribers = models.ManyToManyField(Subscribers, verbose_name='Подписчики',
                                         related_name='subsribers')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED')
    taskid = models.CharField(max_length=255, default='', null=True, blank=True)

    def __str__(self):
        return self.name + '-' + self.status + '.'


@python_2_unicode_compatible
class Mailing_message(models.Model):
    STATUS_MESSAGE = (
        ("OPEN", 'Open'),
        ("NOT OPEN", 'Not open'),
    )

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', related_name='messages')
    subscriber = models.ForeignKey(Subscribers, on_delete=models.CASCADE, verbose_name='Подписчик',
                                   related_name='subscribers')
    status = models.CharField(max_length=255, choices=STATUS_MESSAGE, default='NOT OPEN', verbose_name='Статус')

    def __str__(self):
        return self.status
