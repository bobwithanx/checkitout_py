from django.contrib import admin
from .models import Transaction, Item, Category, Brand, Student, Course

class StudentAdmin(admin.ModelAdmin):
        list_display = ('full_name', 'id_number', 'course')

class TransactionAdmin(admin.ModelAdmin):
        list_display = ('item', 'student', 'out_time', 'in_time')

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
