from django.urls import path

from humans.views import (generate_teacher, generate_group,
                          generate_groups, add_teacher, add_group, edit_teacher)


urlpatterns = [
    path('filt/teach/', generate_teacher, name='filt-teacher'),
    path('filt/group/', generate_groups, name='filt-group'),
    path('gene/group/', generate_group, name='gen-group'),
    path('add/teacher/', add_teacher, name='add-teacher'),
    path('add/group/', add_group, name='add-group'),
    path('edit/teacher/', edit_teacher, name='edit-teacher'),
]
