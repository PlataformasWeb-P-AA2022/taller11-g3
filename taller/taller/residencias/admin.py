from django.contrib import admin

# Importar las clases del modelo
from residencias.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('nombrePropietario', 'costo', 'nroCuartos')

    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)
