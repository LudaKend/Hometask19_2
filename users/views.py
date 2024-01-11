import random
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from users.models import User
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserRegisterForm, UserLoginForm, UserPasswordResetForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import smtplib
from django.conf import settings
from django.contrib.auth.views import PasswordResetView
from django.contrib import messages

class RegisterView(CreateView):
    '''контроллер для регистрации пользователя'''
    model = User
    form_class = UserRegisterForm  #UserCreationForm
    template_name = 'users/register.html'

    #success_url = reverse_lazy('users:route_login_users')
    success_url = reverse_lazy('users:route_verify')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save() #сначала сохраняем данные о вновь введенном пользователе
        # генерируем ключ для верификации и отправляем по указанному адресу пользователю
        verification_key = ''.join([str(random.randint(0,9)) for _ in range(4)])
        #print(f'ключ: {verification_key}')  # для проверки
        try:
            send_mail('Ключ для подтверждения аккаунта от магазина продуктов', verification_key,
                      settings.EMAIL_HOST_USER, [self.object.email])
        except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPNotSupportedError) as smtp_error:
            print(smtp_error)
        # нужно ключ записать в БД, и пользователя пока сделать неактивным
        self.object.verification_key = verification_key
        self.object.is_active = False
        self.object = form.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю'''
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'
    #success_url = reverse_lazy('users:route_verify')
    success_url = reverse_lazy('catalog:home_page')
    error_message = 'не успешный вход'

    # def form_invalid(self, form):
    #     print('не успешный вход')
    #     #temp_user = form.save() #запишем экранные значения переменной
    #     temp_user = requests
    #     # print(self.user.email)
    #     # user_in_bd = User.objects.filter(email=temp_user.email)
    #     # print(user_in_bd)
    #     # if self.user_in_bd.is_active == False:
    #     #     redirect(reverse('users:route_verify'))
    #     messages.error(self.request, self.error_message)
    #     #return super().form_invalid(form)
    #     #return UpdateView.form_invalid(self, form)
    #     return index_verify(form)

    # def get_object(self, queryset=None):
    #     self.object = super().get_object()
    #     print(self.object)
    #     if self.object.is_active == False:
    #         success_url = reverse_lazy('users:route_verify')
    #     else:
    #         success_url = reverse_lazy('catalog:home_page')

# class UserListView(ListView):
#     model = User
#
#     def get_queryset(self, *args, **kwargs):
#         queryset = super().get_queryset()
#         return queryset

def index_verify(requests):
    '''контроллер для ввода ключа подтверждения'''
    if requests.method == 'POST':
        email = requests.POST.get('email') #получить значение поля Почта c экрана
        verify = requests.POST.get('verification_key') #получить значение Ключа с экрана
        #здесь выбираем пользователя с указанным email в БД
        users_list = User.objects.all()
        for user in users_list:
            #проверяю, чтобы ключ сходился
            if email == user.email and verify == user.verification_key:
                print(user)
                user.is_active = True
                user.save()
                print('пользователь успешно активирован, можно переходить к авторизации')
        # temp_user = User.objects.filter(email=email)
        # if email == temp_user.email and verify == temp_user.verification_key:
        #     temp_user.is_active = True
        #     temp_user.save()
        #     print('пользователь успешно активирован, можно переходить к авторизации')
    return render(requests, 'users/verify.html') #это страница на которой работает этот контроллер



def index_reset_password(requests):
    '''контроллер для сброса пароля'''
    if requests.method == 'POST':
        email = requests.POST.get('email') #получить значение поля Почта
        #здесь нужно проверить наличие пользователя с указанным email в БД
        #users_list = User.objects.filter(is_active=True)
        users_list = User.objects.all()
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
                #redirect(reverse('catalog:home_page')) #Reverse for 'home_page' not found. 'home_page' is not a valid view function or pattern name.
                # success_url = reverse_lazy('users:route_login_users')
                break
    return render(requests,'users/password_reset.html')
    #return render(requests, 'users/login.html')
    #return redirect(reverse('users:route_login_users')) #если так, то по кнопке "забыли пароль" не попадаю в password_reset.html


class UserPasswordResetView(PasswordResetView):
    '''контроллер для запуска процесса сброса пароля, на основе стандартного'''
    model = User
    form_class = UserPasswordResetForm
   #template_name = 'users/login.html'

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
