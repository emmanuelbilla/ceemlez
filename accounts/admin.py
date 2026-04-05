from django.contrib import admin
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_joined', 'organisation')
    search_fields = ('email', 'first_name', 'last_name', 'organisation')