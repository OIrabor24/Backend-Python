from django import forms
from django.forms import ModelForm
from .models import File

class UploadForm(ModelForm):
    class Meta: # this class describes the characteristics of this form
        model = File 
        fields = ['name', 'file'] # these fields come from our model fields
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'filename'})
        } 
