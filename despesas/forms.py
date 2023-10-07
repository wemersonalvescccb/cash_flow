from django import forms
from .models import Despesas

class DespesasForm(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['fonte_despesas', 'valor_despesas', 'data']
