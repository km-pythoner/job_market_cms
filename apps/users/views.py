from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend

from .forms import RegisterForm, LoginForm
from .models import UserProfile


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(username=user_name):
                return render(request, 'register.html', {'msg': '用户名已存在！', 'register_form': register_form})
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return render(request, 'register.html', {'email': email, 'msg': '两次密码不一致！'})
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.password = make_password(pwd1)
            user_profile.is_active = False
            user_profile.save()

            #  send_register_email(email=user_name, send_type='R')
            return render(request, 'index.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'index.html')
        else:
            return render(request, 'index.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


