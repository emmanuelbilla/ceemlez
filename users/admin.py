from django.contrib import admin
from .models.new_user import NewUser

# Register your models here.
@admin.register(NewUser)
class NewUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')