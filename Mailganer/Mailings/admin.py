# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subscribers, Mailing, Mailing_message


# Register your models here.

@admin.register(Subscribers)
class SubscribersModel(admin.ModelAdmin):
    pass


@admin.register(Mailing)
class MailingsModel(admin.ModelAdmin):
    pass


@admin.register(Mailing_message)
class Mailing_messageModel(admin.ModelAdmin):
    pass
