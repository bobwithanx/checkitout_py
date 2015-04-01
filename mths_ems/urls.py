from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mths_ems.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'checkout.views.dashboard', name='dashboard'),
    url(r'^student/', include('checkout.urls')),
    url(r'^reports/$', 'checkout.views.reports', name="reports"),
    url(r'^history/$', 'checkout.views.history', name="history"),
    url(r'^admin/', include(admin.site.urls), name="admin"),
    url(r'^item/$', 'checkout.views.item_list'),
    url(r'^item/(?P<pk>[0-9]+)$', 'checkout.views.item_detail'),
    url(r'^check_in/$', 'checkout.views.check_in', name="check-in"),
    url(r'^reservations/$', 'checkout.views.reservations', name="reservation-list"),
    url(r'^reservations/cancel/(?P<pk>[0-9]+)/$', 'checkout.views.cancel_reservation', name="cancel-reservation"),
    
    # Login/Logout URLs
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'checkout/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
)
