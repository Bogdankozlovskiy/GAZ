from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from . import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

# Create your views here.
def index(request):
    # users_list = CustomUser.objects.all()
    users_list = User.objects.exclude(is_staff=True)
    context = {
        "users_list": users_list,
    }
    return render(request, 'administration/index.html', context)

def user_reg(request):
    # model = CustomUser

    if request.method == 'POST':
        form = forms.UserRegForm(request.POST)
        # form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/administration/')

    form_class = forms.UserRegForm
    # form_class = UserCreationForm
    context = {
        "form": form_class,
    }
    return render(request, 'administration/user-reg.html', context)
