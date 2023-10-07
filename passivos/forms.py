from django import forms
from .models import Passivos

class PassivosForm(forms.ModelForm):
    class Meta:
        model = Passivos
        fields = ['fonte_passivos', 'valor_passivos', 'data']
