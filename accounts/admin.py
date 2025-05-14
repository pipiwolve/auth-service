from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_staff', 'is_superuser', 'is_active')