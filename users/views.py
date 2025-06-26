from django.shortcuts import render, reverse, redirect

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, UserForm


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

class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_profile.html'

    def get_object(self,queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        context_data['title'] = f'Ваш профиль {self.get_object()}'
        return context_data




def user_logout_view(request):
    logout(request)
    return redirect('drinks:index')
