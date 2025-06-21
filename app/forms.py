from django import forms
from .models import Denuncia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import AvaliacaoRisco

class AvaliacaoRiscoForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoRisco
        fields = ['resposta_1', 'resposta_2', 'resposta_3', 'resposta_4', 'resposta_5']

class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['usuario', 'descricao', 'localizacao', 'anonima']
