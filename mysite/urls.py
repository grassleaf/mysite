from django.conf.urls import *
from django.conf import settings
# from mysite.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', 'index'),
    url(r'^', include('accounts.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^cms/', include('cms.urls')),

    url(r"^media/(?P<path>.*)$", "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT,}),
)

# urlpatterns += patterns('django.contrib.flatpages.views',
#     (r'^(?P<url>.*/)$', 'flatpage'),
# )