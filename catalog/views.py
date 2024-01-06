from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator

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

#прикручиваю формсет#
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
#прикручиваю формсет#

    def get_success_url(self):
        return reverse_lazy('catalog:route_product', args=[self.kwargs.get('pk')])


class CatalogListView(ListView):
    model = Product

    paginate_by = 4

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

