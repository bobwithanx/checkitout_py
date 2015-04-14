from django.contrib import admin
from .models import Transaction, TransactionHistory, Catalog, Item, Category, Brand, Person, Group

class PersonAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'id_number', 'group')

class TransactionAdmin(admin.ModelAdmin):
        list_display = ('item', 'person', 'time_out')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(TransactionHistory)
admin.site.register(Item)
admin.site.register(Catalog)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Person, PersonAdmin)
admin.site.register(Group)
