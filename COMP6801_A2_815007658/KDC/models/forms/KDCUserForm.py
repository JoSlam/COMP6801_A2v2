from django.forms import ModelForm
from KDC.models import KDCUserModel


class KDCUserForm(ModelForm):
    class Meta:
        model = KDCUserModel
        fields = ['username', 'password']
