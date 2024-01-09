from django.shortcuts import render, redirect
from django.views.generic import CreateView
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterForm, UserLoginForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import smtplib
from django.conf import settings

class RegisterView(CreateView):
    '''контроллер для регистрации пользователя'''
    model = User
    form_class = UserRegisterForm  #UserCreationForm
    template_name = 'users/register.html'

    success_url = reverse_lazy('users:route_login_users')

class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю'''
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'


def index_reset_password(requests):
    '''контроллер для сброса пароля'''
    if requests.method == 'POST':
        email = requests.POST.get('email') #получить значение поля Почта

        #здесь нужно проверить наличие пользователя с указанным email в БД
        users_list = User.objects.filter(is_active=True)
        for user in users_list:
            print(user)
            if email == user.email:
                #генерируем новый пароль и отправляем по указанному адресу пользователю
                new_password = make_password(password='8')
                print(f'новый пароль: {new_password}')  #генерит какой-то длинный хэш
                try:
                    send_mail('Новый пароль для магазина продуктов', new_password, settings.EMAIL_HOST_USER, [email])
                except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPNotSupportedError) as smtp_error:
                    print(smtp_error)
                #еще нужно новый пароль записать в БД, иначе пользователь с новым паролем не сможет зайти
                temp_user = User.objects.get(email=email)
                temp_user.set_password(new_password)
                temp_user.save()
                #context = {'message': 'Новый пароль выслан на почту, повторите процедуру авторизации'}
                redirect(reverse('users:route_login_users')) #не работает
                # success_url = reverse_lazy('users:route_login_users')
    return render(requests,'users/password_reset.html')
    #return render(requests, 'users/login.html')

#success_url = reverse_lazy('catalog:route_home_page')
    # def form_invalid(self, form):
    #     print('некорректный ввод')

    # def login_user(request):
    #     '''метод дополняет контроллер логирования. При неверном вводе пароля предлагается верификация'''
    #     if request.method == 'POST':
    #         form = LoginUserForm(request.POST)
    #         if form.is_valid():        #проверка, что форма авторизации прошла проверки успешно
    #             cd = form.cleaned_data
    #             user = authenticate(request, username=cd['username'], password=cd['password'])
    #             if user and user.is_active:
    #                 login(request, user)
    #                 print('некорректный ввод')
    #                 return HttpResponseRedirect(reverse('home'))
    #     else:
    #         form = LoginUserForm()
    #     return render(request, 'users/login.html', {'form': form})
