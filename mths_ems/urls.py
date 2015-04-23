from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mths_ems.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'checkout.views.search', name='search'),
    url(r'^dashboard/$', 'checkout.views.dashboard', name="dashboard"),
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
