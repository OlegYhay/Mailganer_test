from django.forms import ModelForm, SelectDateWidget, TextInput, EmailInput, MultipleChoiceField, \
    CheckboxSelectMultiple, Textarea, ModelMultipleChoiceField, SplitDateTimeWidget, DateTimeInput

from .models import Subscribers, Mailing


class ContactForm(ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'
        widgets = {
            "date_of_birth": SelectDateWidget(attrs={'class': 'form-control'}, years=range(1950, 2022)),
            "name": TextInput(attrs={'class': 'form-control'}),
            'email_address': EmailInput(attrs={'class': 'form-control'}),
        }


class MailingForm(ModelForm):
    subscribers = ModelMultipleChoiceField(widget=CheckboxSelectMultiple, queryset=Subscribers.objects.all())

    class Meta:
        model = Mailing
        fields = ['name', 'title', 'text_message', 'mailing_date','subscribers']
        widgets = {
            "name": TextInput(attrs={'class': 'form-control'}),
            "title": TextInput(attrs={'class': 'form-control'}),
            "text_message": Textarea(attrs={'class': 'form-control'}),
            "mailing_date": DateTimeInput(),
        }
