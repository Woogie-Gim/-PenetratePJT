from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm):
    model = get_user_model()
    fields = ('username', 'email', 'first_name', 'last_name')

class CustomUserChangeForm(UserChangeForm):
  password = forms.CharField(label="Password", widget=forms.HiddenInput)
  class Meta(UserChangeForm):
    model = get_user_model()
    fields = ('email', 'first_name', 'last_name', 'username')