from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm
from django.urls import reverse_lazy

def index_home_page(requests):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list,
        'name_page': 'Главная'
    }
    return render(requests, 'catalog/home_page.html', context)

class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('catalog:route_product_list')

class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductForm


class CatalogListView(ListView):
    model = Product


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
    context = {
        'object': card_product,
        'name_page': 'Карточка продукта'
    }
    return render(requests, 'catalog/product.html', context)

class CatalogDetailView(DetailView):
    model = Product

