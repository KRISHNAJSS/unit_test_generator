from django import forms
from .models import TestGenerator

class TestGeneratorForm(forms.ModelForm):
    class Meta:
        model = TestGenerator
        fields = ['code']
