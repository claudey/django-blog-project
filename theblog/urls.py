from django.conf.urls import patterns, include, url
import blog.urls
import reg.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theblog.views.home', name='home'),
    # url(r'^theblog/', include('theblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.home'),
	url(r'^', include(blog.urls)),
	url(r'^reg/', include(reg.urls)),
)
