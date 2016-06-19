from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.person_list, name="person-list"),
    url(r'^(?P<tab>[a-z]+)/$', views.person_list, name="person-list"),
    url(r'^/search/$', views.person_search, name="person-search"),
    url(r'^(?P<id_number>[0-9]+)/$', views.person_detail, name="person-detail"),
    url(r'^(?P<id_number>[0-9]+)/history$', views.person_history, name="person-history"),
    url(r'^(?P<id_number>[0-9]+)/search/$', views.item_search, name="item-search"),
    url(r'^(?P<id_number>[0-9]+)/browse/$', 'checkout.views.browse_items', name="browse-items"),
    url(r'^(?P<id_number>[0-9]+)/checkout/$', views.display_checkout),
    url(r'^(?P<id_number>[0-9]+)/checkout/(?P<inventory_tag>[0-9]+)/$', views.display_checkout),
    url(r'^(?P<p>[0-9]+)/quick_checkout/$', views.quick_checkout, name="quick-checkout"),
    url(r'^(?P<p>[0-9]+)/checkout/(?P<i>[0-9]+)/$', views.checkout_item, name='item-checkout'),
    url(r'^(?P<pk>[0-9]+)/checkin/$', views.item_checkin, name='item-checkin'),
)
