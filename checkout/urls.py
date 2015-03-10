from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.student_list),
    url(r'^(?P<pk>[0-9]+)/$', views.student_detail),
    url(r'^(?P<pk>[0-9]+)/checkout/$', views.list_available_items),
    url(r'^(?P<pk>[0-9]+)/checkin/$', views.item_checkin, name='item_checkin'),
    url(r'^(?P<s>[0-9]+)/checkout/(?P<i>[0-9]+)/$', views.item_checkout, name='item_checkout'),
    # url(r'^transaction/(?P<pk>[0-9]+)/$', views.transaction_detail),
    # url(r'^transaction/(?P<pk>[0-9]+)/checkin/$', views.transaction_checkin, name='transaction_checkin'),
    url(r'^transaction/new/$', views.transaction_new, name='transaction_new'),
)
