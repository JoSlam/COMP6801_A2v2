from django.forms import ModelForm
from TGS.models.Application import Application

class ApplicationForm(ModelForm):

    class Meta:
        model = Application
        fields = ['name', 'key']