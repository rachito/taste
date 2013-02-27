from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'taste.views.home', name='home'),
    # url(r'^taste/', include('taste.foo.urls')),

    #Django
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #principal app
    url(r'^$', 'taste.principal.views.index'),
)
