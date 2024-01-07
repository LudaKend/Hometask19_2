from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='route_login_users'),
    path('logout/', LogoutView.as_view(), name='route_logout_users'),
]
