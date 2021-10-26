from django import forms
from .models import Cliente
from django.forms.widgets import ClearableFileInput


class ClienteForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao', 'observacao']

        error_messages = {
            'nome': {
                'required': 'O CAMPO NOME É OBRIGATÓRIO',
            }

        }