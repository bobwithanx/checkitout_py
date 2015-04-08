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
        text = ' *** '.join([self.item.brand.name, self.item.model, str(self.time_out), str(self.time_in), self.person.full_name])
        encoded = text.encode("utf-8")
        return encoded


class Transaction(models.Model):
    status_assigned = 'Assigned'
    status_requested = 'Requested'
    
    person = models.ForeignKey('Person')
    item = models.ForeignKey('Item')
    time_requested = models.DateTimeField(blank=True, null=True)
    time_out = models.DateTimeField(blank=True, null=True)
	
    def is_requested(self):
        return self.status() == self.status_requested

    def cancel_request(self):
        self.delete()

    def get_status(self):
        if self.time_out == None:
            return self.status_requested
        else:
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
        text = ' '.join([self.item.brand.name, self.item.model, str(self.time_out), '(', self.person.full_name, ')'])
        encoded = text.encode("utf-8")
        return encoded

class Item(models.Model):
    category = models.ForeignKey('Category')
    brand = models.ForeignKey('Brand')
    model = models.CharField(max_length=255)
    serial = models.CharField(max_length=255, blank=True, null=True)
    inventory_tag = models.CharField(max_length=255, blank=True, null=True)
    barcode_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image_name = models.CharField(max_length=255, blank=True, null=True)

    def _get_history(self):
        "Returns all items assigned to the person."
        return TransactionHistory.objects.filter(item=self)

    history = property(_get_history)

    def is_available(self):
        #return( self.current_activity == None )
        pass

    def __str__(self):
        text = ' '.join([self.brand.name, self.model])
        encoded = text.encode("utf-8")
        return encoded

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    id_number = models.CharField(max_length=255)
    group = models.ForeignKey('Group', blank=True, null=True)

    def _get_history(self):
        "Returns all items assigned to the person."
        return TransactionHistory.objects.filter(person=self)

    def _get_requests(self):
        """Returns all items currently assigned to the person."""
        return Transaction.objects.filter(person=self).exclude(time_out__isnull=False)

    def _get_inventory(self):
        """Returns all items currently assigned to the person."""
        return Transaction.objects.filter(person=self).filter(time_out__isnull=False)

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    history = property(_get_history)
    requests = property(_get_requests)
    inventory = property(_get_inventory)
    full_name = property(_get_full_name)
    objects = models.Manager()

    def __str__(self):
        return self.full_name
