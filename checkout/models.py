from django.db import models
from django.utils import timezone

class ActiveTransactions(models.Manager):
    def get_queryset(self):
        return super(ActiveTransactions, self).get_queryset().filter(in_time__isnull=True)


class ActivePeople(models.Manager):
    def get_queryset(self):
        return super(ActivePeople, self).get_queryset().filter(in_time__isnull=True).order_by('person').distinct()


class Transaction(models.Model):
    status_assigned = 'ASSIGNED'
    status_reserved = 'RESERVED'
    status_returned = 'RETURNED'
    
    person = models.ForeignKey('Person')
    item = models.ForeignKey('Item')
    out_time = models.DateTimeField(blank=True, null=True)
    in_time = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    active_objects = ActiveTransactions()
    active_people = ActivePeople()
    with_inventory = active_people

    def is_reserved(self):
        return self.status() == self.status_reserved
        
    def is_assigned(self):
        return self.status() == self.status_assigned
        
    def is_returned(self):
        return self.status() == self.status_returned
        
    def get_status(self):
        if self.out_time == None:
            return self.status_reserved
        elif self.in_time == None:
            return self.status_assigned
        else:
            return self.status_returned

    def checkout(self):
        self.out_time = timezone.now()
        self.save()

    def checkin(self):
        self.in_time = timezone.now()
        self.item.assign(None)
        self.save()

    def cancel_reservation(self):
        self.delete()
    

    def __init__(self, person, item):
        if item.is_available():
            self.person = person
            self.item = item
            self.item.set_transaction(self)

    def __str__(self):
        text = ' '.join([self.item.brand.name, self.item.model, self.get_status(), str(self.out_time), ' -> ', str(self.in_time), '(', self.person.full_name, ')'])
        encoded = text.encode("utf-8")
        return encoded

class ItemsAssigned(models.Manager):
    def get_queryset(self):
        return super(ItemsAssigned, self).get_queryset().filter(current_transaction__isnull=False)

class ItemsAvailable(models.Manager):
    def get_queryset(self):
        return super(ItemsAvailable, self).get_queryset().filter(current_transaction__isnull=True)

class Item(models.Model):
    category = models.ForeignKey('Category')
    brand = models.ForeignKey('Brand')
    model = models.CharField(max_length=255)
    serial = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    current_transaction = models.ForeignKey('Transaction', blank=True, null=True)

    objects = models.Manager()
    available_items = ItemsAvailable()
    assigned_items = ItemsAssigned()

    def update_transaction(self, transaction=None):
        self.current_transaction = transaction
        self.save()

    def is_available(self):
        return( self.current_transaction == None )

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
    icon = models.Image(blank=True, null=True)

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

    def get_history(self):
        "Returns all items assigned to the person."
        return Transaction.objects.filter(person=self)

    def get_inventory(self):
        """Returns all items currently assigned to the person."""
        return Transaction.objects.filter(in_time__isnull=True).filter(person=self)

    def _get_full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)

    def __str__(self):
        return self.full_name
