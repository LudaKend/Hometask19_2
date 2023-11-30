from django.shortcuts import render, get_object_or_404
from catalog.models import Product


# Create your views here.
def index_home_page(requests):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list,
        'name_page': 'Главная'
    }
    return render(requests, 'catalog/home_page.html', context)

def index_contacts(requests):
    context = {
        'name_page': 'Контакты'
    }
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')

        print(requests)
        print(f"Имя: {name}\nНомер телефона: {phone}\nСообщение:{message}")
    return render(requests, 'catalog/contacts.html', context)

def index_catalog(requests):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list,
        'name_page': 'Каталог'
    }
    return render(requests, 'catalog/catalog.html', context)

def index_product(requests, pk):
    card_product = get_object_or_404(Product, pk=pk)
    #card_product = Product.objects.all()
    #print(card_product)
    context = {
        'object': card_product,
        'name_page': 'Карточка продукта'
    }
    return render(requests, 'catalog/product.html', context)
