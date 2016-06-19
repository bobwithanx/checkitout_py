from django.contrib import admin
from .models import Transaction, TransactionHistory, Item, Category, Brand, Person

class PersonAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'id_number', 'graduation_year', 'active')

class TransactionAdmin(admin.ModelAdmin):
        list_display = ('item', 'person', 'time_out')

class ItemAdmin(admin.ModelAdmin):
        list_display = ('display_name', 'inventory_tag', 'category', 'serial')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionHistory)
admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Person, PersonAdmin)
