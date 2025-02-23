# meu_app/forms.py
from django import forms
from .models import Reports

class ReportsForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields=['email','name','mensagem']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control'}),
        }