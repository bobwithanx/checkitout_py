from django.contrib import admin
from .models import Transaction, TransactionHistory, Catalog, Item, Category, Brand, Person, Group

class PersonAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'id_number', 'group')

class TransactionAdmin(admin.ModelAdmin):
        list_display = ('item', 'person', 'time_out')

class ItemAdmin(admin.ModelAdmin):
        list_display = ('catalog_item', 'inventory_tag', 'serial')

class CatalogAdmin(admin.ModelAdmin):
        list_display = ('display_name', 'category', 'brand', 'model')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionHistory)
admin.site.register(Item, ItemAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
