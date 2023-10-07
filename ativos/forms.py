from django import forms
from .models import Ativos

class AtivosForm(forms.ModelForm):
    class Meta:
        model = Ativos
        fields = ['fonte_ativos', 'valor_ativos', 'data']
