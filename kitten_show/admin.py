from django.contrib import admin
from kitten_show.models import Kitten


@admin.register(Kitten)
class KittenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'age', 'description', 'breed')
    list_filter = ('id', 'name', 'color', 'age', 'description', 'breed', 'owner')
    search_fields = ('id', 'name', 'color', 'age', 'description', 'breed', 'owner')
