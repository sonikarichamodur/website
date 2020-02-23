from django import forms
from .models.files import Files


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'fil']


class DeleteForm(forms.Form):
    ok = forms.BooleanField(label='Are You Sure?')


class UpdateFileForm(forms.Form):
    title = forms.CharField(label='Title', max_length=80)
    fil = forms.FileField(label="File", required=False)


class PasswordForm(forms.Form):
    passwd = forms.CharField(label="User Password", required=True, max_length=255, widget=forms.PasswordInput())


class StatsForm(forms.Form):
    pct_end = forms.IntegerField(label="Percentage of meeting max if no end", required=True, min_value=0, max_value=100)
    start = forms.DateField(label="Include signings only on/after this date", required=False)
    end = forms.DateField(label="Include signings only on/before this date", required=False)
