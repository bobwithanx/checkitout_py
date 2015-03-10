from django.db import models
from django.utils import timezone

class Transaction(models.Model):
	item = models.ForeignKey('Item')
	student = models.ForeignKey('Student')
	out_time = models.DateTimeField(default=timezone.now)
	in_time = models.DateTimeField(blank=True, null=True)

	def checkout(self):
		self.out_time = timezone.now()
	def checkin(self):
		self.in_time = timezone.now()

	def __str__(self):
	    return ' '.join([self.item.brand.name, self.item.model, str(self.out_time), ' -> ', str(self.in_time), '(', self.student.first_name, self.student.last_name, ')'])


class Item(models.Model):
	category = models.ForeignKey('Category')
	brand = models.ForeignKey('Brand')
	model = models.CharField(max_length=255)
	serial = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	assigned_to = models.ForeignKey('Student', blank=True, null=True)

	def assign(self, student):
		self.assigned_to = student
		self.save()

	def __str__(self):
	    if self.assigned_to <> None: 
		return ' '.join([self.brand.name, self.model, 'is checked out to', self.assigned_to.first_name, self.assigned_to.last_name])
	    else:
		return ' '.join([self.brand.name, self.model, 'is available'])

class Category(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Student(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	id_number = models.CharField(max_length=255)

	def __str__(self):
		return ' '.join([self.first_name, self.last_name])
