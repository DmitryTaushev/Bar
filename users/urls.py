from django.urls import path

from users.apps import UsersConfig
from users.views import UserRegisterView,UserLoginView,user_profile_view,user_logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(),name='user_login'),
    path('register/',UserRegisterView.as_view(),name='user_register'),
    path('profile/',user_profile_view,name='user_profile'),
    path('logout/',user_logout_view,name='user_logout')
]