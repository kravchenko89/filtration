from django.contrib import admin

from humans.models import Teacher, Group, Student


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name', 'last_name')
    list_display = ('id', 'full_name', 'lesson')
    list_per_page = 15
    search_fields = ('first_name', 'last_name', 'lesson')

    def get_readonly_fields(self, request, obj=None):

        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('credit_card', 'email')

        return readonly_fields

    def has_delete_permission(self, request, obj=None):

        if request.user.groups.filter(name='manager').exists():
            return False
        return True


class StudentInline(admin.StackedInline):
    model = Student

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return False
        return True


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'curratt', 'headman')
    list_select_related = ('curratt', 'headman')
    list_per_page = 15
    search_fields = ('first_name', 'last_name', 'group')
    inlines = (StudentInline, )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('curratt', 'headman')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return False
        return True


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name', 'last_name')
    list_display = ('id', 'full_name', 'address', 'phone')
    list_per_page = 15
    search_fields = ('first_name', 'last_name')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)

        if request.user.groups.filter(name='manager').exists():
            return readonly_fields + ('group', 'phone', 'address')
        return readonly_fields

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return False
        return True
