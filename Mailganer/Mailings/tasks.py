from celery import shared_task
from celery.contrib.abortable import AbortableTask
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from Mailganer.celery import app
from .models import Mailing, Mailing_message, Subscribers


@app.task(bind=True, base=AbortableTask)
def mailing_email(self, name='default', text_message='', recipients=[], id=''):
    for recipient in recipients:
        recipient_id = Subscribers.objects.get(email_address=recipient).id
        html_message = render_to_string('templates/Mailing/message_email.html',
                                        {'mail_id': id, 'user_id': recipient_id,'text_message':text_message})
        print(html_message)
        send_mail(
            name,
            text_message,
            'jadk.fre12@mail.ru',
            [recipient],
            fail_silently=False,
            html_message=html_message,
        )

    task = Mailing.objects.get(id=id)
    for subs in task.subscribers.all():
        message = Mailing_message(
            mailing=task,
            subscriber=subs,
            status="NOT OPEN",
        )
        message.save()

    task.status = 'DONE'
    task.save()
