from django.shortcuts import render, reverse, redirect

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:user_login')
    template_name = 'users/user_register.html'
    extra_context = {
        'title': 'Создать аккаунт'
    }

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/user_login.html'
    extra_context = {
        'title':'Вход в аккаунт'
    }



def user_profile_view(request):
    user_object = request.user
    if user_object.first_name and user_object.last_name:
        user_name = user_object.first_name + ' ' + user_object.last_name
    else:
        user_name = user_object
    context = {
        'title': f'Ваш профиль {user_name}'
    }
    return render(request, 'users/user_profile.html', context=context)


def user_logout_view(request):
    logout(request)
    return redirect('drinks:index')
