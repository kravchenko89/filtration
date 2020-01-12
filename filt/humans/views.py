from pdb import set_trace

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from humans.models import Teacher, Group
from humans.forms import TeacherAddForm, GroupAddForm


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def generate_teacher(request):
    queryset = Teacher.objects.all()
    response = ''

    fn = request.GET.get('add')

    if fn:
        queryset = queryset.filter(
            Q(first_name__istartswith=fn)
            | Q(last_name__istartswith=fn)
            | Q(email__istartswith=fn))

    for teacher in queryset:
        set_trace()
        response += teacher.get_info() + '<br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})


def generate_groups(request):
    queryset = Group.objects.all()
    response = ''

    gr = request.GET.get('push')

    if gr:
        queryset = queryset.filter(
            Q(first_name__istartswith=gr)
            | Q(last_name__istartswith=gr)
            | Q(lesson__istartswith=gr)
            | Q(group__startswith=gr))

    for group in queryset:
        response += group.get_info() + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def add_teacher(request):
    set_trace()
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('filt-teach/')
    else:
        form = TeacherAddForm()
    return render(request,
                  'teachers_add.html',
                  context={'form': form})


def add_group(request):

    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('filt-group/')
    else:
        form = GroupAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})
