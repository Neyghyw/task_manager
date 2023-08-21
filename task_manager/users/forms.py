from django.contrib.auth.models import User
from django.forms.fields import CharField
from django.forms.forms import Form
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm


class LoginForm(Form):
    username = CharField(min_length=3, max_length=150, label='username')
    password = CharField(min_length=3, max_length=150, label='password')


class UserUpdateForm(ModelForm, SetPasswordForm):
    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        SetPasswordForm.__init__(self, user=self.instance)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'new_password1', 'new_password2']


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

