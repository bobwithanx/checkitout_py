#from django.conf.urls.defaults import *

from django.conf.urls import patterns, include, url
from django.contrib import admin
import checkout.views
import settings

#urlpatterns = patterns('',
#    url(r'^$', 'checkout.views.home', name='home'),
  #  url(r'^%s$' % settings.SUB_SITE, 'checkout.views.home', name='home'),
 #   url(r'^%s/' % settings.SUB_SITE, include('urls_subsite')),
#)

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
    url(r'static/$', no_view, name='static_root'),

    url(r'^$', checkout.views.home),
    url(r'^checkout$', checkout.views.display_checkout),
    url(r'^dashboard/$', checkout.views.dashboard),
    url(r'^students/$', checkout.views.person_list),
    url(r'^students/all/$', checkout.views.person_list),
    url(r'^students/create/$', checkout.views.person_create),
    url(r'^reports/$', checkout.views.reports),
    url(r'^loans/$', checkout.views.loans),
    url(r'^history/$', checkout.views.history),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^item/$', checkout.views.item_list),
    url(r'^items/all/$', checkout.views.item_list),
    url(r'^item/create/$', checkout.views.item_create),
    url(r'^item/(?P<pk>[0-9]+)/details/$', checkout.views.item_popup),
    url(r'^transaction/cancel/(?P<t>[0-9]+)/$', checkout.views.delete_transaction),

    #url(r'^students/(?P<tab>[a-z]+)/$', views.person_list, name="person-list"),
    url(r'^students/search/$', checkout.views.person_search),
    url(r'^students/(?P<id_number>[0-9]+)/$', checkout.views.person_detail),
    url(r'^students/(?P<id_number>[0-9]+)/history$', checkout.views.person_history),
    url(r'^students/(?P<id_number>[0-9]+)/search/$', checkout.views.item_search),
    url(r'^students/(?P<id_number>[0-9]+)/browse/$', checkout.views.browse_items),
    url(r'^students/(?P<id_number>[0-9]+)/checkout/$', checkout.views.display_checkout),
    url(r'^students/(?P<id_number>[0-9]+)/checkout/(?P<inventory_tag>[0-9]+)/$', checkout.views.display_checkout),
    url(r'^students/(?P<p>[0-9]+)/quick_checkout/$', checkout.views.quick_checkout),
    url(r'^students/(?P<p>[0-9]+)/checkout/(?P<i>[0-9]+)/$', checkout.views.checkout_item),
    url(r'^students/(?P<pk>[0-9]+)/checkin/$', checkout.views.item_checkin),

    # Login/Logout URLs
    url(r'^login/$', admin.site.login, {'template_name': 'checkout/login.html'}),
    url(r'^logout/$', admin.site.logout, {'next_page': '/'}),
)
