from django.urls import path
from catalog.views import index_home_page
from catalog.views import index_contacts
from catalog.views import index_catalog
from catalog.views import index_product
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

# было на FBV  в приложении catalog
# urlpatterns = [
#     path('', index_home_page, name='route_home_page'),
#     path('contacts/', index_contacts, name='route_contacts'),
#     path('catalog/', index_catalog, name='route_catalog'),
#     path('object/<int:pk>/', index_product, name='route_product'),
# ]

# пишем на CBV для приложение blog
urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDeleteView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
