from django import forms

class DateFilterForm(forms.Form):
    start_date = forms.DateField(label='Data de Início', widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Data de Término', widget=forms.DateInput(attrs={'type': 'date'}))
