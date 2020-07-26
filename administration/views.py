from django.shortcuts import render
from django.contrib.auth.views import LoginView
from . import forms
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def index(request):
    # users_list = CustomUser.objects.all()
    users_list = User.objects.all()
    context = {
        "users_list": users_list,
    }
    return render(request, 'administration/index.html', context)

def user_reg(request):
    # model = CustomUser

    if request.method == 'POST':
        form = forms.UserRegForm(request.POST)
        if form.is_valid():
            pass

    form_class = forms.UserRegForm
    context = {
        "form": form_class,
    }
    return render(request, 'administration/user-reg.html', context)
