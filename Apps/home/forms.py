# meu_app/forms.py
from django import forms
from .models import Reports


class ReportsForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['name', 'email', 'mensagem']
        labels = {
            'name': 'Nome completo',
            'email': 'Email para contato',
            'mensagem': 'Sua mensagem',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu nome completo',
                'id': 'name-field',
                'autofocus': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@email.com',
                'id': 'email-field',
            }),
            'mensagem': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem aqui...',
                'id': 'message-field',
                'rows': 5,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes CSS adicionais ou atributos dinamicamente
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.required = True

    def clean_email(self):
        """Validação personalizada para o campo email"""
        email = self.cleaned_data.get('email')
        if email and not email.endswith(('.com', '.br', '.org', '.net')):
            raise forms.ValidationError('Por favor, forneça um email válido com domínio conhecido.')
        return email