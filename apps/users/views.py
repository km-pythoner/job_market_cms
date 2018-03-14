from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View

from .forms import RegisterForm


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        pass


