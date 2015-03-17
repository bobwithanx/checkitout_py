if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mths_ems.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import csv
from checkout.models import Item, Category, Brand, Transaction

with open('import/inventory.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	for my_item in reader:
		item = Item()  
		item.category = Category.objects.get(pk=my_item[0])
		item.brand = Brand.objects.get(pk=my_item[1])
		item.model = my_item[2]
		item.serial = my_item[3]
		item.save()
