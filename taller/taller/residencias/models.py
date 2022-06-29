from django.db import models

class Edificio(models.Model):
    
	opcionesTipo = (
		('residencial', 'Residencial'),
		('comercial', 'Comercial'),
	)
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	ciudad = models.CharField(max_length=30)
	tipo = models.CharField(max_length=25, choices=opcionesTipo)

	def __str__(self):
		return "%s %s %s %s" % (self.nombre,
			self.direccion,
			self.ciudad,
			self.tipo)

	def obtener_costo_departamentos(self):
		valor = 0;
		for d in self.departamentos.all():
			valor = valor + d.costo
			return valor

			def obtener_cantidad_departamentos(self):
				valor = len(self.departamentos.all())
				return valor

class Departamento(models.Model):
    nombrePropietario = models.CharField('Nombre del Propietario' ,max_length=100)
    costo = models.DecimalField(max_digits=100, decimal_places=2)
    nroCuartos = models.IntegerField('Numero de cuartos')
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %.2f %d" % (self.nombrePropietario, 
        	self.costo,
        	self.nroCuartos)


