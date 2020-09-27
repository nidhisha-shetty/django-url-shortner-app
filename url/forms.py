from django import forms
from .models import short_urls

class urlForm(forms.ModelForm):
    class Meta:
        model=short_urls
        fields=['long_url']