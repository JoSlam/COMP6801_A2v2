from django import forms
from KDC.models.KDCUser import KDCUser


class KDCUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = KDCUser
        fields = ['username', 'password']
