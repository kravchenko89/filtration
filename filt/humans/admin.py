from django.contrib import admin

from humans.models import Teacher, Group, Student, Logger
from humans.forms import StudentAdminForm, TeacherAdminForm, LoggerAdminForm


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # readonly_fields = ('first_name', 'last_name')
    list_display = ('id', 'full_name', 'lesson', 'phone')
    list_per_page = 15
    search_fields = ('first_name', 'last_name', 'lesson')
    form = TeacherAdminForm

    def get_readonly_fields(self, request, obj=None):

        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('credit_card', 'email')

        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name='manager').exists()

        # if request.user.groups.filter(name='manager').exists():
        #     return False
        # return True


class StudentInline(admin.TabularInline):
    model = Student
    show_change_link = True
    readonly_fields = ('first_name', 'last_name', 'email', 'phone', 'address')

    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name='manager').exists()
        # if request.user.groups.filter(name='manager').exists():
        #     return False
        # return True


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'curratt', 'headman')
    list_select_related = ('curratt', 'headman')
    list_per_page = 15
    search_fields = ('first_name', 'last_name', 'group')
    inlines = (StudentInline, )
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('curratt', 'headman')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):

        return not request.user.groups.filter(name='manager').exists()

        # if request.user.groups.filter(name='manager').exists():
        #     return False


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('first_name', 'last_name')
    list_display = ('id', 'full_name', 'address', 'phone')
    list_per_page = 15
    search_fields = ('first_name', 'last_name')
    form = StudentAdminForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('group', 'phone', 'address')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):

        return not request.user.groups.filter(name='manager').exists()

        # if request.user.groups.filter(name='manager').exists():
        #     return False
        # return True


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'time_delta', 'user_id', 'created')
    form = LoggerAdminForm
