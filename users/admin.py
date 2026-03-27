from django.contrib import admin
from .models.new_user import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
