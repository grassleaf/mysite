from django.conf.urls import *
from django.shortcuts import render_to_response

urlpatterns = patterns('accounts.views',

    url(r'^$', 'index'),
    ('^register/$', 'register'),
    ('^login/$', 'login'),
    ('^login_view/$', 'login_view'),
    ('^logout/$', 'logout'),
    ('^add_photo/$', 'add_photo'),
    ('^add_item/$', 'add_item'),
    ('^add_category/$', 'add_category'),
    ('^add_story/$', 'add_story'),
)