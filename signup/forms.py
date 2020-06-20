
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignUpForm(UserCreationForm):
    # birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
