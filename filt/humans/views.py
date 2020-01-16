from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from humans.models import Teacher, Group
from humans.forms import TeacherAddForm, GroupAddForm, EmailForm


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

        response += f'<a  href="../../edit/teacher/{teacher.id}">' + teacher.get_info() + '</a><br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response, })


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
        response += f'<a  href="../../edit/group/{group.id}">' + group.get_info() + '<br>'
    return render(request,
                  'groups_list.html',
                  context={'groups_list': response})


def add_teacher(request):
    # set_trace()
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('filt-teacher'))
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
            return HttpResponseRedirect(reverse('filt-group'))
    else:
        form = GroupAddForm()
    return render(request,
                  'groups_add.html',
                  context={'form': form})


def edit_teacher(request, num):
    try:
        teacher = Teacher.objects.get(id=num)
    except Teacher.DoseNotExist:
        HttpResponseNotFound(f'Teacher with id{num} not found')
    # set_trace()
    if request.method == 'POST':
        form = TeacherAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('filt-teacher'))
    else:
        form = TeacherAddForm(instance=teacher)
    return render(request,
                  'edit_teacher.html',
                  context={'form': form, 'num': num})


def edit_group(request, num):
    try:
        group = Group.objects.get(id=num)
    except Group.DoseNotExist:
        HttpResponseNotFound(f'Teacher with id{num} not found')

    if request.method == 'POST':
        form = GroupAddForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('filt-group'))
    else:
        form = GroupAddForm(instance=group)
    return render(request,
                  'edit_group.html',
                  context={'form': form, 'num': num})


def email_list(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save_email()
            return HttpResponseRedirect(reverse('email-list'))
    else:
        form = EmailForm()
    return render(request,
                  'email_list.html',
                  context={'form': form})


def email_text(request):
    file = open('emm.txt')
    fun = file.read()
    return HttpResponse(fun)
