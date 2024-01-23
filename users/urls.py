from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserLoginView, index_reset_password, index_verify

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='route_login_users'),
    path('logout/', LogoutView.as_view(), name='route_logout_users'),
    path('register/', RegisterView.as_view(), name='route_register_users'),
    path('reset/', index_reset_password, name='route_reset_password'),
    path('verify/', index_verify, name='route_verify'),
    #path('redirect-success/', index_verify, name='route_login_users')
    #path('verify/', index_verify, name='route_verify'),

    ##этот патч в ошибку не валится, но и не перенаправляет на страницу входа, им всё-таки сломала, теперь по кнопке Войти сразу на страницу верификации попадаю
    ##path('verify/redirect-success/', index_verify, name='route_login_users')

    #path('verify/redirect-success/login/', index_verify, name='route_login_users') - ошибка!
]
