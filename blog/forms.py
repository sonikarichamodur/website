from django import forms
from .models.files import Files


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'fil']
