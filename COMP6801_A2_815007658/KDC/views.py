from django.utils import timezone
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect

from KDC.modules import *
from KDC.models.User import User, UserApplication
from KDC.models.forms.UserForms import UserRegistrationForm, UserLoginForm

from TGS.models.Application import Application
from TGS.modules.tgs_supporting import *

from globals.globals import *
from django.http.response import JsonResponse

tgs_key = "tgs-key1"

def index(request):
    context = get_context(request)
    registered_ids = []

    if request.user.is_authenticated:
        registered = request.user.applications.values()

        for app in registered:
            registered_ids.append(app["id"])
    else:
        registered = None

    available = Application.objects.exclude(pk__in=registered_ids)
    context.update({"available": available, "registered": registered})

    return render(request, 'KDC/index.html', context)

def logout_user(request):
    if request.user is not None:
        logout(request)
    return redirect('app:index')


def connect_to_service(request, username):
    user = User.objects.get(username=username)

    if user is not None:
        userApp = UserApplication.objects.get(user=user)
        encrypted_tgt = userApp.tgt

        #tgs creds
        tgt = decrypt(encrypted_tgt, tgs_key)
        tgt_username = tgt.split(",")[0]
        tgt_nonce = tgt.split(",")[1]

        #user creds
        nonce = decrypt(userApp.nonce, user.password[:8])

        if nonce == tgt_nonce and user.username == tgt_username:
            return JsonResponse({ 'data': "You have successfully been authenticated with the application."})
    return JsonResponse({ 'data': "You have failed to be authenticated by the application." })


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


