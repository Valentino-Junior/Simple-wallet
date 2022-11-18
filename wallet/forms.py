from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Wallet


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class DepositForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['balance']

class WithdrawForm(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = ['balance']
