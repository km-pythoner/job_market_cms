from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .forms import RegisterForm
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
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()

            #  send_register_email(email=user_name, send_type='R')
            return render(request, 'index.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


