from django.db import models


class Sala(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        
        ordering=['nombre']
    
    

class Alumnos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    tutor=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=['apellido']

class Maestras(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
    
    class Meta:
        verbose_name="Maestra"
        verbose_name_plural="Maestras"
        ordering=['apellido']

class Eventos(models.Model):
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name="Evento"
        verbose_name_plural="Eventos"    
        ordering=['fecha']