from django import forms
from .models.files import Files
from django.utils import timezone, timesince
from datetime import timedelta


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
    year = timezone.now().year
    pct_end = forms.IntegerField(label="Percentage of meeting max if no end", required=True, min_value=0, max_value=100,
                                 initial=0)
    start = forms.DateField(label="Include signings only on/after this date", required=False,
                            initial=timezone.datetime(year=year - 1, month=5, day=1),
                            widget=forms.DateInput,
                            )
    end = forms.DateField(label="Include signings only on/before this date", required=False,
                          initial=timezone.datetime(year=year, month=5, day=1),
                          widget=forms.DateInput,
                          )
