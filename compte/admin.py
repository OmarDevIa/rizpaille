from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser', 'is_student', 'is_professor']
    search_fields = ['username', 'email', 'first_name', 'last_name']

admin.site.register(User, UserAdmin)
