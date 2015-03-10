from django.contrib import admin
from .models import Transaction, Item, Category, Brand, Student

admin.site.register(Transaction)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Student)
