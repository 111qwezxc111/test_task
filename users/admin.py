from django.contrib import admin
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'city')
    list_filter = ('id', 'email', 'phone_number', 'city')
    search_fields = ('id', 'email', 'phone_number', 'city')
