from django.views.generic import TemplateView, DetailView, ListView

from gallery.models import Item, Photo

# class ItemListView(ListView):
#     model = Item
#     context_object_name = 'object_list'
#     template_name = "items_list.html"

#     def get_context_data(self, **kwargs):
#         context = super(ItemListView, self).get_context_data(**kwargs)
#         return context

#     # def get_queryset(self):
#     #     queryset = super(ItemListView, self).get_queryset()
#     #     return queryset

# class ItemDetailView(DetailView):
#     model = Item
#     context_object_name = 'object'
#     template_name = "items_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super(ItemDetailView, self).get_context_data(**kwargs)
#         return context

#     # def get_object(self, queryset=None):
#     #     return super(ItemDetailView, self).get_object()

# class PhotoDetailView(DetailView):
#     model = Photo
#     context_object_name = 'object'
#     template_name = "photos_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super(PhotoDetailView, self).get_context_data(**kwargs)
#         return context

class AboutView(TemplateView):
    template_name = "about.html"