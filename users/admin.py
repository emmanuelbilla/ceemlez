from django.contrib import admin
from users.models.user import User
from users.models.userassignment import UserAssignment

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role')
    search_fields = ('name', 'email', 'role')

@admin.register(UserAssignment)
class UserAssignmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task')
    search_fields = ('user__username', 'task__title')