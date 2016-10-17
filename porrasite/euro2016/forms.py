from django import forms

from .models import PartidoEuro2016

class PartidoEuro2016Form(forms.ModelForm):

    class Meta:
        model = PartidoEuro2016
        fields = ('local', 'visitante')

