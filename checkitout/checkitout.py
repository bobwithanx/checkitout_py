"""
WSGI config for mths_ems project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
from site import addsitedir
# from django.core.handlers.wsgi import WSGIHandler

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
sys.path.append('/Users/Shared/checkitout/checkout')
sys.path.append('/Users/Shared/checkitout/checkitout')
sys.path.append('/Usres/Shared/checkitout')

addsitedir('/Users/Shared/checkitout/lib/python2.7/site-packages')
# application = WSGIHandler()
application = get_wsgi_application()
