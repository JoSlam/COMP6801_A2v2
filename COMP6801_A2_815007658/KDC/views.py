from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from KDC.modules import *
from KDC.models.forms.UserForm import UserForm
from KDC.models.User import User


def index(request):
    return HttpResponse("Hello, world. You're at the KDC index.")


def login(request):
    return HttpResponse("Hello, world. You're at the KDC user login page.")


def register_success(request):
    return render(request, "account/register_success.html")

def dashboard(request):
    # get applications registered with kdc
    return render(request, 'dashboard.html')

class UserRegistrationView(View):
    form_class = UserForm
    template_name = 'account/register.html'

    # display blank form for signup
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # register user with supplied form info.
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            
        return redirect("KDC:register_success")


class UserLoginView(View):
    form_class = UserForm
    template_name = 'account/login.html'

    # display blank form for login
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # login user with supplied form info.
    def post(self, request):
        form = self.form_class(request.POST)
        login_user(form)

        return redirect("KDC:dashboard")

    
    