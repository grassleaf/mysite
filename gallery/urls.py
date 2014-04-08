from django.conf.urls import *
from gallery.models import Item, Photo
from django.views.generic import TemplateView, DetailView, ListView
# from gallery.views import ItemListView, ItemDetailView, PhotoDetailView

urlpatterns = patterns('django.views.generic',
    url(r'^$', TemplateView.as_view(template_name="gallery.html"),
        name = 'gallery'
    ),
    # url(r'^items/$', ItemListView.as_view(),
    #     name='item_list'
    # ),
    # url(r'^items/(?P<slug>[-_\w]+)/$', ItemDetailView.as_view(),
    #     name='item_detail'
    # ),
    # url(r'^photos/(?P<slug>[-_\w]+)/$', PhotoDetailView.as_view(), 
    #     name='photo_detail'
    # ),
    url(r'^items/$', ListView.as_view(queryset=Item.objects.all(),
        context_object_name='object_list', template_name='items_list.html'),
        name='item_list'
    ),
    url(r'^items/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Item,
        template_name='items_detail.html'),
        name='item_detail'
    ),
    url(r'^photos/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Photo,
        template_name='photos_detail.html'),
        name='photo_detail'
    ),
)
