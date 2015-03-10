from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mths_ems.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('checkout.urls')),
    url(r'^student/', include('checkout.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
