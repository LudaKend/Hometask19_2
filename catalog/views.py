from django.shortcuts import render

# Create your views here.
def index_home_page(requests):
    return render(requests, 'home_page.html')

def index_contacts(requests):
    return render(requests, 'contacts.html')
