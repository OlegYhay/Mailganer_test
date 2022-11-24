# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import os
import urllib

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ContactForm, MailingForm
from .models import Subscribers, Mailing, Mailing_message

from .tasks import mailing_email
from Mailganer.celery import app


def home_page(request, *args, **kwargs):
    active_mailings = Mailing.objects.filter(status='CREATED')
    return render(request, 'templates/home_page.html', {'mailings': active_mailings})


class SubsribersListView(ListView):
    model = Subscribers
    template_name = 'templates/subscribers/subscribers_page.html'
    context_object_name = 'subscribers'


class SubsribersAddView(CreateView):
    model = Subscribers
    template_name = 'templates/subscribers/subsribers_add.html'
    form_class = ContactForm
    success_url = reverse_lazy('subsribers_page')


class SubsribersUpdateView(UpdateView):
    model = Subscribers
    template_name = 'templates/subscribers/subscribers_update.html'
    form_class = ContactForm
    success_url = reverse_lazy('subsribers_page')


class SubscribersDeleteView(DeleteView):
    model = Subscribers
    success_url = reverse_lazy('subsribers_page')
    template_name = 'templates/subscribers/subscribers_confirm_delete.html'


class MailingsListView(ListView):
    model = Mailing
    template_name = 'templates/Mailing/mailing_list.html'
    context_object_name = 'mailings'


class MailingsDeleteView(DeleteView):
    model = Mailing
    template_name = 'templates/Mailing/mailings_confirm_delete.html'
    success_url = reverse_lazy('mailings_page')

    def form_valid(self, form):
        self.object = form.save()
        app.control.revoke(self.object.taskid, terminate=True)
        return HttpResponseRedirect(self.get_success_url())


class MailingsUpdateView(UpdateView):
    model = Mailing
    template_name = 'templates/Mailing/mailings_update.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailings_page')

    def form_valid(self, form):
        self.object = form.save()
        # delete task then create new
        if self.object.status != 'DONE':
            app.control.revoke(self.object.taskid, terminate=True)
            current_time = datetime.datetime.now()
            m = mailing_email.apply_async(
                (self.object.title, self.object.text_message, [x.email_address for x in self.object.subscribers.all()],
                 self.object.id),
                countdown=(self.object.mailing_date - current_time).total_seconds())
            self.object.taskid = m.id
            self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class MailingsCreateView(CreateView):
    model = Mailing
    template_name = 'templates/Mailing/mailings_add.html'
    form_class = MailingForm
    success_url = reverse_lazy('mailings_page')

    def get_initial(self):
        return {'mailing_date': datetime.datetime.now()}

    def form_valid(self, form):
        self.object = form.save()
        current_time = datetime.datetime.now()
        # если дата рассылки меньше текущей, рассылка начинается после создания
        # если рассылка в будушем, celery ждет оставшиеся время
        m = mailing_email.apply_async(
            (self.object.title, self.object.text_message, [x.email_address for x in self.object.subscribers.all()],
             self.object.id),
            countdown=(self.object.mailing_date - current_time).total_seconds())
        self.object.taskid = m.id
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class Message_mailings(ListView):
    model = Mailing_message
    template_name = 'templates/messages/messages_mailings.html'
    context_object_name = 'messages'

    def get_queryset(self):
        messages = Mailing_message.objects.filter(mailing=self.kwargs['pk'])
        return messages



def email_seen(request, key,key2):
    META = {
        header: value
        for header, value in request.META.items()
        if header.startswith(("HTTP_", "REMOTE_"))
    }

    get_message = Mailing_message.objects.get(mailing=key, subscriber=key)
    get_message.status = "OPEN"
    get_message.save()

    print("Successfully Tracketd")
    with open(os.path.dirname(os.path.abspath(__file__)) + "/static/img/pixel.png", "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")
