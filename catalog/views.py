from django.shortcuts import render
from catalog.models import Product

# Create your views here.
def index_home_page(requests):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }
    return render(requests, 'home_page.html', context)

def index_contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')

        print(requests)
        print(f"Имя: {name}\nНомер телефона: {phone}\nСообщение:{message}")
    return render(requests, 'contacts.html')

def index_catalog(requests):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }
    return render(requests, 'catalog.html', context)

