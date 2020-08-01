from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# class UserRegForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

class UserRegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
