from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from catalog.forms import ProductForm, VersionForm
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from utils import get_category_from_cache


def index_home_page(requests):
    # products_list = Product.objects.all()
    # context = {
    #     'objects_list': products_list,
    #     'name_page': 'Главная'
    # }
    categories_list = get_category_from_cache()
    context = {
        'objects_list': categories_list,
        'name_page': 'Главная'
    }
    return render(requests, 'catalog/home_page.html', context)

class CatalogCreateView(PermissionRequiredMixin, CreateView):
    '''класс-контроллер для создания Карточки продукта,работающий с шаблоном product_form.html'''
    model = Product
    form_class = ProductForm
    extra_context = {'name_page': 'Создание Карточки продукта'}
    permission_required = 'catalog.add_product'

    success_url = reverse_lazy('catalog:route_product_list')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user = self.get_object()   #беру текущего юзера, который залогинился
        self.object = form.save()  #сначала нужно сохранить
        self.object.author = user  #записываю текущего пользователя в качестве автора
        self.object = form.save()  #измененные данные сохраняю
        return super().form_valid(form)

class CatalogUpdateView(PermissionRequiredMixin,UpdateView):
    '''класс-контроллер для внесения изменений в Карточку продукта,работающий с шаблоном product_form.html'''
    model = Product
    form_class = ProductForm
    extra_context = {'name_page': 'Изменение Карточки продукта'}

    permission_required = 'catalog.change_product' #['reset_is_published', 'change_category', 'change_description']

    # def get_permission_required(self):
    #     '''метод для получения атрибута permission_required в зависимости от группы полномочий, присвоенной пользователю'''
    #     print(self.object.groups)
    #     if self.object.groups == 3 and self.object.author == self.user.email:
    #         #для пользователей с группой полномочий suppliers(поставщики),изменять позволено только автору
    #         self.permission_required = 'catalog.change_product'
    #     elif self.object.groups == 3:
    #         #для пользователей с группой полномочий moderators(модераторы),изменять можно только 3 поля
    #         self.permission_required = ['reset_is_published', 'change_category', 'change_description']
    #     return self.permission_required


    def get_object(self, queryset=None):
        '''изменять продукт можно только автору'''
        self.object = super().get_object(queryset)
        print(self.object)  #для отладки
        #сначала надо проверить, если пользователь является модератором, то ему можно изменить 3 поля
        user = self.request.user  # беру текущего юзера, который залогинился
        print(user) #для отладки
        #temp_user_id = self.request.user.id
        #print(temp_user_id)  #для отладки
        #group_id = self.request.user.groups.filter(user_id=temp_user_id)
        #print(group_id)
        is_moderator = user.groups.filter(name='moderators').exists()
        print(is_moderator) #для отладки
        #if user.has_perm('catalog.reset_is_published_product'):
        print(user.has_perm('catalog.reset_is_published'))
        if is_moderator:
            print('К изменению доступны только 3 поля')
            #return reverse_lazy('catalog:route_home_page') #- не работает
        else:
            if self.object.author != self.request.user:
                raise Http404('Изменения доступны только поставщику товара')
        return self.object


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


class CatalogListView(LoginRequiredMixin, ListView):
    '''класс-контроллер,работающий с шаблоном product_list.html'''
    model = Product
    extra_context = {'name_page': 'Каталог продуктов'}

    paginate_by = 4


def index_contacts(requests):
    '''функция-контроллер для страницы контактов'''
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

# def index_catalog(requests):
#     '''функция-контроллер для страницы Каталог(catalog.html),
#     заменена на класс-контроллер CatalogListView,работающий с шаблоном product_list.html'''
#     products_list = Product.objects.all()
#     context = {
#         'objects_list': products_list,
#         'name_page': 'Каталог'
#     }
#     return render(requests, 'catalog/catalog.html', context)

# def index_product(requests, pk):
#     '''функция-контроллер для страницы Карточка продукта(product.html),
#     заменена на класс-контроллер CatalogDetailView,работающий с шаблоном product_detail.html'''
#     card_product = get_object_or_404(Product, pk=pk)
#     context = {
#         'object': card_product,
#         'name_page': 'Карточка продукта'
#     }
#     return render(requests, 'catalog/product.html', context)

class CatalogDetailView(DetailView):
    '''класс-контроллер для страницы Карточка продукта,работающий с шаблоном product_detail.html'''
    model = Product
    extra_context = {'name_page': 'Карточка продукта'}

