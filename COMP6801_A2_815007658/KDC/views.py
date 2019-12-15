from django.utils import timezone
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect

from KDC.modules import *
from KDC.models import User
from KDC.models.forms.UserForms import UserRegistrationForm, UserLoginForm
from TGS.models.Application import Application

from globals.globals import *

def index(request):
    context = get_context(request)
    if request.user.is_authenticated:
        # registered = request.user.applications.exclude(pk__in=)
        registered = request.user.applications
    else:
        registered = None
    available = Application.objects.all()
    context.update({"available": available, "registered": registered})

    return render(request, 'KDC/index.html', context)

def logout_user(request):
    if request.user is not None:
        logout(request)
    return redirect('app:index')


class UserRegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'KDC/account/register.html'

    # display blank form for signup
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # register user with supplied form info.
    def post(self, request):
        context = get_context(request)
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        user = authenticate(username=form.cleaned_data.get("username"), password=form.cleaned_data.get("password"))
        if user is not None:
            if user.is_active:
                context.update({ "message": "User Registration Successful!" })
                context.update({ "redirect_url": "/kdc/login" })
                return render(request, "KDC/success.html", context)
        return HttpResponseServerError()
            


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'KDC/account/login.html'

    # display blank form for login
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # login user with supplied form info.
    def post(self, request):
        context = get_context(request)
        user = login_user(request, request.POST.get("username"), request.POST.get("password"))
        
        if user:
            context.update({"message": "Login successful!"})
            context.update({"redirect_url": "/kdc/"})
            return render(request, "KDC/success.html", context)
        else:
            return HttpResponseServerError()



