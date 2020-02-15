from django.forms import (ModelForm, Form, EmailField,
                          CharField, ValidationError)
from django import forms

from django.conf import settings


from humans.tasks import task_email_send
from humans.models import Teacher, Group, Student


class BaseTeacherForm(ModelForm):

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_exists = Teacher.objects \
            .filter(phone__iexact=phone) \
            .exclude(id=self.instance.id)

        if phone_exists:
            raise ValidationError(f'{phone} is all ready used!!!')
        elif not phone.isdigit():
            raise ValidationError(f'{phone} is not Integer!!!')
        else:
            return phone

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects \
            .filter(email__iexact=email) \
            .exclude(id=self.instance.id)

        if email_exists:
            raise ValidationError(f'{email} is all ready used!!!')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].capitalize()
        if not first_name.isalpha():
            raise ValidationError(f'{first_name} is not String!!!')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].capitalize()
        if not last_name.isalpha():
            raise ValidationError(f'{last_name} is not String!!!')
        return last_name


class BaseStudentForm(ModelForm):

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_exists = Student.objects \
            .filter(phone__iexact=phone) \
            .exclude(id=self.instance.id)

        if phone_exists:
            raise ValidationError(f'{phone} is all ready used!!!')
        elif not phone.isdigit():
            raise ValidationError(f'{phone} is not Integer!!!')
        else:
            return phone

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        email_exists = Teacher.objects \
            .filter(email__iexact=email) \
            .exclude(id=self.instance.id)

        if email_exists:
            raise ValidationError(f'{email} is all ready used!!!')
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].capitalize()
        if not first_name.isalpha():
            raise ValidationError(f'{first_name} is not String!!!')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name'].capitalize()
        if not last_name.isalpha():
            raise ValidationError(f'{last_name} is not String!!!')
        return last_name


class TeacherAddForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(BaseTeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentAdminForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(BaseStudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class EmailForm(Form):
    email = EmailField()
    subject = CharField()
    text = forms.CharField(widget=forms.Textarea)


class LoggerAdminForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def save_email(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER]
        task_email_send.delay(subject, message, email_from, recipient_list)
        # send_mail(subject, message, email_from, recipient_list)

        with open('emm.txt', 'a') as tex:
            tex.write(f"Email_from: {email_from} | Subject: {subject} | Message: {message} <br>")


# class EmailAuthForm(Form):
#     email = EmailField()
#
#     def save_authot(self):
#         data = self.cleaned_data
#         email_from = data['email']
#         recipient_list = [settings.EMAIL_HOST_USER]
