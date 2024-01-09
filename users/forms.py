from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country', 'password1', 'password2')


#улучшение формы авторизации по Балакиреву, с использванием функции get_user_model(), пока не работает
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
#         fields = ['username', 'password']
