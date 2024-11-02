from django.contrib import admin

from .models import Employee, Position, User


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'patronymic',
                    'position', 'is_fired', 'fire_date')
    search_fields = ('is_fired',)


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Position)
