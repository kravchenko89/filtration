from django.forms import (ModelForm, Form, EmailField,
                          CharField)
from django import forms
from django.core.mail import send_mail
from django.conf import settings

from humans.models import Teacher, Group


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class EmailForm(Form):
    email = EmailField()
    subject = CharField()
    text = forms.CharField(widget=forms.Textarea)

    def save_email(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, email_from, recipient_list)

        my_file = open('emm.txt', 'a')
        text = subject
        my_file.write(f"Email_from: {email_from} | Subject: {text} | Message: {message}\n <br>")

        my_file.close()
