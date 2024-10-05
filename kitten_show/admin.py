from django.contrib import admin
from kitten_show.models import Kitten, Grade


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'age', 'description', 'breed')
    list_filter = ('id', 'name', 'color', 'age', 'description', 'breed', 'owner')
    search_fields = ('id', 'name', 'color', 'age', 'description', 'breed', 'owner')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'kitten', 'value')
    list_filter = ('id', 'user', 'kitten', 'value')
    search_fields = ('id', 'user', 'kitten', 'value')
