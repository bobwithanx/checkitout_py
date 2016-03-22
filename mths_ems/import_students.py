if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import csv
from checkout.models import Person, Group

with open('import/students.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	
	for my_student in reader:
		student = Person()  
		student.first_name = my_student[0]
		student.last_name = my_student[1]
		student.id_number = my_student[2]
		student.group, created = Group.objects.get_or_create(name=my_student[3])
		student.save()
