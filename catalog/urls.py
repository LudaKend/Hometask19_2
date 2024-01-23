from django.urls import path
from catalog.views import index_home_page
from catalog.views import index_contacts
from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, CatalogDetailView, CatalogUpdateView, CatalogCreateView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

# было на FBV
# urlpatterns = [
#     path('', index_home_page, name='route_home_page'),
#     path('contacts/', index_contacts, name='route_contacts'),
#     path('catalog/', index_catalog, name='route_catalog'),
#     path('object/<int:pk>/', index_product, name='route_product'),
# ]

# стало на CBV
urlpatterns = [
    path('', index_home_page, name='route_home_page'),
    path('catalog/', CatalogListView.as_view(), name='route_product_list'),
    path('contacts/', index_contacts, name='route_contacts'),
    path('view/<int:pk>/', cache_page(60)(CatalogDetailView.as_view()), name='route_product'),
    path('create/', CatalogCreateView.as_view(), name='route_create_product'),
    path('update/<int:pk>/', CatalogUpdateView.as_view(), name='route_update_product'),
]
