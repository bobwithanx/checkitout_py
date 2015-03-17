from django.db import models
from django.utils import timezone

class StudentsWithInventory(models.Manager):
  def get_queryset(self):
    return super(StudentsWithInventory, self).get_queryset().filter(in_time__isnull=True).order_by('assigned_to').distinct()

class Transaction(models.Model):
	item = models.ForeignKey('Item')
	student = models.ForeignKey('Student')
	out_time = models.DateTimeField(default=timezone.now)
	in_time = models.DateTimeField(blank=True, null=True)

	def checkout(self):
		self.out_time = timezone.now()
	def checkin(self):
		self.in_time = timezone.now()

	objects = models.Manager()
	with_inventory = StudentsWithInventory()

	def __str__(self):
	    text = ' '.join([self.item.brand.name, self.item.model, str(self.out_time), ' -> ', str(self.in_time), '(', self.student.first_name, self.student.last_name, ')'])
	    encoded = text.encode("utf-8")
	    return encoded

class ItemsAssigned(models.Manager):
  def get_queryset(self):
    return super(ItemsAssigned, self).get_queryset().filter(assigned_to__isnull=False)

class ItemsAvailable(models.Manager):
  def get_queryset(self):
    return super(ItemsAvailable, self).get_queryset().filter(assigned_to__isnull=True)

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

	objects = models.Manager()
	available_items = ItemsAvailable()
	assigned_items = ItemsAssigned()

	def __str__(self):
	    text = ' '.join([self.brand.name, self.model])
	    encoded = text.encode("utf-8")
	    return encoded

class Category(models.Model):
	name = models.CharField(max_length=255)
	def _get_assigned_item_count(self):
		return Item.objects.filter(category=self).filter(assigned_to__isnull=False).count()
	def _get_available_item_count(self):
		return Item.objects.filter(category=self).filter(assigned_to__isnull=True).count()
	def _get_item_count(self):
		return Item.objects.filter(category=self).count()
	item_count = property(_get_item_count)
	available_item_count = property(_get_available_item_count)
	assigned_item_count = property(_get_assigned_item_count)
	icon = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.name

class Brand(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Course(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class StudentInventory(models.Manager):
  def get_queryset(self):
    return super(StudentInventory, self).get_queryset().filter(assigned_to=self)

class Student(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	id_number = models.CharField(max_length=255)
	course = models.ForeignKey('Course', blank=True, null=True)

	def _get_inventory_count(self):
		"Returns a count of all items assigned to the person."
		return Transaction.objects.filter(in_time__isnull=True).filter(student=self).count()

	def _get_full_name(self):
		"Returns the person's full name."
		return '%s %s' % (self.first_name, self.last_name)
	full_name = property(_get_full_name)
	objects = models.Manager()

	def __str__(self):
		return self.full_name
