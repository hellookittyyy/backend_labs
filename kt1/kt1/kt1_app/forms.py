from django import forms
from .models import Url

class CreateUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url']

class UpdateUrlForm(forms.ModelForm):
    oldShortCode = forms.CharField(max_length=10, required=True)
    newShortCode = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Url
        fields = ['oldShortCode', 'newShortCode']

class DeleteUrlForm(forms.Form):
    shortCode = forms.CharField(max_length=10)
