from django import forms

from .models import STATUS_CHOICES

class InsertItemForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    # cantidad = forms.IntegerField(label='Cantidad')

class InsertLista(forms.Form):
    nombre = forms.CharField(label='Dale un nombre a tu lista', max_length=50)
    status = forms.ChoiceField(choices=STATUS_CHOICES)
