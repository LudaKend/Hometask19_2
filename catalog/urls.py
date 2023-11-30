#from django.contrib import admin
from django.urls import path
from catalog.views import index_home_page
from catalog.views import index_contacts
from catalog.views import index_catalog
from catalog.views import index_product
from catalog.apps import CatalogConfig


# urlpatterns_home_page = [
#     path('', index_home_page),
# ]
#
# urlpatterns_contacts = [
#     path('contacts', index_contacts),
# ]

app_name = CatalogConfig.name

urlpatterns = [
    path('', index_home_page, name='route_home_page'),
    path('contacts/', index_contacts, name='route_contacts'),
    path('catalog/', index_catalog, name='route_catalog'),
    path('object/<int:pk>/', index_product, name='route_product'),
]
