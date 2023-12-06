from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import Blog_post
from django.urls import reverse_lazy

# Create your views here.

class BlogCreateView(CreateView):
    model = Blog_post
    fields = ('head', 'slug', 'content', 'preview',)

    success_url = reverse_lazy('blog:route_blog_post_list')

class BlogListView(ListView):
    model = Blog_post

class BlogDetailView(DetailView):
    model = Blog_post

class BlogUpdateView(UpdateView):
    model = Blog_post
    fields = ('head', 'slug', 'content', 'preview', 'is_published',)

    success_url = reverse_lazy('blog:route_blog_post_list')

class BlogDeleteView(DeleteView):
    model = Blog_post

    success_url = reverse_lazy('blog:route_blog_post_list')

