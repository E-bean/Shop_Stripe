from django.contrib import admin

from store.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_editable = ('price',)
    empty_value_display = '-empty-'
    search_fields = ('name',)
