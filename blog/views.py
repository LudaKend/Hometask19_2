from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog_post
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify


class BlogCreateView(CreateView):
    '''класс-контроллер,работающий с шаблоном blog_post_form.html'''
    model = Blog_post
    fields = ('head', 'slug', 'content', 'preview',)

    success_url = reverse_lazy('blog:route_blog_post_list')
    def form_valid(self, form):
        '''метод для формирования slug'''
        if form.is_valid():  #проверка, что форма с наполнением для новой статьи прошла проверки успешно
            new_blog_post = form.save()
            new_blog_post.slug = slugify(new_blog_post)
            new_blog_post.save()
        return super().form_valid(form)


class BlogListView(ListView):
    '''класс-контроллер,работающий с шаблоном blog_post_list.html'''
    model = Blog_post
    def get_queryset(self, *args, **kwargs):
        '''метод для фильтрации постов в блоге: выводим только is_published = True'''
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class BlogDetailView(DetailView):
    '''класс-контроллер,работающий с шаблоном blog_post_detail.html'''
    model = Blog_post

    def get_object(self, queryset=None):
        '''метод для получения количества просмотров у статьи в блоге'''
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogUpdateView(UpdateView):
    '''класс-контроллер,работающий с шаблоном blog_post_form.html'''
    model = Blog_post
    fields = ('head', 'slug', 'content', 'preview', 'is_published',)


    def get_success_url(self):
        return reverse_lazy('blog:route_blog_post_view', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    '''класс-контроллер,работающий с шаблоном blog_post_confirm_delete.html'''
    model = Blog_post

    success_url = reverse_lazy('blog:route_blog_post_list')

