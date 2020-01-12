from django.forms import ModelForm

from humans.models import Teacher, Group


class TeacherAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
