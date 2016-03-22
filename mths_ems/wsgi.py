"""
WSGI config for macmini project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

sys.path.append('/Users/Shared/checkitout')
sys.path.append('/Users/Shared/checkitout/mths_ems')
sys.path.append('/Users/Shared/checkitout/static')

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

import django.core.handlers.wsgi

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()