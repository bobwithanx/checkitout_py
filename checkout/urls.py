from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.person_list, name="person-list"),
    url(r'^search/$', views.person_search, name="person-search"),
    url(r'^(?P<pk>[0-9]+)/$', views.person_detail, name="person-detail"),
    url(r'^(?P<pk>[0-9]+)/history$', views.person_history, name="person-history"),
    url(r'^(?P<pk>[0-9]+)/search/$', views.item_search, name="item-search"),
    url(r'^(?P<pk>[0-9]+)/reserve/cancel$', views.person_cancel_reservation, name="reservation-cancel"),
    url(r'^(?P<p>[0-9]+)/reserve/(?P<i>[0-9]+)/$', views.reserve_item, name="reserve-item"),
    url(r'^(?P<p>[0-9]+)/checkout/(?P<i>[0-9]+)/$', views.checkout_item, name='item-checkout'),
    url(r'^(?P<pk>[0-9]+)/checkin/$', views.item_checkin, name='item-checkin'),
)
