from django.conf.urls import *
from cms.models import Story
from django.views.generic import DetailView, ListView

urlpatterns = patterns('django.views.generic',
    url(r'^$', ListView.as_view(queryset=Story.objects.all(),
        context_object_name='story_list'),
        name="cms-home"
    ),
    url(r'^(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Story), name="cms-story"),
)

urlpatterns += patterns('cms.views',
    url(r'^category/(?P<slug>[-_\w]+)/$', 'category', name="cms-category"),
    url(r'^search/$', 'search', name="cms-search"),
)
