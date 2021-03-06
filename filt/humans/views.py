from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

from humans.models import Teacher, Group, Logger
from humans.forms import TeacherAddForm, GroupAddForm,\
                            EmailForm


def generate_group(request):
    group = Group.generate_group()
    return HttpResponse(f'{group.get_info()}')


def generate_teacher(request):
    queryset = Teacher.objects.all()
    fn = request.GET.get('add')

    if fn:
        queryset = queryset.filter(
            Q(first_name__istartswith=fn)
            | Q(last_name__istartswith=fn)
            | Q(email__istartswith=fn))

    return render(request,
                  'teachers_list.html',
                  context={'generate_teacher': queryset})


def generate_groups(request):
    queryset = Group.objects.all().select_related('curratt', 'headman')
    gr = request.GET.get('push')

    if gr:
        queryset = queryset.filter(
            Q(name__istartswith=gr)
            | Q(curratt__istartswith=gr)
            | Q(headman__istartswith=gr))

    return render(request,
                  'groups_list.html',
                  context={'generate_groups': queryset})


def add_teacher(request):

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
            return HttpResponseRedirect(reverse('filt-teacher'))
    else:
        form = EmailForm()
    return render(request,
                  'email_list.html',
                  context={'form': form})


def email_text(request):
    with open('emm.txt') as file:
        txt = file.read()
    return HttpResponse(txt)


def logger(request):
    logger = Logger.objects.all()
    return HttpResponse(f'{logger}{request.user}')


def handler404(request):
    return render(request, 'error_404.html', status=404)


def handler500(request):
    return render(request, 'error_500.html', status=500)
