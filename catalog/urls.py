#from django.contrib import admin
from django.urls import path
from catalog.views import index_home_page
from catalog.views import index_contacts
from catalog.views import index_catalog

# urlpatterns_home_page = [
#     path('', index_home_page),
# ]
#
# urlpatterns_contacts = [
#     path('contacts', index_contacts),
# ]

urlpatterns = [
    path('', index_home_page),
    path('contacts/', index_contacts),
    path('catalog/', index_catalog),
]
