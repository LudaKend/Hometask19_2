from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

# пишем на CBV для приложение blog
urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='route_blog_post_form'),
    path('', BlogListView.as_view(), name='route_blog_post_list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='route_blog_post_view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='route_blog_post_edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='route_blog_post_delete'),
]
