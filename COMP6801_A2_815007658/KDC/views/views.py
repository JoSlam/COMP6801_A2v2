from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

from KDC.models.forms import KDCUserForm
from KDC.models.forms.KDCUserForm import KDCUserForm


def index(request):
    return HttpResponse("Hello, world. You're at the KDC index.")


def login(request):
    return HttpResponse("Hello, world. You're at the KDC user login page.")


def register(request):
    return render(request, "account/register.html")


class UserFormView(View):
    form_class = KDCUserForm
    template_name = 'account/register.html'

    # display blank form for signup
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # register user with supplied form info.
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = self.form_class()
            user.save(form.cleaned_data['username'], form.cleaned_data['password'])

        return redirect("KDC:index")
