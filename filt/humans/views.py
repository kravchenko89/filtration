from pdb import set_trace
from django.shortcuts import render

from django.db.models import Q

from humans.models import Teacher


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
