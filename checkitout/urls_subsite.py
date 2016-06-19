from django.conf.urls import patterns, include, url
from django.contrib import admin

#from django.conf.urls.defaults import *
import settings

# NOTE: I don't really like defining this here, but the only other place it
# should logically go is in an overall site-level app.  Seems like too much
# overhead.
from django.shortcuts import Http404
def no_view(request):
    """
    We don't really want anyone going to the static_root.
    However, since we're raising a 404, this allows flatpages middleware to
    step in and serve a page, if there is one defined for the URL.
    """
    raise Http404

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mths_ems.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Special URL defined here, so that we have DRY in templates, without RequestContext.
    url(r'^static/$', no_view, name='static_root'),

    url(r'^$', 'checkout.views.home', name='home'),
    url(r'^checkout$', 'checkout.views.display_checkout'),
    url(r'^returns$', 'checkout.views.display_checkin', name="returns"),
    url(r'^quick_checkin$', 'checkout.views.quick_checkin', name='quick_checkin'),
    url(r'^dashboard/$', 'checkout.views.dashboard', name="dashboard"),
    url(r'^returns/?(?P<result>.+)/(?P<item>.+)?/$', 'checkout.views.display_checkin', name="returns"),
    url(r'^reservations/$', 'checkout.views.reservations', name="reservations"),
    url(r'^on_loan/$', 'checkout.views.on_loan', name="on_loan"),
    url(r'^student/', include('checkout.urls')),
    url(r'^reports/$', 'checkout.views.reports', name="reports"),
    url(r'^history/$', 'checkout.views.history', name="history"),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^item/$', 'checkout.views.item_list'),
    url(r'^item/(?P<pk>[0-9]+)/details/$', 'checkout.views.item_popup', name="item-popup"),
    url(r'^request/(?P<pk>[0-9]+)/cancel/$', 'checkout.views.person_cancel_request', name="person-cancel-request"),
    url(r'^transaction/cancel/(?P<t>[0-9]+)/$', 'checkout.views.delete_transaction', name="delete-transaction"),
    
    # Login/Logout URLs
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'checkout/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
