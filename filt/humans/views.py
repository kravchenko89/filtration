from django.shortcuts import render
from django.http import HttpResponse
from humans.models import Teacher


def generate_teacher(request):
    # queryset = Teacher.objects.all()
    # response = ''
    # for teacher in queryset:
    #     response += teacher.get_info() + '<br>'
    # return HttpResponse(response)

    queryset = Teacher.objects.all()
    response = ''

    fn = request.GET.get('first_name')
    if fn:
        queryset = queryset.filter(first_name__istartswith=fn)

    for teacher in queryset:
        response += teacher.get_info() + '<br>'
    return render(request,
                  'teachers_list.html',
                  context={'teachers_list': response})
