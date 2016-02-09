from django import forms
from .models import upload

class upload_url(forms.ModelForm):
    class Meta:
        model = upload
        fields = ('database','file_url')
