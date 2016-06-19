from django.db import models
from django.db.models import F
from django.utils import timezone

class TransactionHistory(models.Model):
    person = models.ForeignKey('Person')
    item = models.ForeignKey('Item')
    time_out = models.DateTimeField()
    time_in = models.DateTimeField()

    def get_history(self, person):
        return objects.filter(person=person)

    def __str__(self):
        text = ' *** '.join([self.item.display_name, str(self.time_out), str(self.time_in), self.person.full_name])
        encoded = text.encode("utf-8")
        return encoded

    class Meta:
				verbose_name_plural = "transaction histories"

class Transaction(models.Model):
    status_assigned = 'Assigned'
    
    person = models.ForeignKey('Person')
    item = models.ForeignKey('Item')
    time_out = models.DateTimeField(blank=True, null=True)
	
    def get_status(self):
		return self.status_assigned

    def check_out(self):
        self.time_out = timezone.now()
        self.save()

    def check_in(self):
    	th_person = self.person
    	th_item = self.item
    	th_time_out = self.time_out
    	th_time_in = timezone.now()
    	
    	th = TransactionHistory.objects.create(person=th_person, item=th_item, time_out=th_time_out, time_in=th_time_in)
        th.save()
    	th_item = None
        
        self.delete()

    def __str__(self):
        text = ' '.join([self.item.display_name, str(self.time_out), '(', self.person.full_name, ')'])
        encoded = text.encode("utf-8")
        return encoded

class Item(models.Model):
    category = models.ForeignKey('Category', blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)
    serial = models.CharField(max_length=255, blank=True, null=True)
    inventory_tag = models.CharField(max_length=255)

    def _get_history(self):
      "Returns all items assigned to the person."
      return TransactionHistory.objects.filter(item=self)

    history = property(_get_history)

    def is_available(self):
      try:
        transaction = Transaction.objects.get(item=self)
        assigned_to = transaction.person
        status = assigned_to.full_name
      except Transaction.DoesNotExist:
        status = "available"
      return ( status )
    
    def name(self):
      text = self.display_name
      encoded = text.encode("utf-8")
      return encoded

    def __str__(self):
      text = self.display_name
      encoded = text.encode("utf-8")
      return encoded

    class Meta:
      ordering = ['display_name']
				

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
				verbose_name_plural = "categories"
				ordering = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    class Meta:
				ordering = ['name']

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    graduation_year = models.CharField(max_length=4)
    active = models.BooleanField(default=True)

    def _isActive(self):
        "Is the user active in the system."
        return self.active

    def _get_history(self):
        "Returns all items assigned to the person."
        return TransactionHistory.objects.filter(person=self).order_by('-time_out')

    def _get_inventory(self):
        """Returns all inventory currently assigned to the person."""
        return Transaction.objects.filter(person=self).filter(time_out__isnull=False)

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    history = property(_get_history)
    inventory = property(_get_inventory)
    full_name = property(_get_full_name)
    objects = models.Manager()

    def __str__(self):
        return self.full_name

    class Meta:
				ordering = ['-active', 'id_number']
				verbose_name_plural = "people"