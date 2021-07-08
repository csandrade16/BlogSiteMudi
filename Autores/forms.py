from django import forms
from .models import Cadastro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ["nome", "sobrenome"]
