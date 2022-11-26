from django import forms
from .models import *

class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['Email']