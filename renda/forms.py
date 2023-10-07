from django import forms
from .models import Renda

class RendaForm(forms.ModelForm):
    class Meta:
        model = Renda
        fields = ['fonte_renda', 'valor_renda', 'categoria_renda', 'data']
