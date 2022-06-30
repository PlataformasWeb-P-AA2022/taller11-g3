from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from residencias.models import Edificio, \
        Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese dirección por favor'),
            'ciudad': _('Ingrese ciudad por favor'),
            'tipo': _('Ingrese tipo por favor'),
        }


    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        nCiudad = valor.split()
        letra = nCiudad[0]

        if letra[0] == 'L':
            raise forms.ValidationError("No puede ingresar una ciudad que inicie con la letra 'L'")
        return valor


class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costo', 'edificio', 'nroCuartos']

class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costo', 'edificio', 'nroCuartos']

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("Ingrese sus nombres completos por favor")
        return valor

    def clean_nroCuartos(self):
        valor = self.cleaned_data['nroCuartos']
        num_cuartos = valor

        if num_cuartos < 1 or num_cuartos > 7:
            raise forms.ValidationError("El numero de cuartos validos son de 1 a 7")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        precio = valor
        if precio > 100000:
            raise forms.ValidationError("El costo no debe ser superior a $100000")
        return valor
