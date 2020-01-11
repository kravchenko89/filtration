from pdb import set_trace

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from humans.models import Teacher, Group


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
