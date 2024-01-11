from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from users.models import User
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserPasswordResetForm(PasswordResetForm):
    class Meta:
        model = User
