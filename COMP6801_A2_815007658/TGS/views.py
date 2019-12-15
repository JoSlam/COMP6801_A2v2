from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseServerError


from TGS.models.forms.ApplicationForm import ApplicationForm
from TGS.models.Application import Application
from TGS.modules.tgs_supporting import *

from KDC.models.User import UserApplication

from globals.globals import *
from django.http.response import HttpResponse

tgs_key = "tgs-key1"

def index(request):
    context = get_context(request)
    all_apps = Application.objects.all()
    context.update({"app_list": all_apps})
    return render(request, 'TGS/index.html', context)

def app_details(request, app_id):
    context = get_context(request)
    app = Application.objects.get(pk=app_id)
    context.update({"app": app})
    return render(request, "TGS/application_form.html", context)


class ApplicationCreationView(View):
    form_class = ApplicationForm
    template_name = 'TGS/application_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        context = get_context(request)
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            context.update({ "message": "Application created successfully!" })
            context.update({ "redirect_url": "/" })
            return render(request, "TGS/success.html", context)

        return HttpResponseServerError
        
    

class ApplicationEditView(View):
    form_class = ApplicationForm
    form_model = Application
    template_name = 'TGS/application_form.html'

    def get(self, request, app_id):
        context = get_context(request)
        app = get_object_or_404(self.form_model, pk=app_id)
        context.update({"app": app})
        context.update({"form": self.form_class(None)})

        return render(request, self.template_name, context)


    def post(self, request, app_id):
        context = get_context(request)

        app = self.form_model.objects.get(pk=app_id)
        form = self.form_class(request.POST or None, instance=app)

        if form.is_valid():
            form.save()
        context.update({"app": app})

        context.update({ "message": "Application edited successfully!" })
        context.update({ "redirect_url": "/tgs/application/edit/" + str(app.id) })
        return render(request, "TGS/success.html", context)
        

@login_required(login_url='/kdc/login/')
def add_app_to_user(request, app_id):
    context = get_context(request)
    user = request.user

    if user.is_authenticated:
        app = Application.objects.get(pk=app_id)

        #gen nonce and encrypt
        nonce = generate_nonce(1000)
        encrypted_nonce = encrypt(str(nonce), user.password[:8])

        #encrypt tgt
        app_key = app.key
        pre_tgt = user.username + "," + str(nonce)
        tgt = encrypt(pre_tgt, tgs_key)

        userApp = UserApplication(user=user, application=app, nonce=encrypted_nonce, tgt=tgt)
        userApp.save()

        context.update({ "message": "Application added to user!" })
        context.update({ "redirect_url": "/kdc/" })

        return render(request, "TGS/success.html", context)

    return redirect("KDC:index")
    
    