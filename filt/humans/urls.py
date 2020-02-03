from django.conf import settings
from django.urls import include, path

from humans.views import (generate_teacher, generate_group,
                          generate_groups, add_teacher,
                          add_group, edit_teacher, edit_group,
                          email_list, email_text, create_author)

urlpatterns = [
    path('filt/teach/', generate_teacher, name='filt-teacher'),
    path('filt/group/', generate_groups, name='filt-group'),
    path('gene/group/', generate_group, name='gen-group'),
    path('add/teacher/', add_teacher, name='add-teacher'),
    path('add/group/', add_group, name='add-group'),
    path('edit/teacher/<int:num>/', edit_teacher, name='edit-teacher'),
    path('edit/group/<int:num>/', edit_group, name='edit-group'),
    path('email/list/', email_list, name='email-list'),
    path('email/', email_text, name='email'),
    path('create/', create_author, name='create')
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                      path(r'^silk/', include('silk.urls', namespace='silk'))
                  ] + urlpatterns
