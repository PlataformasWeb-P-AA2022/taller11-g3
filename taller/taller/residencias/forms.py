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
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese una ciudad sin L por favor")
        return valor


class DepartamentoForm(ModelForm):
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
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
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
