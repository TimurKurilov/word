from django import forms
from new.models import wordadd

class wordaddForm(forms.ModelForm):
    class Meta:
        model = wordadd
        fields = ['word']